

import logging, nextcord, os, config, jsonfs
from nextcord import Interaction, SlashOption
from nextcord.ext import commands, application_checks

#Logs 
logger=logging.getLogger('nextcord')
logger.setLevel(logging.DEBUG)
handler=logging.FileHandler(
    filename="NextCord.log",
    encoding="utf-8",
    mode="w"
)
logging.basicConfig(
    filename="bot.log",
    encoding="utf-8",
    filemode="w",
    format="{asctime} - [{levelname}]: {message}",
    style="{",
    datefmt="%Y/%m/%d - %H:%M"
)
logger.addHandler(handler)
# Discord bot configurations
description="""A simple management bot to fit all your needs.

for any quetions reach out to me @weird0cats"""

GUILD_ID = 1222304349326151793

intents=nextcord.Intents.default()
intents.members=True
intents.message_content=True

bot=commands.Bot(
    command_prefix="$",
    description=description,
    intents=intents
    )
# End of that

@bot.event
async def on_ready():
    print(f"""Logged in as {bot.user}, ID:{bot.user.id}
Powered by Nextcord {nextcord.__version__}""")

@bot.command()
async def test(ctx):
    await ctx.send("It works!")

#slash commands, to remain seperate from other commands, as they're simpler to use and I refuse to keep track of them. 
@bot.slash_command(description="Test the bot")
async def test(interaction:Interaction):
    await interaction.send("test successful", ephemeral=True)

@bot.slash_command(description='Get a list of commands')
async def helpme(interaction:Interaction):
    embed=nextcord.Embed(colour=0xdc143c,title='commands',description=f"""
    {bot.command_prefix}c - "colors" - prints a list of colors
    {bot.command_prefix}m -  - 
    """)
    await interaction.send(embed=embed,ephemeral=True)
#until I can fix standard commands

bot.run(config.tok)