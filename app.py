from shiny import App
from ui.main_ui import main_ui
from views import expenses
from database import Database

db = Database("dbs/budget.db")

app_ui = main_ui()

def server(input, output, session):
    expenses.expenses_server(input, output, session, db)

app = App(app_ui, server)