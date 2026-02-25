from sqlalchemy import create_engine, text

engine = create_engine('postgresql://postgres:pooja521689@localhost:5432/ecommerce_db')

with engine.connect() as conn:
    conn.execute(text('DROP TABLE IF EXISTS alembic_version CASCADE'))
    conn.execute(text('DROP TABLE IF EXISTS orders CASCADE'))
    conn.execute(text('DROP TABLE IF EXISTS products CASCADE'))
    conn.execute(text('DROP TABLE IF EXISTS categories CASCADE'))
    conn.execute(text('DROP TABLE IF EXISTS customers CASCADE'))
    conn.commit()

print("Database tables dropped successfully")
