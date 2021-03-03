import math
from enum import Enum
from random import choice, randint

from app.database.sql_session import SQLSession


class OPERATIONS(Enum):
    ADDITION = "+"
    SUBTRACTION = "-"
    MULTIPLICATION = "*"
    DIVISION = "/"


class REAL(Enum):
    PLUS = ""  # you don't need to mark it with +, it's + by default
    MINUS = "-"


class Generator:
    MIN_COEFFICIENTS = 4
    MAX_COEFFICIENTS = 10

    MIN_COEFFICIENT_VALUE = 1
    MAX_COEFFICIENT_VALUE = 30

    MIN_COEFFICIENT_VALUE_SPECIAL = 1
    MAX_COEFFICIENT_VALUE_SPECIAL = 10

    MIN_EQUATIONS_IN_DB = 10
    EQUATIONS_TO_PUSH_IN_DB = 1000

    TABLE = None

    def __init__(self, table):
        self.TABLE = table

    def generate_equation(self):
        coefficients = randint(self.MIN_COEFFICIENTS, self.MAX_COEFFICIENTS)
        final_equation = ""
        for _ in range(0, coefficients - 1):
            operation = choice(list(OPERATIONS))
            operation_value = operation.value
            real = choice(list(REAL))
            real_value = real.value

            if operation == OPERATIONS.DIVISION or operation == OPERATIONS.MULTIPLICATION:
                coefficient_value = randint(self.MIN_COEFFICIENT_VALUE_SPECIAL, self.MAX_COEFFICIENT_VALUE_SPECIAL)
            else:
                coefficient_value = randint(self.MIN_COEFFICIENT_VALUE, self.MAX_COEFFICIENT_VALUE)

            if real == REAL.MINUS:
                final_equation += f"({real_value}{coefficient_value}){operation_value}"
            else:
                final_equation += f"{real_value}{coefficient_value}{operation_value}"
        final_equation = final_equation[:-1]  # get rid of additional operator
        str_result = str(math.floor(eval(final_equation)))
        SQLSession().insert(table=self.TABLE,
                            columns=("equation", "result", "winner"),
                            values_types=("%s", "%s", "%s"),
                            values=(final_equation, str_result, ""))

    def auto_fill_db(self):
        print("Checking database...")
        if len(list(
                SQLSession().find_where(table=self.TABLE, column="winner", search_value=""))) < self.MIN_EQUATIONS_IN_DB:
            print(f"Filling database table {self.TABLE}...")
            for _ in range(0, self.EQUATIONS_TO_PUSH_IN_DB):
                self.generate_equation()
