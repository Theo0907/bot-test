import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
import logging
import os

logging.basicConfig(level=logging.INFO)

numMenu = 0

bot = commands.Bot(description=os.getenv("BOTDESC"), command_prefix=os.getenv("COMMAND"))




@bot.event
async def on_ready():
    bot.load_extension("bot_ext")
    bot.load_extension("Music")
    print("I'm ready!")

@bot.command(pass_context = True)
async def load(ctx,ext):
    """: Charge une extension"""
    bot.load_extension(ext)
    print("extention "+str(ext)+" loaded")
    await bot.say("extension "+str(ext)+" loaded")

@bot.command()
async def close():
    """Permet d'arreter le bot."""
    await bot.say("Arret du bot")
    await bot.logout()
    await bot.close()


@bot.command(pass_context = True)
async def unload(ctx,ext):
    """: Décharge une extension"""
    bot.unload_extension(ext)
    print("extention "+str(ext)+" unloaded")
    await bot.say("extension "+str(ext)+" unloaded")

@bot.command(pass_context = True)
async def reload(ctx,ext):
    """: Recharge une extension avec ses modifications"""
    bot.unload_extension(ext)
    bot.load_extension(ext)
    print("extension "+str(ext)+" updated")
    await bot.say("extension "+str(ext)+" updated")
    


bot.run(os.getenv("TOKEN"))
