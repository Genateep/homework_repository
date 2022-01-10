from homework11.task02 import Order


def test_discount_programs():

    def morning_discount(order):
        return order.price * 0.75

    def elder_discount(order):
        return order.price * 0.1

    order_1 = Order(100, morning_discount)
    assert order_1.final_price() == 75

    order_2 = Order(100, elder_discount)
    assert order_2.final_price() == 10


def test_no_discount():
    order_3 = Order(100)
    assert order_3.final_price() == 100
