import nextcord, os, config
from nextcord.ext import commands, application_checks
description="""A simple management bot to fit all your needs.

for any quetions reach out to me @weird0cats"""
intents=nextcord.Intents.default()
intents.members=True
intents.message_content=True

bot=commands.Bot(command_prefix="|", description=description, intents=intents)

@bot.event
async def on_ready():
    print(f"""Logged in as {bot.user}, ID:{bot.user.id}
Wrapper version:{nextcord.__version__}""")

@bot.command()
async def color(ctx):
    embed=nextcord.Embed(title="test")
    await ctx.send("what")

#slash commands, to remain seperate from other commands, as they're simpler to use
@bot.slash_command(description="Test the bot")
async def test(interaction:nextcord.Interaction):
    await interaction.send("test successful", ephemeral=True)

@bot.slash_command(description='Get a list of commands')
async def help(interaction=nextcord.Interaction):
    embed=nextcord.Embed(colour=0xdc143c,title='commands',description=f"""
    {bot.command_prefix}color - prints a list of colors
    
    """)
    await interaction.send(embed=embed,ephemeral=True)

bot.run(config.tok)