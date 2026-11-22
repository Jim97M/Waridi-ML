import json
import sys
from pathlib import Path

import pandas as pd
from sqlalchemy import text

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.database.connection import engine


def inspect_tables():
    query = text("""
        SELECT
            table_schema,
            table_name
        FROM information_schema.tables
        WHERE table_schema NOT IN (
            'information_schema',
            'pg_catalog'
        )
        AND table_type = 'BASE TABLE'
        ORDER BY table_schema, table_name;
    """)

    with engine.connect() as connection:
        return pd.read_sql(query, connection)


def inspect_columns():
    query = text("""
        SELECT
            table_schema,
            table_name,
            column_name,
            data_type,
            is_nullable,
            column_default
        FROM information_schema.columns
        WHERE table_schema NOT IN (
            'information_schema',
            'pg_catalog'
        )
        ORDER BY table_schema, table_name, ordinal_position;
    """)

    with engine.connect() as connection:
        return pd.read_sql(query, connection)


def inspect_foreign_keys():
    query = text("""
        SELECT
            tc.table_schema,
            tc.table_name,
            kcu.column_name,
            ccu.table_name AS referenced_table,
            ccu.column_name AS referenced_column
        FROM information_schema.table_constraints tc
        JOIN information_schema.key_column_usage kcu
            ON tc.constraint_name = kcu.constraint_name
            AND tc.constraint_schema = kcu.constraint_schema
        JOIN information_schema.constraint_column_usage ccu
            ON ccu.constraint_name = tc.constraint_name
            AND ccu.constraint_schema = tc.constraint_schema
        WHERE tc.constraint_type = 'FOREIGN KEY'
          AND tc.table_schema NOT IN (
              'information_schema',
              'pg_catalog'
          )
        ORDER BY tc.table_schema, tc.table_name;
    """)

    with engine.connect() as connection:
        return pd.read_sql(query, connection)


def main():
    print("\nConnecting to Waridi PostgreSQL...")

    tables = inspect_tables()
    columns = inspect_columns()
    foreign_keys = inspect_foreign_keys()

    print("\n========== DATABASE TABLES ==========")
    print(tables.to_string(index=False))

    print("\n========== DATABASE COLUMNS ==========")
    print(columns.to_string(index=False))

    print("\n========== FOREIGN KEYS ==========")
    print(foreign_keys.to_string(index=False))

    # Save schema metadata, not property or customer records.
    tables.to_csv("database_tables.csv", index=False)
    columns.to_csv("database_columns.csv", index=False)
    foreign_keys.to_csv("database_foreign_keys.csv", index=False)

    print("\nSchema inspection completed.")
    print("Metadata exported to CSV files.")


if __name__ == "__main__":
    main()
