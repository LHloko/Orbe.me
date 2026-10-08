from pydantic import BaseModel, EmailStr, Field

class LoginRequest(BaseModel):
    """
    Esquema de dados para a requisição de login do usuario
    """
    email: EmailStr = Field(
        ...,
        description="Endereco de email cadastrado pelo usuario",
        examples=["meuemail@gmail.com"],
    )
    password: str = Field(
        ...,
        description="Senha do usuario sem hash",
        examples=["Minhasenha123"],
    )

class TokenResponse(BaseModel):
    """
    Esquema de dados para reposta de autenticacao bem-sucedida.
    """
    access_token: str = Field(
        ...,
        description="Token de acesso JWT gerado para o usuario",
    )
    token_type: str = Field(
        default="bearer",
        description="O tipo de token emitido",
    )

