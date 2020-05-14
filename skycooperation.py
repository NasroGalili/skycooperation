import discord
from discord.ext import commands

import asyncio
import re
from datetime import datetime
from random import randint, random, choice
from discord.ext.commands import command, UserConverter, BucketType, Command
client = commands.Bot(command_prefix ='.')

@client.event
async def on_ready():
    print('I am ready!')

@client.command()
async def krill(ctx,*, victim):
    def __init__(self, bot):
        super().__init__(bot)
        self.krilled = dict()
        self.channels = dict()
        self.monsters = dict()
        self.ignored = set()
        self.loaded = False
    victim_name = victim
    client = commands.Bot(command_prefix = '.')
    head = "<:krillhead:710049231234400356>"
    body = "<:krillbody:710049223969603594>"
    tail = "<:krillback:710049219179839538>"
    red = "<:moth:710049237173534771>"
    star = "<:wingbuff:710049235361595392>"
    blank = "<:emptye:710049214968758373>"
    ded = "<:lookdead:710049227732156456>" if victim_name != "skycooperation" else ':robot:' if victim_name == "banana" else 'banana'
    time_step = 1
    step = randint(1, 2)
    distance = step * 3
    spaces = str(blank) * distance
    spacestep = str(blank) * step
    message = await ctx.send(f"{spacestep}{victim_name} {red}{spaces}{head}{body}{tail}")
    await ctx.send(f"*summoned by {ctx.author.mention}*")
    while distance > 0:
        distance = distance - step
        spaces = str(blank) * distance
        await message.edit(content=f"{spacestep}{victim_name} {red}{spaces}{head}{body}{tail}")
        await asyncio.sleep(time_step)

    step = randint(0, 2)
    distance = step*3
    count = 0
    secaps = ""
    while count < distance:
        spaces = str(blank) * count
        count = count + step
        secaps = str(blank) * (distance - count)
        await message.edit(content=f"{secaps}{star}{spaces}{ded} {victim_name}{spaces}{star}{spaces}{star}")
        await asyncio.sleep(time_step)
    await message.edit(content=f"{secaps}{star}{spaces}{ded} {victim_name}{spaces}{star}{spaces}{star}")
client.run(process.env.BOT_KEY)
