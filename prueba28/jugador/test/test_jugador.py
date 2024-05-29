import pytest

from prueba28.jugador.jugador import Jugador


@pytest.fixture
def jugador():
    return jugador("William", "Cricket")

def test_read(jugador):
    assert jugador.read() == "William,Cricket"