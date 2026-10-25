import os
import discord
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

TARGET_CHANNEL_ID = 1560270031386976327  # استبدل هذا الرقم بـ آي دي قناتك في ديسكورد

STICKY_CONTENT = """📌 **أهلاً بك في المختبر**
يرجى إلقاء نظرة على القوانين والحفاظ على بيئة المخبر. شكراً لتفهمكم!"""

last_sticky_message = None


@client.event
async def on_ready():
  global last_sticky_message
  print(f'تم تشغيل البوت بنجاح باسم: {client.user}')
  keep_alive()  # تشغيل خادم الإبقاء على الاتصال
  channel = client.get_channel(TARGET_CHANNEL_ID)
  if channel:
    async for message in channel.history(limit=5):
      if message.author == client.user:
        await message.delete()
    last_sticky_message = await channel.send(STICKY_CONTENT)
    print('تم إرسال الستيكي مسج بنجاح.')


@client.event
async def on_message(message):
  global last_sticky_message

  if message.author.bot:
    return

  if message.channel.id == TARGET_CHANNEL_ID:
    if last_sticky_message:
      try:
        await last_sticky_message.delete()
      except:
        pass

    last_sticky_message = await message.channel.send(STICKY_CONTENT)


# قراءة التوكن من بيئة السيرفر بأمان
TOKEN = os.getenv('BOT_TOKEN')
client.run(TOKEN)
