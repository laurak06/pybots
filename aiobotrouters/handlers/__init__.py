from aiogram import Router
from .router1 import router as router_1
from .router2 import router as router_2
from .router3 import router as router_3

router = Router()
router.include_routers(router_1, router_2, router_3)
