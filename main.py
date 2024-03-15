import discord
import random
from discord.ext import commands
import requests
from model import get_class

import os
print(os.listdir('images'))
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)



@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command('reward')
async def reward(ctx):
  await ctx.send("ТЫ ПОЛУЧИЛ НАГРАДУ \n 5000 Экокоинов")


@bot.command('check')
async def check(ctx):
    if ctx.message.attachments:
         for attachment in ctx.message.attachments:
             file_name = attachment.filename
             file_url = attachment.url
             await attachment.save(f'Мы сохранили картинку: {file_name}')
             await ctx.send(get_class(model_path="keras_model.h5", labels_path="labels.txt", image_path=f"images/{file_name}"))
    else:
        await ctx.send(' вы забыли картинку')
    


bot.run("TOKEN")    
