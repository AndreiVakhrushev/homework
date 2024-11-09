from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio

api = ""
bot = Bot(token= api)
dp = Dispatcher(bot, storage= MemoryStorage())

kb_1 = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text='Рассчитать')
button_2 = KeyboardButton(text='Информация')
kb_1.add(button_1)
kb_1.add(button_2)

kb_2 = InlineKeyboardMarkup(resize_keyboard=True)
button_1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_2.add(button_1)
kb_2.add(button_2)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    print("Выберите опцию:")
    await message.answer("Выберите опцию:", reply_markup=kb_2)

@dp.callback_query_handler(text=['formulas'])
async def get_formulas(call):
    print("(10 х вес в кг) + (6,25 х рост в см) – (5 х возраст в годах)")
    await call.message.answer("Формула Миффлина-Сан Жеора:(10 х вес в кг) + (6,25 х рост в см) – (5 х возраст в годах)")

@dp.message_handler(commands=['start'])
async def start_message(message):
    print("Привет! Я бот помогающий твоему здоровью.")
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb_1)

@dp.message_handler(text=['Информация'])
async def inform(message):
    await message.answer("Это информация о боте!")

@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    print("Введите свой возраст в годах:")
    await call.message.answer("Введите свой возраст в годах:")
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    print("Введите свой рост в см:")
    await message.answer("Введите свой рост в см:")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    print("Введите свой вес в кг:")
    await message.answer("Введите свой вес в кг:")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age'])
    await message.answer(f'По формуле Миффлина-Сан Жеора норма для Вас - {calories} калорий')
    await state.finish()

@dp.message_handler()
async def all_message(message):
    print("Введите команду /start, чтобы начать общение.")
    await message.answer("Введите команду /start, чтобы начать общение.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
