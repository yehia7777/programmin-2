from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def calculate(self, price):
        pass


class NoDiscount(Discount):
    def calculate(self, price):
        return price


class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage

    def calculate(self, price):
        return price - (price * self.percentage / 100)


# استخدام الكلاسات
product_price = 100
discount = PercentageDiscount(10)
final_price = discount.calculate(product_price)
print(final_price)  # 90.0
