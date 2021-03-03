import sys
import time

import schedule

from app.utils.Generator import Generator
from app.database.sqldb import create_table
from app.core.config import TABLE

if __name__ == "__main__":
    try:
        create_table(TABLE)
    except Exception as e:
        print(f'Unhandled exception {e}')
        sys.exit()

    schedule.every(10).seconds.do(Generator(table=TABLE).auto_fill_db)
    while True:
        schedule.run_pending()
        time.sleep(1)
