from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    """
    Esquema de dados para criacao de um usuario no sistema.
    """
    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Nome do completo do usuario",
    )

    email: EmailStr = Field(
        ...,
        description="Endereco de E-mail unico para o cadastro",
    )

    password: str = Field(
        ...,
        min_length=8,
        max_length=128,
        description="Senha do usuario",
    )


#Define o que e retornado do usuario para autenticacao 
class UserResponse(BaseModel):
    """
    Esquema de dados retornado apos o cadastro ou consulta de usuario.
    Remove dados sensiveis antes de enviar a resposta ao cliente.
    """
    id: int = Field(
        ...,
        description="Identificador unico do usuario no bando de dados",
        examples=[1]
    )
    name: str = Field(
        ..., 
        description="Nome completo do usuario cadastrado",
        examples=["Luiz Henrique"],
    )
    email: EmailStr = Field(
        ...,
        description="Endereco de E-mail do usuario cadastrado",
        examples=["meuemail@gmail.com"],
    )

    model_config = { 
        "from_attributes" : True,
        "json_schema_extra":{
            "example":{
                "id":1,
                "name":"Luiz Henrique",
                "email":"meuemail@gmail.com"
            }
        }
    }