import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv
load_dotenv()

disc = os.getenv('DISCORD')
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='/', intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f"Server up as {client.user}")
    for guild in client.guilds:
        print(f'{guild.name} (ID: {guild.id})')

    await client.tree.sync()
    await client.change_presence(status=discord.Status.online)

@client.tree.command(name="pong")
async def pong(interaction: discord.Interaction):
    await interaction.response.send_message("ping!")

client.run(disc)