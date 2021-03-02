import math
import sys
from enum import Enum
from random import choice, randint

from app.config import TABLE
from app.database.sqldb import create_table, get_database, SQLSession

MIN_COEFFICIENTS = 4
MAX_COEFFICIENTS = 10

MIN_COEFFICIENT_VALUE = 1
MAX_COEFFICIENT_VALUE = 30

MIN_COEFFICIENT_VALUE_SPECIAL = 1
MAX_COEFFICIENT_VALUE_SPECIAL = 10

session = SQLSession()


class OPERATIONS(Enum):
    ADDITION = "+"
    SUBTRACTION = "-"
    MULTIPLICATION = "*"
    DIVISION = "/"


class REAL(Enum):
    PLUS = ""  # you don't need to mark it with +, it's + by default
    MINUS = "-"


class Generator:

    @classmethod
    def equation(cls):
        coefficients = randint(MIN_COEFFICIENTS, MAX_COEFFICIENTS)
        final_equation = ""
        for _ in range(0, coefficients - 1):
            operation = choice(list(OPERATIONS))
            operation_value = operation.value
            real = choice(list(REAL))
            real_value = real.value

            if operation == OPERATIONS.DIVISION or operation == OPERATIONS.MULTIPLICATION:
                coefficient_value = randint(MIN_COEFFICIENT_VALUE_SPECIAL, MAX_COEFFICIENT_VALUE_SPECIAL)
            else:
                coefficient_value = randint(MIN_COEFFICIENT_VALUE, MAX_COEFFICIENT_VALUE)

            if real == REAL.MINUS:
                final_equation += f"({real_value}{coefficient_value}){operation_value}"
            else:
                final_equation += f"{real_value}{coefficient_value}{operation_value}"
        final_equation = final_equation[:-1]  # get rid of additional operator
        str_result = str(math.floor(eval(final_equation)))
        session.insert(table=TABLE,
                       columns=("equation", "result", "winner"),
                       values_types=("%s", "%s", "%s"),
                       values=(final_equation, str_result, ""))


if __name__ == "__main__":
    try:
        create_table()
    except Exception as e:
        print(f'Unhandled exception {e}')
        sys.exit()
    print("Nr. of equations to be generated: ")
    nr_eq = int(input())
    generator = Generator()
    for i in range(0, nr_eq):
        generator.equation()
    print(f"{nr_eq} record inserted.")

    # for result in session.select(table=TABLE):
    #     print(result)
