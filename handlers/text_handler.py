from aiogram import types
from misc import dp,bot
import asyncio
from .sqlit import get_info_key,get_info_fav
from .find_mov import find_m
from .generate_markup import subscription_markup, check_subscription

file_id = "AgACAgIAAxkBAAMZZb4eE5skBSjW7S9J_Ibgp1tg8hgAAmfWMRsKhvBJ41LlLlzrQG8BAAMCAANzAAM0BA"

film1 = ["AgACAgIAAxkBAAMjZb4ejIOANPW-3c2Qg4b4Tbk2_rwAAjfGMRt6t3FLxBradYq0JGYBAAMCAANzAAM0BA", "https://findmovie.bazon.site/embed/f7eab5f7cdc2ff628cddf1d741d2d450/91227","""<b>Кот в сапогах 2: Последнее желание [2022 | +16]\n\nРейтинг: 8.563</b>\n\nКот в сапогах потратил восемь из девяти отпущенных ему жизней и теперь отправляется в новое приключение, чтобы отыскать мифическое Последнее желание и восстановить свои жизни."""]
film2 = ["AgACAgIAAxkBAAMkZb4ejLwJ4CFTIg1lLiY9EnirhikAAjnGMRt6t3FLbZfZPQaCW7ABAAMCAANzAAM0BA" , "https://findmovie.bazon.site/embed/ada0fd346081137bf83ec0c530e45791/89290","<b>М3ГАН [2022 | +16]\n\nРейтинг:</b> 7.545\n\nДжемма — робототехник в компании по производству игрушек. Неожиданно получив опеку над своей недавно осиротевшей племянницей, она дарит девочке экспериментальную куклу-андроид, которая вскоре в буквальном смысле понимает свою миссию защищать ребенка."]
film3 = ["AgACAgIAAxkBAAMlZb4ejLTCMdBvKpjcmmtXx3shX8IAAjrGMRt6t3FLfza-yrDF390BAAMCAANzAAM0BA", "https://findmovie.bazon.site/embed/c0b1535adc34536b5f7ac51dfc5068b3/88143","<b>Black Panther: Wakanda Forever [2022 | +16]\n\nРейтинг:</b> 7.552\n\nКоролевство Ваканда погрузилось в хаос: король Т'Чалла умирает от тяжелой болезни, оставляя мать Рамонду, сестру Шури и всю страну в глубоком трауре, а также лишает ее защитника - Черной пантеры. После как весь мир узнал что Ваканда осталась без самого главного защитника Ваканды, у США и Франции появилось желание заполучить вибраниум любым способом. Тем временем мировое сообщество требует свободного использования вибраниума - одного из самый мощных металлов на планете, и пытается добывать его в других местах. Во время одной из таких вылазок происходит столкновение людей с новой расой - воинами подводного города Талокан, которых возглавляет могущественный Нэмор. Он же делает предложение Ваканде: выступить на его стороне, когда он пойдет войной на людей, а в случае отказа, он выступит против самой Ваканды..."]
film4 = ["AgACAgIAAxkBAAMmZb4ejHvQiP7Nc3245UNRITsD9dcAArnOMRuDgHlLb4x1uRQgvrABAAMCAANzAAM0BA", "https://findmovie.bazon.site/embed/d1bb4bb1e0a4399959215712216c0c1d/88568","<b>Аватар: Путь воды [2022 | +16]\n\nРейтинг: 7.745</b>\n\nПосле принятия образа аватара солдат Джейк Салли становится предводителем народа на'ви и берет на себя миссию по защите новых друзей от корыстных бизнесменов с Земли. Теперь ему есть за кого бороться — с Джейком его прекрасная возлюбленная Нейтири. Когда на Пандору возвращаются до зубов вооруженные земляне, Джейк готов дать им отпор."]
film5 = ["AgACAgIAAxkBAAMnZb4ejFaQCHkuPoA4WnA_odCavjQAAjvGMRt6t3FLh-s2TlujhGsBAAMCAANzAAM0BA", "https://findmovie.bazon.site/embed/a08a2874be3861b12b2ec9d5aa2e7445/89289","<b>Двойная петля [2022 | +16]\n\nРейтинг:</b> 7.561\n\nДва пилота американских ВМС во время Корейской войны становятся близкими друзьями и братьями по оружию. Во время очередного задания одного из лётчиков подбивают аккурат над вражеской территорией. Командование не видит необходимости в спасательной операции, но истинная преданность не позволит солдату оставить товарища в беде..."]
film6 = ["AgACAgIAAxkBAAMoZb4ejHOJmmTkwzdu9D_5cBEwDwcAAjzGMRt6t3FL7DFOUhaQdXsBAAMCAANzAAM0BA", "https://findmovie.bazon.site/embed/a3a304fea5d7741a959e805d1564be9a","<b>Зловещий свет [2022 | +16]\n\nРейтинг: 7.285</b>\n\n25-летняя монахиня Энн уверена, что ее призвание – изгнание дьявола, хотя обряд экзорцизма разрешено совершать только священникам. Несмотря на запреты, она приступает к своей миссии, но скоро лицом к лицу сталкивается с ужасающими демонами. Сможет ли Энн противостоять силам зла и открыть тайну своего мистического дара?"]
film7 = ["AgACAgIAAxkBAAMpZb4ejOOxyxGBgkRQG3QcPGbMRyUAAj3GMRt6t3FLSVbNnongjIkBAAMCAANzAAM0BA", "https://findmovie.bazon.site/embed/fe31f5e0b84b83a14d1f1295d68a4ccc/86715","<b>Достать ножи: Стеклянная луковица [2022 | +16]\n\nРейтинг: 7.099</b>\n\nПродолжение иронического детектива 2019 года. Новое расследование сыщика Бенуа Бланка (Дэниэл Крэйг) будет происходить на частном острове в Греции. Миллиардер Майлз Брон (Эдвард Нортон) приглашает к себе разношёрстную компанию друзей. Вскоре на вечеринке происходит убийство."]

