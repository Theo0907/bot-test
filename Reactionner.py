import discord
from discord.ext import commands

cons_symbole = "🦄"
licorne = ["licorne","Licorne"]

def is_licorne(msg):
    for i in range(len(licorne)):
        if msg == cons_symbole[i]:
            return True
    return False


class Reactionner:
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        #print(message.content[len('licorne'):])


def setup(bot):
    bot.add_cog(Reactionner(bot))