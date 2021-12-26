"""Ваша задача спарсить информацию о компаниях, находящихся в индексе S&P 500 с данного сайта:
https://markets.businessinsider.com/index/components/s&p_500

Для каждой компании собрать следующую информацию:

Текущая стоимость в рублях (конвертацию производить по текущему курсу, взятому с сайта центробанка РФ)
Код компании (справа от названия компании на странице компании)
P/E компании (информация находится справа от графика на странице компании)
Годовой рост/падение компании в процентах (основная таблица)
Высчитать какую прибыль принесли бы акции компании (в процентах), если бы они были куплены на уровне 52 Week Low и проданы на уровне 52 Week High (справа от графика на странице компании)
Сохранить итоговую информацию в 4 JSON файла:

Топ 10 компаний с самими дорогими акциями в рублях.
Топ 10 компаний с самым низким показателем P/E.
Топ 10 компаний, которые показали самый высокий рост за последний год
Топ 10 комппаний, которые принесли бы наибольшую прибыль, если бы были куплены на самом минимуме и проданы на самом максимуме за последний год.
Пример формата:
[
{
    "code": "MMM",
    "name": "3M CO.",
    "price" | "P/E" | "growth" | "potential profit" : value,
},
...
]
For scrapping you can use beautifulsoup4
For requesting aiohttp
"""
import asyncio
import datetime
import json
import random
import re
import time

import aiohttp
from bs4 import BeautifulSoup

URL = 'https://markets.businessinsider.com'
TABLE_URL = 'https://markets.businessinsider.com/index/components/s&p_500'
CBR_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'


async def get_usd_rate_from_cbr(session) -> float:
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
    async with session.get(TABLE_URL) as table:
        html = await table.text()
        soup = BeautifulSoup(html, features='html.parser')
        return int(*soup.find(class_='finando_paging').find_all('a')[-2])


def get_company_param(soup: BeautifulSoup, string: str):
    try:
        return float(soup.find(
            'div', class_='snapshot__header', string=string
        ).parent.contents[0].replace(',', ''))
    except AttributeError:
        return None


async def get_data(session):
    usd = await get_usd_rate_from_cbr(session)
    pages = await get_table_page_count(session)

    print(usd, 'rub')
    print(pages, 'pages')

    for page in range(1, pages+1):
        async with session.get(TABLE_URL, params=[('p', page)]) as resp:
            html = await resp.text()
            soup = BeautifulSoup(html, features='html.parser')
            companies = soup.find(class_='table__tbody').find_all('tr')

            for company in companies:
                company_url = URL + company.find('a')['href']
                growth = float(company.find_all('span')[-1].string.rstrip('%'))

                asyncio.create_task(
                    get_data_from_company_page(session, company_url, usd, growth)
                )
                await asyncio.sleep(random.randrange(0, 10) / 100)


async def get_data_from_company_page(session, url, usd, growth):
    async with session.get(url) as resp:
        html = await resp.text()
        soup = BeautifulSoup(html, features='html.parser')

        name = soup.find('span', class_='price-section__label').string
        print(name)

        code = soup.find(
            'span', class_='price-section__category'
        ).find('span').string.strip(', ')
        print(code)

        price = round(float(
            soup.find(
                'span', class_='price-section__current-value'
            ).string.replace(',', '')
        ) * usd, 2)
        print(price, 'руб')

        p_e = get_company_param(soup, 'P/E Ratio')
        print(p_e)

        year_low = get_company_param(soup, '52 Week Low')
        year_high = get_company_param(soup, '52 Week High')
        if year_low and year_high:
            potential_profit = round((year_high - year_low) / year_low * 100)
        else:
            potential_profit = None
        print(potential_profit, '% потенциальный доход')


async def main():

    async with aiohttp.ClientSession() as session:
        start = time.time()

        await get_data(session)

        print(time.time() - start, 'sec')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
