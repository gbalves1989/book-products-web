from fastapi.routing import APIRouter
from fastapi.requests import Request
from fastapi.responses import Response
from app.core.config import settings


router = APIRouter()


@router.get('/signup', name='get_signup')
async def get_signup(request: Request) -> Response:
    context = {
        "request": request
    }
    
    return settings.TEMPLATES.TemplateResponse(
        'auth/signup.html', 
        context=context
    )
    

@router.get('/signin', name='get_signin')
async def get_signin(request: Request) -> Response:
    context = {
        "request": request
    }
    
    return settings.TEMPLATES.TemplateResponse(
        'auth/signin.html', 
        context=context
    )


@router.get('/reset-password', name='get_reset_password')
async def get_reset_password(request: Request) -> Response:
    context = {
        "request": request
    }
    
    return settings.TEMPLATES.TemplateResponse(
        'auth/reset-password.html', 
        context=context
    )
    

@router.get('/confirm-email', name='get_confirm_email')
async def get_confirm_email(request: Request) -> Response:
    context = {
        "request": request
    }
    
    return settings.TEMPLATES.TemplateResponse(
        'auth/confirm-email.html', 
        context=context
    )
    

@router.get('/', name='get_dashboard')
async def get_dashboard(request: Request) -> Response:
    context = {
        "request": request
    }
    
    return settings.TEMPLATES.TemplateResponse(
        'dashboard.html', 
        context=context
    )
    