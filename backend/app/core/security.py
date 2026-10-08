from datetime import datetime, timedelta, timezone
from pwdlib import PasswordHash
import jwt 

from app.core.config import settings

#Inicilizando com as configuracoes recomendadas da biblioteca
password_hash = PasswordHash.recommended()

#Hasheia (toma essa lirica aqui) a senha
def hash_password(password: str) -> str:
    return password_hash.hash(password)

#Verifica a senha
def verify_password(password: str, hashed_password) -> bool:
    return password_hash.verify(password, hashed_password)

# Cria o token de acesso 
def create_acess_token(user_id: int) -> str:
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.JWT_EXPIRE_MINUTES
    )

    payload ={
        "sub": str(user_id),
        "exp": expire
    }

    return jwt.encode(
        payload,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM
    )