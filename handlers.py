from aiogram import Router
from aiogram.types import (
    Message
)

router = Router()


@router.message()
async def reply_message_handler(message: Message) -> None:
    text = message.text + " bot"
    await message.answer(text)
