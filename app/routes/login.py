from fastapi import APIRouter, HTTPException,Path
from schemas.login import LoginRequest, LoginResponse

router = APIRouter()

@router.post("/login/{user_id}/{action}", response_model=LoginResponse)
async def login(user_id: str, action: str, request: LoginRequest=Path(..., description="Login request payload")):
    # Dummy authentication logic for demonstration purposes
    if request.username == "admin" and request.password == "password":
        return LoginResponse(message=f"Login successful for user {user_id} with action {action}", token="dummy_token_123")
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")