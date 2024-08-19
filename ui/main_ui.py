from shiny import ui
from ui.expenses_ui import expenses_ui
import shinyswatch

def main_ui():
    return ui.page_fluid(
        ui.navset_tab(
            ui.nav_panel("Expenses", expenses_ui())
        ),
        theme=shinyswatch.theme.vapor,
    )