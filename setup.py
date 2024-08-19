import sqlite3
from pathlib import Path

def create_database():
    # Define database directory and path
    db_dir = Path("dbs")
    db_path = db_dir / "budget.db"

    # Create the dbs directory if it doesn't exist
    db_dir.mkdir(exist_ok=True)

    # Check if database file exists
    if db_path.exists():
        print(f"Database already exists at {db_path.resolve()}. Skipping creation.")
        return
    
    # Create new database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
    CREATE TABLE categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE NOT NULL,
        amount DECIMAL(10, 2) NOT NULL,
        description TEXT,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES categories(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE income (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE NOT NULL,
        amount DECIMAL(10, 2) NOT NULL,
        description TEXT
    )
    ''')

    # Add default categories
    default_categories = ['Food', 'Groceries', 'Entertainment', 'Other']
    for category in default_categories:
        cursor.execute("INSERT INTO categories (name) VALUES (?)", (category,))

    # Commit changes and close connection
    conn.commit()
    conn.close()

    print(f"Database created successfully at {db_path.resolve()} with default categories.")

if __name__ == "__main__":
    create_database()