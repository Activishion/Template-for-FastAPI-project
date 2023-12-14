import uvicorn

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware

from src.users import auth_router, user_router
from src.config import settings


def create_app() -> FastAPI:
    """
    The application factory using FastAPI framework.
    """

    app = FastAPI(
        title = '',
        version = '',
        debug = '',
        docs_url = "/docs",
        openapi_url ='/api/openapi.json',
        default_response_class = ORJSONResponse,
        redoc_url = None
    )

    origins_host: list = []

    allow_methods: list = ['OPTIONS', 'HEAD', 'GET', 'POST']

    allow_headers=[
        'Content-Type',
        'Set-Cookie',
        'Access-Control-Allow-Headers',
        'Access-Control-Allow-Credentials',
        'Access-Control-Allow-Origin'
    ]

    init_routers(app)
    init_middleware(app, origins_host, allow_methods, allow_headers)
    return app


def init_routers(app: FastAPI) -> None:
    app.include_router(auth_router)
    app.include_router(user_router)


def init_middleware(
    app: FastAPI,
    origins_host: list,
    allow_methods: list,
    allow_headers: list
) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins_host,
        allow_credentials=True,
        allow_methods=allow_methods,
        allow_headers=allow_headers,
    )


if __name__ == '__main__':
    uvicorn.run(
        'main:create_app',
        port = settings.PORT,
        host = settings.HOST,
        reload = settings.RELOAD
    )
