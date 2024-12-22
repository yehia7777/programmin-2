from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, content):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self):
        pass


class MultiFunctionPrinter(Printer, Scanner):
    def print(self, content):
        print(f"Printing: {content}")

    def scan(self):
        print("Scanning document...")


class SimplePrinter(Printer):
    def print(self, content):
        print(f"Printing: {content}")


# استخدام الكلاسات
printer = SimplePrinter()
printer.print("Hello, world!")

multi_function_printer = MultiFunctionPrinter()
multi_function_printer.print("Document")
multi_function_printer.scan()
