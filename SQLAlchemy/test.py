import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import Table, Column, Integer, String, Float, MetaData
from sqlalchemy import ForeignKey
from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import and_, or_

# engine = create_engine("mysql+pymysql://root:I65faue#ML5#@localhost/sakila?host=localhost?port=3306")
engine = create_engine("mysql+pymysql://root:I65faue#MB7#@localhost/testalchemy?host=localhost?port=3306")
conn = engine.connect()
print(f"Connection established to DB <{engine}> with SQL Alchemy version {sqlalchemy.__version__}...")

# Initialize Metadata
metadata = MetaData()

# Define object / table
user_table = Table(
    "user_account",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('fullname', String(50))
)
# print(user_table.c.name)            # name of the table => user_account
# print(user_table.c.keys())          # all column-names / keys as list => ['id', 'name', 'fullname']
# print(user_table.primary_key)       # shows the primary key of the object

# Define object / second table with foreign key
address_table = Table(
    "address",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', ForeignKey('user_account.id'), nullable=False),
    Column('email_address', String(50), nullable=False)
)

# # Create the table on the metadata definitions
# metadata.create_all(engine)

# # Inserting one row
# stmt = insert(user_table).values(name='spongebob', fullname="Spongebob Squarepants")
# with engine.connect() as conn:
#      result = conn.execute(stmt)

# # Inserting multiple rows
# with engine.connect() as conn:
#     result = conn.execute(
#         insert(user_table),
#         [
#             {"name": "sandy", "fullname": "Sandy Cheeks"},
#             {"name": "patrick", "fullname": "Patrick Star"}
#         ]
#     )    

# # Select statement
# stmt = select(user_table).where(user_table.c.name == 'spongebob')
# with engine.connect() as conn:
#     erg = conn.execute(stmt)
#     for row in erg:
#         print(row)

# stmt = select(user_table)       => Select statement with all columns from the table
# stmt = select(user_table.c.name, user_table.c.fullname))         => Select statement with only 2 defined columns

# # Select statement with and - first variant
# print(
#     select(address_table.c.email_address).
#     where(user_table.c.name == 'squidward').
#     where(address_table.c.user_id == user_table.c.id)
# )

# # Select statement with and - second variant
# print(
#     select(address_table.c.email_address).
#     where(
#          user_table.c.name == 'squidward',
#          address_table.c.user_id == user_table.c.id
#     )
# )

# Select statement with and + or:
from sqlalchemy import and_, or_
print(
    select(address_table.email_address).
    where(
        and_(
            or_(User.name == 'squidward', User.name == 'sandy'),
            address_table.user_id == User.id
        )
    )
)