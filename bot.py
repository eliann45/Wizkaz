import discord
from discord.ext import commands
import os

TOKEN = os.environ.get("TOKEN")

if TOKEN is None:
    print("Falta el TOKEN en Environment Variables de Render")
    exit()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")

@bot.command()
async def hola(ctx):
    await ctx.send("Que lo que 😹")

bot.run(TOKEN)
