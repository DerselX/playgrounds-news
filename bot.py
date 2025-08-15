import requests

from aiogram import Bot, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bs4 import BeautifulSoup
import asyncio, os

from dotenv import load_dotenv

load_dotenv()


dp = Dispatcher()
bot = Bot(token=os.getenv("BOT_TOKEN"))

# функция для отправки запроса на сервер
def get_connection_playgrounds() -> BeautifulSoup:
    response = requests.get("https://www.playground.ru/news")
    soup = BeautifulSoup(response.content, "lxml")

    return soup

def about_url_news(url):
    
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")

    get_desc = soup.find("p").contents[0]
    return get_desc
    
# функция для парсер блоков: название, дата публикации, описание и т.д
def block_parser():
    soup = get_connection_playgrounds()

    # берём основной блок новостей
    block = soup.find_all("div", "post")
    

    # словарь с данными
    news = []
    for el in block:
        images = el.find("img").get("src")
        
        blockf = el.find("div", "post-title")
        title = blockf.find("a").contents[0]
        time = el.find("div", "post-content")
        date = time.find("div", "post-metadata")
        date2 = date.find("time").contents[0]

        #print(date2)
        get_description = about_url_news(blockf.find("a").get("href"))
        news.append({"img": images, "title": title, "link": blockf.find("a").get("href"), "description": get_description, "time": date2 })

    return news



async def send_to_channel():
    method = block_parser()
    item = method[1]
      
    await bot.send_photo(chat_id=os.getenv("CHANNEL_ID"), photo=f"{item['img']}", caption=f"<b> 🌐 {item['title']} </b>\n{item['description']} \n<b>⌚ Дата публикации:</b> {item['time']}", reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton( text='▶ Перейти', url=item['link'] ) ]]), parse_mode="HTML")
    await asyncio.sleep(2.3)

async def main():
    await send_to_channel()
    #await dp.start_polling(bot)
    await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())