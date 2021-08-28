import discord
import os
from keep_alive import keep_alive

client = discord.Client()
image_types = ["png", "jpeg", "gif", "jpg"]

@client.event
async def on_ready():
  print("I'm in")
  print(client.user)

@client.event
async def on_message(message):
  if message.author != client.user:
    for attachment in message.attachments:
      if any(attachment.filename.lower().endswith(image) for image in image_types):
        await attachment.save('output.png')
        # await message.reply(file=attachment.filename)
        await message.reply("Here's your framed pic!\n")
        with open('output.png', 'rb') as f:
          await message.channel.send(file=discord.File(f))

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
