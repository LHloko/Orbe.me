from app.core.security import hash_password, verify_password

def test_password_hash():
    """Garante que a senha é criptografada com sucesso usando o algoritmo Argon2"""
    password = "Minhasenha123"
    
    hashed_pw = hash_password(password)

    assert hashed_pw != password
    assert hashed_pw.startswith("$argon2")

def test_password_verification():
    """Garante que a verificacao retorne True ao fornecer a senha correta"""
    password = "Minhasenha123"
    hashed_pw = hash_password(password)

    assert verify_password(password, hashed_pw)

def test_wrong_password():
    """Garante que a verificacao retorne False ao fornecer a senha incorreta"""
    password = "Minhasenha123"
    wrong_pw = "Outrasenha321"
    hashed_pw = hash_password(password)

    assert not verify_password(wrong_pw, hashed_pw)

