"""
PJECZ Carina API Key
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

from config.settings import get_settings

from .v4.autoridades.paths import autoridades
from .v4.bitacoras.paths import bitacoras
from .v4.distritos.paths import distritos
from .v4.entradas_salidas.paths import entradas_salidas
from .v4.estados.paths import estados
from .v4.exh_areas.paths import exh_areas
from .v4.exh_exhortos.paths import exh_exhortos
from .v4.exh_exhortos_archivos.paths import exh_exhortos_archivos
from .v4.exh_exhortos_partes.paths import exh_exhortos_partes
from .v4.materias.paths import materias
from .v4.modulos.paths import modulos
from .v4.municipios.paths import municipios
from .v4.permisos.paths import permisos
from .v4.roles.paths import roles
from .v4.tareas.paths import tareas
from .v4.usuarios.paths import usuarios
from .v4.usuarios_roles.paths import usuarios_roles


def create_app() -> FastAPI:
    """Crea la aplicación FastAPI"""

    # FastAPI
    app = FastAPI(
        title="PJECZ Carina API Key",
        description="API con autentificación para enviar y recibir exhortos.",
        docs_url="/docs",
        redoc_url=None,
    )

    # CORSMiddleware
    settings = get_settings()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.origins.split(","),
        allow_credentials=False,
        allow_methods=["GET", "POST"],
        allow_headers=["*"],
    )

    # Rutas
    app.include_router(autoridades, include_in_schema=False)
    app.include_router(bitacoras, include_in_schema=False)
    app.include_router(distritos, include_in_schema=False)
    app.include_router(entradas_salidas, include_in_schema=False)
    app.include_router(estados)
    app.include_router(exh_areas)
    app.include_router(exh_exhortos)
    app.include_router(exh_exhortos_archivos)
    app.include_router(exh_exhortos_partes)
    app.include_router(materias)
    app.include_router(modulos, include_in_schema=False)
    app.include_router(municipios)
    app.include_router(permisos, include_in_schema=False)
    app.include_router(roles, include_in_schema=False)
    app.include_router(tareas, include_in_schema=False)
    app.include_router(usuarios, include_in_schema=False)
    app.include_router(usuarios_roles, include_in_schema=False)

    # Paginación
    add_pagination(app)

    # Mensaje de Bienvenida
    @app.get("/")
    async def root():
        """Mensaje de Bienvenida"""
        return {"message": "API con autentificación para enviar y recibir exhortos."}

    # Entregar
    return app
