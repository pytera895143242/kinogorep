from aiogram import types
from misc import dp,bot
from .sqlit import reg_user
from .generate_markup import subscription_markup, check_subscription, open_markup

file_id = "AgACAgIAAxkBAAMZZb4eE5skBSjW7S9J_Ibgp1tg8hgAAmfWMRsKhvBJ41LlLlzrQG8BAAMCAANzAAM0BA"

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    if len(message.text) == 6:
        reg_user(message.chat.id,'default')
    else:
        reg_user(message.chat.id,(message.text[7:]))

    if await check_subscription(message.chat.id) == True:
        await message.answer("""<b>Привет, киноман!</b>

Какой фильм или сериал ты хочешь посмотреть? Напиши мне название!""",reply_markup=open_markup())
    else:
        await bot.send_photo(message.chat.id, photo=file_id,caption="""<b>⭐️ Для полноценного использования КИНОБОТА, подпишитесь на наших спонсоров:</b>""",reply_markup=subscription_markup())