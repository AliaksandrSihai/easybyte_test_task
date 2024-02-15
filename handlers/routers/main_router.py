from aiogram import Router

from handlers.routers.callback_routers import router as callback_router
from handlers.routers.command_router import router as command_router
from handlers.routers.state_router import router as state_router

main_router = Router()
main_router.include_routers(command_router)
main_router.include_routers(callback_router)
main_router.include_routers(state_router)
