import pytest 
from pydantic import ValidationError
from app.schemas.user import UserCreate

def test_valid_user():
    """Garante que o modelo aceita e armazena corretamente dados validos."""
    user = UserCreate(
        name="Luiz Henrique",
        email="meuemail@gmail.com",
        password="Minhasenha123",
    )

    assert user.name == "Luiz Henrique"
    assert user.email == "meuemail@gmail.com"

def test_valid_email():
    """Garante que uma excecao ValidationErro e emitida se o formato de e-mail for invalido."""
    with pytest.raises(ValidationError):
        UserCreate(
            name="Luiz Henrique",
            email="email-invalido",
            password="Minhasenha123",
        )  

def test_short_password():
    """Garante que uma exceção ValidationError é lançada se a senha tiver menos de 8 caracteres."""
    with pytest.raises(ValidationError):
        UserCreate(
            name="Luiz Henrique",
            email="email-invalido",
            password="123",
        )