from shiny import ui

def expenses_ui():
    
    return ui.div(
        ui.h2("Expenses"),
        ui.input_date("expense_date", "Date"),
        ui.input_numeric("expense_amount", "Amount", value=0),
        ui.input_text("expense_description", "Description"),
        ui.input_select("expense_category", "Category", ["Food", "Groceries", "Entertainment", "Other"]),
        ui.input_action_button("add_expense", "Add Expense"),
        ui.output_table("expenses_table")
    )