import discord
from discord.ext import commands
import threading
from flask import Flask
import os

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

# Flask setup
app = Flask(__name__)

@app.route('/health')
def health():
    return "OK", 200

@app.route('/')
def welcome():
    return """
    <html>
        <head><title>My Bot</title></head>
        <body>
            <h1>🤖 My Discord Bot is Running!</h1>
            <p>Health: <a href="/health">/health</a></p>
        </body>
    </html>
    """

def run_flask():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

# Start Flask in a thread before running bot
if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    bot.run(TOKEN)
