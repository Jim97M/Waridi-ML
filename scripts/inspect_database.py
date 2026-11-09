import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.database.connection import test_connection


if __name__ == "__main__":
    try:
        result = test_connection()

        print("Database connection successful!")
        print(f"Database: {result[0]}")
        print(f"User: {result[1]}")

    except Exception as error:
        print("Database connection failed:")
        print(error)
        