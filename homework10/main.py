import asyncio
import json
import random

import aiohttp
from bs4 import BeautifulSoup

CBR_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'
URL = 'https://markets.businessinsider.com'
TABLE_URL = 'https://markets.businessinsider.com/index/components/s&p_500'


async def get_usd_rate_from_cbr(session) -> float:
    """Gets current USD rate from cbr.ru
    """
    async with session.get(CBR_URL) as resp:
        html = await resp.text()
        soup = BeautifulSoup(html, features='html.parser')
        return float(
            soup.find(
                'valute',
                id='R01235'
            ).value.string.replace(',', '.')
        )


async def get_table_page_count(session) -> int:
    """Gets actual pagination of S&P500 table
    """
    async with session.get(TABLE_URL) as table:
        html = await table.text()
        soup = BeautifulSoup(html, features='html.parser')
        return int(*soup.find(class_='finando_paging').find_all('a')[-2])


def get_company_param(soup: BeautifulSoup, param: str):
    """Gets value of parameter from company page html
    """
    try:
        return float(soup.find(
            'div', class_='snapshot__header', string=param
        ).parent.contents[0].replace(',', ''))
    except AttributeError:
        return None


async def get_data_from_company(session, url, usd, growth, data) -> None:
    async with session.get(url) as resp:
        html = await resp.text()
        soup = BeautifulSoup(html, features='html.parser')

        name = soup.find('span', class_='price-section__label').string.strip()

        code = soup.find(
            'span', class_='price-section__category'
        ).find('span').string.strip(', ')

        price = round(float(
            soup.find(
                'span', class_='price-section__current-value'
            ).string.replace(',', '')
        ) * usd, 2)

        ratio = get_company_param(soup, 'P/E Ratio')

        year_low = get_company_param(soup, '52 Week Low')
        year_high = get_company_param(soup, '52 Week High')

        if year_low and year_high:
            profit = round((year_high - year_low) / year_low * 100)
        else:
            profit = None

        company_info = {
            'code': code,
            'name': name,
            'price': price,
            'P/E': ratio,
            'growth': growth,
            'potential profit': profit
        }
        data.append(company_info)


def sort_data(data, key, reverse) -> list:
    """Returns list of 10 dicts sorted by key
    """
    result_list = []

    for item in sorted(
            data,
            key=lambda k: k[f'{key}'] if k[f'{key}'] is not None else 0,
            reverse=reverse
    )[:10]:
        result_list.append(
            {
                'code': item['code'],
                'name': item['name'],
                f'{key}': item[f'{key}']
            }
        )
    return result_list


def json_writer(data) -> None:
    """Makes json files from lists of dicts
    """
    with open('top_price.json', "w") as file:
        json.dump(sort_data(data, 'price', True), file, indent=0)
    with open('lowest_ratio.json', "w") as file:
        json.dump(sort_data(data, 'P/E', False), file, indent=0)
    with open('top_growth.json', "w") as file:
        json.dump(sort_data(data, 'growth', True), file, indent=0)
    with open('top_potential_profit.json', "w") as file:
        json.dump(sort_data(data, 'potential profit', True), file, indent=0)


async def main():
    async with aiohttp.ClientSession() as session:
        data = []
        usd = await get_usd_rate_from_cbr(session)
        pages = await get_table_page_count(session)

        for page in range(1, pages+1):
            async with session.get(TABLE_URL, params=[('p', page)]) as resp:
                html = await resp.text()
                soup = BeautifulSoup(html, features='html.parser')
                companies = soup.find(class_='table__tbody').find_all('tr')

                for company in companies:
                    company_url = URL + company.find('a')['href']
                    growth = float(
                        company.find_all('span')[-1].string.rstrip('%')
                    )
                    asyncio.create_task(
                        get_data_from_company(
                            session,
                            company_url,
                            usd,
                            growth,
                            data)
                    )
                    await asyncio.sleep(random.randrange(5, 30) / 100)
        json_writer(data)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
