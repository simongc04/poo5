from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, Static


class ButtonsApp(App[str]):
    CSS_PATH = "button.tcss"

    def compose(self) -> ComposeResult:
        yield Horizontal(
            VerticalScroll(
                Static("Botones", classes="header"),
                Button("Entrar", id="butEntrar"),
                Button("Salir", id="butSalir"),
            ),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "butEntrar":
            self.notify(
            "Now witness the firepower of this fully "
            "[b]ARMED[/b] and [i][b]OPERATIONAL[/b][/i] battle station!",
            title="Possible trap detected",
            severity="warning",
        )
        elif button_id == "butSalir":
            self.log("Botón 'Salir' presionado. Cerrando la aplicación...")
            self.exit("Has salido.")
        else:
            self.log(f"Botón desconocido presionado: {button_id}")


if __name__ == "__main__":
    app = ButtonsApp()
    print(app.run())
