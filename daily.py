import os
# ========================================================
# To write a code "pg_dump -U postgres -h localhost -p 5432 -F c -f база.psql postgres"
# to create a backup of the database with the help of python


def save_db_at_this_point():
    os.system('pg_dump -U postgres -h localhost -p 5432 -F c -f db.psql postgres')

def read_db():
    os.system("pg_restore -U postgres -h localhost -p 5432 -d postgres db.psql")


# save_db_at_this_point()
# read_db()
# ========================================================
# .com - commercial
# .org - organization
# .net - network
# .gov - government
# .ru  - Russia
# .ua  - Ukraine
# .uz  - Uzbekistan
# .us  - United States
