import random
import discord
from discord.ext import commands

config = {
    'token': 'MTA3NTc2MTU1Mjk2NTIzODg3NA.GtqGaY.48uOlDjQ2qz0o3Or-v1ua6Ady067VXq3GKcZwc',
    'prefix': '/',
}

bot = commands.Bot(command_prefix=config['prefix'])
@bot.event
async def on_message(ctx):
    if ctx.author != bot.user:
        await ctx.reply(ctx.content)
@bot.command()
async def kick(ctx, user : discord.User(), *arg, reason='Причина не указана'):
    await bot.kick(user)
    await ctx.send('Пользователь {user.name} был изгнан по причине "{reason}"')
@bot.event
async def on_message(ctx):
    if ctx.author != bot.user:
        await ctx.reply(ctx.content)
@bot.command()
async def kick(ctx, user : discord.User(), *arg, reason='Причина не указана'):
    await bot.kick(user)
    await ctx.send('Пользователь {user.name} был изгнан по причине "{reason}"')
@bot.event
async def on_message(ctx):
    if ctx.author != bot.user:
        await ctx.reply(ctx.content)
@bot.command()
async def kick(ctx, user : discord.User(), *arg, reason='Причина не указана'):
    await bot.kick(user)
    await ctx.send('Пользователь {user.name} был изгнан по причине "{reason}"')
@bot.event
async def on_message(ctx):
    if ctx.author != bot.user:
        await ctx.reply(ctx.content)
bot.run(config['token'])