import discord
import os

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
        await attachment.save(attachment.filename)

token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
