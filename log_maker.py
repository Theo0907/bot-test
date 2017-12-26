import discord
from discord.ext import commands

class log_Maker:
    def __init__(self,bot):
        self.bot = bot
        logger = open("log.txt","a")
        logger.write("Début de l'enregistrement")
        logger.close
    
    

    async def on_message(self, msg):
        logger = open("log.txt","a")
        print(msg.timestamp)
        logger.write(str(msg.timestamp)+"\n")
        print(msg.author)
        logger.write(str(msg.author)+"\n")
        print(str(msg.channel)+" sur "+str(msg.server))
        logger.write(str(msg.channel)+" sur "+str(msg.server)+"\n")
        print(msg.content)
        logger.write(str(msg.content)+"\n")
        logger.write("End of message\n\n\n")
        logger.close





def setup(bot):
    bot.add_cog(log_Maker(bot))
