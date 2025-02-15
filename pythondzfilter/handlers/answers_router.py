from aiogram import Router, F
from aiogram.types import Message
from pythondzfilter.states.state import UserFrom
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from pythondzfilter.filters.python_msg import PythonMsgFilter
from pythondzfilter.filters.time_allow import TimeMsgFilter

router = Router()
# router.message.filter(PythonMsgFilter(word='python'))

# @router.message(F.text)
# async def answer(message: Message):
#     if TimeMsgFilter(start='9:00', end='18:00'):
#         await message.answer('python at working time')
#     else:
#         await message.answer('python not at working time?')

@router.message(Command('start'))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer('Здравствуйте укажите имя')
    await state.set_state(UserFrom.name)

@router.message(UserFrom.name)
async def handler_name(message: Message, state: FSMContext):
    await state.update_data(my_name=message.text)
    await message.answer('okay а на какое время?')
    await state.set_state(UserFrom.time)

@router.message(UserFrom.time)
async def handler_name(message: Message, state: FSMContext):
    await state.update_data(my_time=message.text)
    await message.answer('okay а какие предпочтения?')
    await state.set_state(UserFrom.exact)

@router.message(UserFrom.exact)
async def handler_name(message: Message, state: FSMContext):
    await state.update_data(my_exact=message.text)
    user_data = await state.get_data()
    print(user_data)
    await state.clear()
