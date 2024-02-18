from vkbottle.user import User, UserLabeler, Message, rules
from settings import settings
from aiogram import Bot

user = User(settings.VK_TOKEN)
bot = Bot(settings.TG_TOKEN)

labeler = UserLabeler()
labeler.auto_rules = [rules.FromPeerRule(settings.VK_PEER_ID)]

@labeler.private_message()
async def on_message_recv(message: Message):
    await bot.send_message(chat_id=settings.TG_CHAT_ID, text=message.text)

user.labeler.load(labeler)

user.run_forever()