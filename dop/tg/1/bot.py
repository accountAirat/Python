import asyncio
import telegram

async def main():
    bot = telegram.Bot("5893850453:AAESI6Vw72hqsASbfiBIvuKUpzarNr8cqh8")
    async with bot:
        print((await bot.get_updates())[0])
        await bot.send_message(text='Hi John!', chat_id=1025989969)

if __name__ == '__main__':
    asyncio.run(main())
    