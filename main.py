import discord
import os
import youtube_dl
import random
import nacl
from keep_alive import keep_alive
from PIL import Image
from discord.ext import commands, tasks
from discord import FFmpegPCMAudio
from replit import db



intents = discord.Intents().all()
intents.members = True
client = discord.Client(intents=intents)
# client = commands.Bot(command_prefix = "/")
bot = commands.Bot(command_prefix='!', intents=intents)

image_types = ["png", "jpeg", "gif", "jpg"]

riddle_qs = ["What happened when the shark got famous?",
"How did the hammerhead do on the Math exam?",
"What do you call a shark who wants to be by himself?",
"Why don't sharks like fast food?",
"What did the shark say to the other shark?",
"How do you throw a shark out of a bar?",
"What did the shark get on his biology test?",
"Where do sharks go on vacation?",
"Who is the most famous shark playwright?"
]

riddle_ans = ["He became a starfish.", 
 "He nailed it.",
 "A lone shark.",
 "Because they can't catch it!",
 "There’s some-fin special about you!",
 "You cast it out.",
 "A sea-minus.",
 "Finland.",
"William Sharkspeare!"
 ]


health_bar = 100
blahaj_is_active = True

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)


@client.event
async def on_message(message):
  if message.author != client.user:
    if message.content.startswith("s!frame"):
      for attachment in message.attachments:
        if any(attachment.filename.lower().endswith(image)
          for image in image_types):
          await attachment.save('input.png')
            # await message.reply(file=attachment.filename)
          await message.reply("Here's your framed pic!\n")
          newsize = (1847, 1402)
          img1 = Image.open(r"oldhaj.png").convert('RGBA')
          # img1 = img1.resize(newsize)
          img2 = Image.open(r"input.png").convert('RGBA')
          img2 = img2.resize(newsize)
          img2.paste(img1, (0, 0), img1)
          img2.save('output.png')
          with open('output.png', 'rb') as f:
            await message.channel.send(file=discord.File(f))

    if message.content.startswith("s!help"):
      await message.channel.send("```**COMMANDS:**\ns!riddle - get a random riddle\n/blahajsinging, /blahajdancing - for random videos about sharks\n/blahajplay - play music to help you relax\n\n**PET-A-SHARK: The Game - commands:**\ns!buy - buy a blahaj\ns!feed - feed your blahaj\ns!me - view your blahaj's health and points\ns!status - see where your blahaj is ```")
      

    if message.content.startswith("s!riddle"):
      string = random.choice(riddle_qs)
      await message.channel.send(string)
      index = int(riddle_qs.index(string))
      await message.channel.send("|| " + riddle_ans[index] + " ||")
      string = ""

    if message.content.startswith("/blahajdancing"):
      await message.channel.send("|| https://www.youtube.com/watch?v=dQw4w9WgXcQ ||")

    if message.content.startswith("/blahajsinging"):
      await message.channel.send(" https://www.youtube.com/watch?v=XqZsoesa55w")
    
    if message.content.startswith("/blahajplay"):
      some_reason = True
      if some_reason:await message.channel.send(file=discord.File('blahaj_in_aquarium.png'))
      
    if message.content.startswith('s!buy'):
      db[str(message.author.id)] = 0
      await message.channel.send("You bought a blahaj! Make sure you take good care of him!", file=discord.File('blahaj_in_aquarium.png'))
      # print(db)
      
    if message.content.startswith('s!status'):
      if db[str(message.author.id)] <= 0:
        await message.channel.send("Your blahaj escaped the aquarium because you didn't feed him!", file=discord.File('aquarium.png'))
      else:
        await message.channel.send("Here's your blahaj!", file=discord.File('blahaj_in_aquarium.png'))

    if message.content.startswith('s!me'):
      await message.channel.send("You have " + str(db[str(message.author.id)]) + " points")

    if message.content.startswith('s!feed'):
      db[str(message.author.id)] += 1
      await message.channel.send("Ayy, your blahaj is happy!")

#try to let the bot enter the voice channel and play the music
    if message.content.startswith('s!play'):
      channel = message.author.voice.channel
      vc = await channel.connect()
      vc.play(discord.FFmpegPCMAudio("relax.mp3"), after=lambda e: print('done', e))


def get_saw_shark_fact():
  response = requests.get("https://api.fungenerators.com/")
  json_data = json.loads(response.text) 


keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
