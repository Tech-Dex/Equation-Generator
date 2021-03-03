import sys
import time

import schedule

from app.utils.Generator import Generator
from app.database.sqldb import create_table
from app.core.config import (
    TABLE, 
    TIMER, 
    MIN_COEFFICIENTS, 
    MAX_COEFFICIENTS,
    MIN_COEFFICIENT_VALUE,
    MAX_COEFFICIENT_VALUE,
    MIN_COEFFICIENT_VALUE_SPECIAL,
    MAX_COEFFICIENT_VALUE_SPECIAL,
    MIN_EQUATIONS_IN_DB,
    EQUATIONS_TO_PUSH_IN_DB 
)

if __name__ == "__main__":
    try:
        create_table(TABLE)
    except Exception as e:
        print(f'Unhandled exception {e}')
        sys.exit()

    schedule.every(int(TIMER)).seconds.do(Generator(
        TABLE,
        MIN_COEFFICIENTS,
        MAX_COEFFICIENTS,
        MIN_COEFFICIENT_VALUE,
        MAX_COEFFICIENT_VALUE,
        MIN_COEFFICIENT_VALUE_SPECIAL,
        MAX_COEFFICIENT_VALUE_SPECIAL,
        MIN_EQUATIONS_IN_DB,
        EQUATIONS_TO_PUSH_IN_DB
    ).auto_fill_db)
    while True:
        schedule.run_pending()
        time.sleep(1)
