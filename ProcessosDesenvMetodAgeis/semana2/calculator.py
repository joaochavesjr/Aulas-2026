"""Simple calculator module with basic arithmetic operations."""


class Calculator:
    """Calculator providing basic arithmetic operations."""

    @staticmethod
    def add(a, b):
        """Return the sum of a and b."""
        return a + b

    @staticmethod
    def subtract(a, b):
        """Return the difference a - b."""
        return a - b

    @staticmethod
    def multiply(a, b):
        """Return the product of a and b."""
        return a * b

    @staticmethod
    def divide(a, b):
        """Return the quotient a / b.

        Raises
        ------
        ZeroDivisionError
            if b is zero.
        """
        if b == 0:
            raise ZeroDivisionError("division by zero")
        return a / b

if __name__ == "__main__":

    # Teste local
    # Para executar mais testes execute na linha de comando:
    #  python3 -m unittest discover -v tests
    print("Resultado 1 + 2 =", Calculator.add(1, 2))
    print("Resultado 5 - 3 =", Calculator.subtract(5, 3))
    print("Resultado 3 X 4 =", Calculator.multiply(3, 4))
    print("Resultado 10 / 2 = ", Calculator.divide(10, 2))
