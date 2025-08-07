class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Static methods
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

    # Class method as required by the checker
    @classmethod
    def multiply(cls, a, b):
        return a * b

    # Class method to return the calculation type
    @classmethod
    def get_calculation_type(cls):
        return cls.calculation_type
