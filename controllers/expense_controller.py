from models.expense import Expense
from database import Database
import pandas as pd

class ExpenseController:
    def __init__(self, db: Database):
        self.db = db

    def add_expense(self, date, amount, description, category_id):
        self.db.execute_query("INSERT INTO expenses (date, amount, description, category_id) VALUES (? , ?, ?, ?)", (date, amount, description, category_id))

    def get_all_expenses(self):
        
        query = """
        SELECT e.id, e.date, e.amount, e.description, e.category_id, c.name AS category_name
        FROM expenses e
        INNER JOIN categories c ON e.category_id = c.id
        ORDER BY e.date DESC
        """
        expenses = self.db.fetch_all(query)

        # Convert the expenses list to a pandas DataFrame
        expenses_df = pd.DataFrame(expenses, columns=["id", "date", "amount", "description", "category_id", "category_name"])

        # Convert date string to datetime
        expenses_df['date'] = pd.to_datetime(expenses_df['date'])

        return expenses_df
    
    def get_expense_by_id(self, expense_id):
        query = """
        SELECT e.id, e.date, e.amount, e.description, e.category_id, c.name as category_name
        FROM expenses e
        LEFT JOIN categories c ON e.category_id = c.id
        WHERE e.id = ?
        """
        expense = self.db.fetch_all(query, (expense_id,))

        if not expense:
            return None
        
        # Convert to pandas DataFrame
        df = pd.DataFrame([expense[0]], columns=['id', 'date', 'amount', 'description', 'category_id', 'category_name'])
        
        # Convert date string to datetime
        df['date'] = pd.to_datetime(df['date'])
        
        return df