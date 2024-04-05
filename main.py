import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware import Middleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from app.routes import home_route 
from app.routes import errors_route
from dotenv import load_dotenv

load_dotenv(".env")


middlewares = [
    Middleware(
        TrustedHostMiddleware, 
        allowed_hosts=['localhost']
    ),
]

app = FastAPI(
    docs_url=None, 
    redoc_url=None, 
    exception_handlers=errors_route.exception_handlers,
    middleware=middlewares    
    )
app.include_router(home_route.router)
app.mount('/static', StaticFiles(directory='static'), name='static')
app.mount('/media', StaticFiles(directory='media'), name='media')


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        app="main:app", 
        host=os.getenv("APP_HOST"), 
        port=int(os.getenv("APP_PORT")), 
        log_level="info"
    )
    