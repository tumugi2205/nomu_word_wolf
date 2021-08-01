import os
import discord
import json
import random
import codecs
from discord.ext import commands

token = os.environ['DISCORD_BOT_TOKEN']
DEBUG=""


client = discord.Client()
bot = commands.Bot(command_prefix='$')

wolf = []
answer = []

@client.event
async def on_message(message: discord.Message):
    # メッセージの送信者がbotだった場合は無視する
    if message.author.bot:
        return

    if message.content == f"!wolf{DEBUG}":
        members = message.author.voice.channel.members
        with codecs.open("data/data.json", "r", 'utf-8') as f:
            data = json.load(f)
        theme = data[random.randint(0, len(data))]
        if len(wolf): wolf.pop(0)
        if len(answer): answer.pop(0)
        A = random.randint(0, 1)
        B = 0 if A else 1
        W = random.randint(0, len(members))
        answer.append(theme[B])
        for i, member in enumerate(members):
            if i == W:
                embed = discord.Embed(title="お題", description=f'{theme[A]}', color=0x4169e1)
                wolf.append(member.name)
            else:
                embed = discord.Embed(title="お題", description=f'{theme[B]}', color=0x4169e1)
            await member.send(embed=embed)
    elif message.content.startswith(f"!ans{DEBUG}"):
        if len(message.content.split(" "))[-1] == "-t":
            embed = discord.Embed(title="お題は…", description=f'{answer[0]}でした！', color=0x4169e1)
            await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(title="wolfは…", description=f'{wolf[0]}さんでした！', color=0x4169e1)
            await message.channel.send(embed=embed)

client.run(token)