# :3
import os
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands 
import config
description="""A simple management bot to fit all your needs.

for any quetions reach out to me @weird0cats"""
intents=nextcord.Intents.default()
intents.members=True
intents.message_content

bot=commands.Bot(command_prefix="|", description=description, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}, ID:{bot.user.id}")

@bot.slash_command(description="Test the bot")
async def test(interaction:nextcord.Interaction):
    await interaction.send("test successful", ephemeral=True)

@bot.slash_command(description='Get a list of commands')
async def help(interaction=nextcord.Interaction):
    embed="embed"
    interaction.send(embed)

bot.run(config.tok)
# Mr pipe? => |