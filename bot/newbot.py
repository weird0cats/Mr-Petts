import logging, nextcord, os, cooldowns, config, jsonfs
from nextcord import Interaction, SlashOption
from nextcord.ext import commands, application_checks
from cooldowns import SlashBucket
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

#Pet commands
@bot.slash_command(description="Claim yourself a pet! doesn't work if there is an active pet.")
async def adopt(interaction:Interaction,name:str):
    try:
        jsonfs.create(f'{interaction.user.id}.jsonc',{"name":name,'love':0})
        await interaction.send(f"""Congratulations, {interaction.user.name}, you have adopted {name}!""",ephemeral=True)
    except FileExistsError:
        await interaction.send("You already have a pet!",ephemeral=True)

@bot.slash_command(description="Bond with your pet!")
@cooldowns.cooldown(1,15,bucket=cooldowns.SlashBucket.author)
async def play(interaction:Interaction):
    try:
        data=jsonfs.read(f'{interaction.user.id}.jsonc')
        data['love']+=1
        await interaction.send(f"You spent some time playing with {data['name']}.",ephemeral=True)
        jsonfs.write(f'{interaction.user.id}.jsonc', data)
    except FileNotFoundError:
        await interaction.send("You don't have a pet! you can adopt one with /adopt!",ephemeral=True)

@bot.slash_command(description="Abandon your pet :(")
async def abandon(interaction:Interaction):
    try:
        data=jsonfs.read(f'{interaction.user.id}.jsonc')
        jsonfs.delete(f'{interaction.user.id}.jsonc')
        await interaction.send(f"You've abandoned {data['name']}... :(",ephemeral=True)
    except FileNotFoundError:
        await interaction.send("You don't have a pet!",ephemeral=True)

#error handler goes here 
@play.error
async def play_error(interaction:Interaction, error):
    if isinstance(error, cooldowns.exceptions.CallableOnCooldown):
        try:
            await interaction.send(f"{jsonfs.read(f'{interaction.user.id}.jsonc')["name"]} is tired, wait a little bit!",ephemeral=True)
        except FileNotFoundError:
            await interaction.send(f"Why are you trying to play with a pet you don't have, {interaction.user.name}?",ephemeral=True)

bot.run(config.tok)