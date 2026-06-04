from fastapi import APIRouter

from app.core.deps import CurrentUser
from app.schemas.user import UserOut

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserOut)
async def get_me(current_user: CurrentUser):
    return current_user
