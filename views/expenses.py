from shiny import reactive, render
from controllers.expense_controller import ExpenseController

def expenses_server(input, output, session, db):
    controller = ExpenseController(db)

    @reactive.effect
    @reactive.event(input.add_expense)
    def add_expense():
        controller.add_expense(
            input.expense_date(),
            input.expense_amount(),
            input.expense_description(),
            input.expense_category()
        )

    @render.data_frame
    def expenses_table():
        return controller.get_all_expenses()