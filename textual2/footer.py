from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer


class FooterApp(App):
    BINDINGS = [
        Binding(key="q", action="quit", description="Quit the app"),
        Binding(
            key="e",
            action="help",
            description="editar"
        ),
        
        Binding(
            key="n",
            action="2",
            description="Nuevo"
        ),
        
        Binding(
            key="b",
            action="help3",
            description="borrar"
        ),
    ]

    def compose(self) -> ComposeResult:
        yield Footer()


if __name__ == "__main__":
    app = FooterApp()
    app.run()