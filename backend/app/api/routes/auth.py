from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.auth import create_user
from app.core.security import create_acess_token
from app.services.auth import authenticate_user
from app.schemas.auth import LoginRequest, TokenResponse
from app.core.dependencies import get_current_user
from app.models.user import User 

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)

def register(
    user_data: UserCreate,
    db: Session = Depends(get_db),
): 
    try:
        return create_user(db, user_data)
    
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        )from exc

@router.post(
        "/login",
        response_model=TokenResponse,
)
def login(
    login_data: LoginRequest,
    db: Session = Depends(get_db),
):
    user = authenticate_user(db, login_data.email, login_data.password)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid e-mail or password",
        )

    acess_token = create_acess_token(user.id)

    return TokenResponse(
        access_token=acess_token,
        token_type="bearer",
    )

@router.get(
    "/me",
    response_model=UserResponse,
)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user


