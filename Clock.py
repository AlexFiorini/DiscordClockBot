# bot.py
import os

from datetime import datetime
from time import sleep
import pytz

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )
    channel = client.get_channel(1012711976046182501)

    tz_Rome = pytz.timezone('Europe/Rome')
    datetime_Rome = datetime.now(tz_Rome)
    message = await channel.fetch_message(1012726198352228484)

    while 1:
        if datetime_Rome != datetime.now(tz_Rome):
            datetime_Rome = datetime.now(tz_Rome)
            testo=datetime_Rome.strftime("%H:%M")
            await message.edit(content=testo)

client.run(TOKEN)
