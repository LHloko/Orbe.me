from collections.abc import Generator
from sqlalchemy.orm import Session

import jwt 
from fastapi import Depends,HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.config import settings
from app.db.session import SessionLocal
from app.models.user import User

security = HTTPBearer()

def get_db() -> Generator[Session, None, None]:
	db = SessionLocal()
	
	try:
		yield db
	finally:
		db.close()

def get_current_user(
	credentials: HTTPAuthorizationCredentials = Depends(security),
	db: Session = Depends(get_db),
) -> User:
	token = credentials.credentials

	try: 
		payload = jwt.decode(
			token,
			settings.JWT_SECRET_KEY,
			algorithms=[settings.JWT_ALGORITHM],
		)

		user_id = payload.get("sub")

		if user_id is None:
			raise HTTPException(
				status_code=status.HTTP_401_UNAUTHORIZED,
				detail="Invalid authentication credentials",
			)

	except jwt.PyJWKError as exc:
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail="Invalid authentication credentials",
		) from exc

	user = db.get(User, int(user_id))

	if user is None:
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail="User not found",
		)

	return user