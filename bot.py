import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # Needed for message reading

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'🤖 Bot is ready! Logged in as {bot.user.name}')

@bot.command()
async def ping(ctx):
    await ctx.send('🏓 Pong!')

@bot.command()
async def say(ctx, *, message):
    await ctx.send(message)

@bot.command()
async def user(ctx, member: discord.Member = None):
    member = member or ctx.author
    await ctx.send(f'👤 Name: {member.name}\n🆔 ID: {member.id}')

bot.run(TOKEN)
