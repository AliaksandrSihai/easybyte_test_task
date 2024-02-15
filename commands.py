from aiogram import types


async def set_default_commands(bot):
    await bot.set_my_commands(
        [
            types.BotCommand(command="start", description="Запустить бота"),
            types.BotCommand(command="help", description="Просмотр доступных команд"),
            types.BotCommand(command="convert", description="Конвертировать валюту"),
        ]
    )