films = [film1,film2,film3,film4,film5,film6,film7]

@dp.message_handler(content_types='text')
async def all_other_messages(message: types.message):
    if await check_subscription(message.chat.id) == True:
        if message.text == "Поиск фильмов 🔎":
            await bot.send_photo(message.chat.id, photo=file_id, caption="""<b>Вы запустили поиск фильмов 🔎</b> \n\nНапишите мне название фильма или сериала...""")

        elif message.text == "Фильм из ТикТок 🎬":
            await message.answer("<b>Введи поисковый запрос</b>")

        elif message.text == "Новинки 🎊":
            for f in films:
                markup = types.InlineKeyboardMarkup()
                bat_a = types.InlineKeyboardButton(text='🖥 Смотреть фильм', url=f[1])
                bat_b = types.InlineKeyboardButton(text='⭐️ Добавить в избранное', callback_data=f'iz_{f[1][46:]}')
                markup.add(bat_a)
                markup.add(bat_b)
                await bot.send_photo(message.chat.id, photo=f[0],caption=f[2],reply_markup=markup)

        elif message.text == "Избранное ❤️":
            fav_txt = ""
            data_f = get_info_fav(message.chat.id)
            for f in data_f:
                fav_txt += f"<a href = '{f[1]}'>" + f"👉🏻 {f[2]}..." + "</a>" + "\n"

            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='🗑 Удалить все', callback_data='del_fav')
            markup.add(bat_a)
            await bot.send_photo(message.chat.id, photo=file_id, caption=f"""<b>Пришло время посмотреть что-то из избранного? \n\n{fav_txt}\nФильмы в избранном </b>""",reply_markup=markup)


        elif message.text == "Информация ⚙️":
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='👨🏻‍💻 Администратор', url='https://t.me/admin')
            markup.add(bat_a)
            await bot.send_photo(message.chat.id, photo=file_id,caption="""<b>Краткий информационный стенд кинотеатра 🎥</b>\n\n0\n\nПо всем вопросам обращайтесь к администратору""",reply_markup=markup)

        elif message.text == "FAQ ?":
            await message.answer("Если Вы владелец авторских прав или его представитель, просим Вас учесть, что все ссылки в боте берутся из сторонних источников, сайтов, видео-хостингов. Мы не имеем отношения к размещенным материалам по этим ссылкам. \n\nБот работает по принципу поисковой системы.")
        else:
            info = (get_info_key(message.text))
            if len(info) != 0:
                await message.answer(f"{message.text} - {info[0][2]}")

            else:
                await find_m(message)
    else:
        await bot.send_photo(message.chat.id, photo=file_id,caption="""<b>⭐️ Для полноценного использования КИНОБОТА, подпишитесь на наших спонсоров:</b>""",reply_markup=subscription_markup())


@dp.message_handler(content_types='photo')
async def all_fdsfdsessages(message: types.message):
    print(message.photo[0].file_id)

    pass