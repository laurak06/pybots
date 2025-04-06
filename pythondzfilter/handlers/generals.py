from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from pythondzfilter.database.crud import insert_food_drinks_to_table

from pythondzfilter.keyboards.simple_row import make_row_keyboard
from pythondzfilter.states.state import ChooseFood, ChooseDrink

router = Router()

available_food_name = ['burgers', 'sushi', 'xachapury']
available_food_size = ['big', 'middle', 'little']

available_drinks_name = ['kvas', 'coffee', 'tea']
available_drinks_size = ['big', 'middle', 'little']


@router.message(Command('food'))
async def cmd_food(message: Message, state: FSMContext):
    await message.answer('choose', reply_markup=make_row_keyboard(available_food_name))
    await state.set_state(ChooseFood.food_name)


@router.message(
    ChooseFood.food_name,
    F.text.in_(available_food_name)
)
async def choose_food_cmd(message: Message, state: FSMContext):
    await state.update_data(choosen_food=message.text)
    await message.answer('okay porcia', reply_markup=make_row_keyboard(available_food_size))
    await state.set_state(ChooseFood.food_size)


@router.message(
    ChooseFood.food_size,
    F.text.in_(available_food_size)
)
async def choose_food_size_cmd(message: Message, state: FSMContext):
    await state.update_data(choosen_size=message.text)
    data = await state.get_data()
    await message.answer(f'good\nfood - {data.get("choosen_food")}, size - {data.get("choosen_size")}')
    await message.answer('choose drink', reply_markup=make_row_keyboard(available_drinks_name))
    await state.set_state(ChooseDrink.drink_name)


@router.message(
    ChooseDrink.drink_name,
    F.text.in_(available_drinks_name)
)
async def choose_drink_cmd(message: Message, state: FSMContext):
    await state.update_data(choosen_drink=message.text)
    await message.answer('okay now size', reply_markup=make_row_keyboard(available_drinks_size))
    await state.set_state(ChooseDrink.drink_size)


@router.message(
    ChooseDrink.drink_size,
    F.text.in_(available_drinks_size)
)
async def choose_drink_size_cmd(message: Message, state: FSMContext):
    await state.update_data(choosen_drink_size=message.text)
    data = await state.get_data()
    await message.answer(f'good\ndrink - {data.get("choosen_drink")}, size - {data.get("choosen_drink_size")}')
    insert_food_drinks_to_table(message.from_user.id, data.get('choosen_food'), data.get("choosen_size"), data.get("choosen_drink"), data.get("choosen_drink_size"))
    await state.clear()




