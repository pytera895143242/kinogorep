import asyncio
from misc import dp, bot
from .sqlit import info_members
import datetime, pytz
channel = -1002098357551

last_day = 0
last_hour = 0

def second_time(finish_data):
    hours_f = int(finish_data[0:2]) #Часы финиша
    min_f = int(finish_data[3:]) #Минуты финиша
    second_f = 0

    hours_now = datetime.datetime.now(pytz.timezone('Europe/Moscow')).hour
    min_now = datetime.datetime.now(pytz.timezone('Europe/Moscow')).minute
    seconf_now = datetime.datetime.now(pytz.timezone('Europe/Moscow')).second


    time_now = datetime.datetime(year = 2023,month = 1,day = 1, hour = hours_now,minute = min_now,second = seconf_now)
    time_finish = datetime.datetime(year = 2023,month = 1,day = 1, hour = hours_f,minute = min_f,second = second_f)

    delta = (time_finish-time_now).seconds
    return delta




async def while_stat():
    global last_hour
    global last_day
    while True:
        hours_now = datetime.datetime.now(pytz.timezone('Europe/Moscow')).hour

        if hours_now == 23:
            t = second_time("23:59")
            await asyncio.sleep(t)

            info = info_members()
            await bot.send_message(chat_id=channel,text=f"За последний час: {info - last_hour}")
            await bot.send_message(chat_id=channel, text = f"""24 часа назад: {last_day}\nCейчас: {info}\nИзменение:{info-last_day}""")
            last_hour = info
            last_day = info

        if hours_now == 22:
            t = second_time("22:59")
            await asyncio.sleep(t)

            info = info_members()
            await bot.send_message(chat_id=channel, text=f"За последний час: {info - last_hour}")
            last_hour = info

        if hours_now == 21:
            t = second_time("21:59")
            await asyncio.sleep(t)

            info = info_members()
            await bot.send_message(chat_id=channel, text=f"За последний час: {info - last_hour}")
            last_hour = info

        if hours_now == 20:
            t = second_time("20:59")
            await asyncio.sleep(t)

            info = info_members()
            await bot.send_message(chat_id=channel, text=f"За последний час: {info - last_hour}")
            last_hour = info

        if hours_now == 19:
            t = second_time("19:59")
            await asyncio.sleep(t)

            info = info_members()
            await bot.send_message(chat_id=channel, text=f"За последний час: {info - last_hour}")
            last_hour = info

        if hours_now == 18:
            t = second_time("18:59")
            await asyncio.sleep(t)

            info = info_members()
            await bot.send_message(chat_id=channel, text=f"За последний час: {info - last_hour}")
            last_hour = info

        if hours_now == 17:
            t = second_time("17:59")
            await asyncio.sleep(t)
            info = info_members()

            await bot.send_message(chat_id=channel, text=f"За последний час: {info - last_hour}")
            last_hour = info

        if hours_now == 16:
            t = second_time("16:59")
            await asyncio.sleep(t)

            info = info_members()
            await bot.send_message(chat_id=channel, text=f"За последний час: {info - last_hour}")
            last_hour = info

        if hours_now == 15:
            t = second_time("15:59")
            await asyncio.sleep(t)

            info = info_members()
            await bot.send_message(chat_id=channel, text=f"За последний час: {info - last_hour}")
            last_hour = info

        if hours_now == 14:
            t = second_time("14:59")
            await asyncio.sleep(t)

            info = info_members()
            await bot.send_message(chat_id=channel, text=f"За последний час: {info - last_hour}")
            last_hour = info

        if hours_now == 13:
            t = second_time("13:59")
            await asyncio.sleep(t)

            info = info_members()
            await bot.send_message(chat_id=channel, text=f"За последний час: {info - last_hour}")
            last_hour = info

        if hours_now == 12:
            t = second_time("12:59")
            await asyncio.sleep(t)

            info = info_members()
            await bot.send_message(chat_id=channel, text=f"За последний час: {info - last_hour}")
            last_hour = info

        if hours_now == 11:
            t = second_time("11:59")
            await asyncio.sleep(t)

            info = info_members()
            await bot.send_message(chat_id=channel, text=f"За последний час: {info - last_hour}")
            last_hour = info

        if hours_now == 10:
            t = second_time("10:59")
            await asyncio.sleep(t)

            info = info_members()
            await bot.send_message(chat_id=channel, text=f"За последний час: {info - last_hour}")
            last_hour = info

        if hours_now == 9:
            t = second_time("09:59")
            await asyncio.sleep(t)

            info = info_members()
            await bot.send_message(chat_id=channel, text=f"За последний час: {info - last_hour}")
            last_hour = info

        if hours_now == 8:
            t = second_time("08:59")
            await asyncio.sleep(t)

            info = info_members()
            await bot.send_message(chat_id=channel, text=f"За последний час: {info - last_hour}")
            last_hour = info

        if hours_now == 7:
            t = second_time("07:59")
            await asyncio.sleep(t)

            info = info_members()
            await bot.send_message(chat_id=channel, text=f"За последний час: {info - last_hour}")
            last_hour = info

        if hours_now == 6:
            t = second_time("06:59")
            await asyncio.sleep(t)

            info = info_members()
            await bot.send_message(chat_id=channel, text=f"За последний час: {info - last_hour}")
            last_hour = info

        if hours_now == 5:
            t = second_time("05:59")
            await asyncio.sleep(t)

            info = info_members()
            await bot.send_message(chat_id=channel, text=f"За последний час: {info - last_hour}")
            last_hour = info

        if hours_now == 4:
            t = second_time("04:59")
            await asyncio.sleep(t)

            info = info_members()
            await bot.send_message(chat_id=channel, text=f"За последний час: {info - last_hour}")
            last_hour = info

        if hours_now == 3:
            t = second_time("03:59")
            await asyncio.sleep(t)

            info = info_members()
            await bot.send_message(chat_id=channel, text=f"За последний час: {info - last_hour}")
            last_hour = info

        if hours_now == 2:
            t = second_time("02:59")
            await asyncio.sleep(t)

            info = info_members()
            await bot.send_message(chat_id=channel, text=f"За последний час: {info - last_hour}")
            last_hour = info

        if hours_now == 1:
            t = second_time("01:59")
            await asyncio.sleep(t)

            info = info_members()
            await bot.send_message(chat_id=channel, text=f"За последний час: {info - last_hour}")
            last_hour = info

        if hours_now == 0:
            t = second_time("00:59")
            await asyncio.sleep(t)

            info = info_members()
            await bot.send_message(chat_id=channel, text=f"За последний час: {info - last_hour}")
            last_hour = info


        await asyncio.sleep(1800) #Проверяем каждые 30 минут
