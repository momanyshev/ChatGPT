import config
import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

openai.api_key = config.OPENAI_TOKEN

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def send(message : types.Message):
  response = openai.Completion.create(
  model="text-davinci-003",
  prompt=message.text,
  temperature=0.9,
  max_tokens=2048,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.6
)

  await message.answer(response['choices'][0]['text'])

executor.start_polling(dp, skip_updates=True)

