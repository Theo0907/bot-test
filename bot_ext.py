import discord
from discord.ext import commands
numMenu = 0


def is_owner(ctx):
    if ctx.message.author.id == 156484695083843585:
        return True
    return False



def logger(ctx,type = 0):
    msg = ctx.message
    f = open("command_log.txt","a")
    if type == 1:
        f.write("Début de l'enregistrement")
    elif type == 2:
        f.write("Fin de l'enregistrement")
    else:
        print(msg.timestamp)
        f.write(str(msg.timestamp)+"\n")
        print(msg.author)
        f.write(str(msg.author)+"\n")
        print(str(msg.channel)+" sur "+str(msg.server))
        f.write("Salon"+str(msg.channel)+" sur "+str(msg.server)+"\n")
        print(msg.content)
        f.write(str(msg.content)+"\n")
        f.write("End of command\n\n\n")
    f.close


class Useless:
    def __init__(self,bot):
        self.bot = bot
        global loging
        loging = 1
        global loggingInactive
        logingInactive = 0
        
        
    
    
    
    
    
    
    
    #async def on_message(self, msg):
    #    print(msg.timestamp)
    #   print(msg.author)
    #    print(str(msg.channel)+" sur "+str(msg.server))
    #    print(msg.clean_content)
    #    print(msg.raw_mentions)
    #    print(msg.content)
    
    
    @commands.command(pass_context=True)
    async def menu(self,ctx,*,choix = "pas de choix"):
        """: Montre le menu du bot et permet de choisir un article
        """
        if loging == 1:
            logger(ctx)
        if choix == "pas de choix":
            say = "Menu:\nTruc: 3 bierres\nBidule: 3 vodkas"
            global numMenu
            numMenu+=1
            await self.bot.say(say + "\nVous etes la "+str(numMenu)+"èem personne a demander le menu")
        else:
            if choix == "Truc":
                await self.bot.say("Cela vous fera 3 bierres utilisateur "+str(ctx.message.author))
            elif choix == "Bidule":
                await self.bot.say("Cela vous fera 3 vodkas utilisateur "+str(ctx.message.author))
            else:
                await self.bot.say("Vous avez échoué à faire un choix existant.")
    

    @commands.command(pass_context=True)
    async def Bonjour(self,ctx):
        if loging == 1:
            logger(ctx)
        print(ctx.message.author.id)
        if ctx.message.author.id == "156484695083843585":
            await self.bot.say("Bonjour Maitre")
        else:    
            await self.bot.say("Bonjour!")
        
    @commands.command(pass_context=True)
    async def ID(self,ctx):
        if loging == 1:
            logger(ctx)
        print(ctx.message.author.id)
        await self.bot.say(ctx.message.author.id)
    
    @commands.command(pass_context=True)
    async def bonjour(self,ctx):
        if loging == 1:
            logger(ctx)
        print(ctx.message.author.id)
        if ctx.message.author.id == "156484695083843585":
            await self.bot.say("Bonjour Maitre")
        else:    
            await self.bot.say("Bonjour!")
    
    @commands.group(pass_context=True)
    async def role(self,ctx):
        """: Ne sert a rien pour le moment
        """
        if loging == 1:
            logger(ctx)
        if ctx.invoked_subcommand is None:
            await self.bot.say("pas de commande")
    
    
    @role.command(name="test", pass_context=True)
    async def role_test(self,ctx,name):
        await self.bot.say("ITS WORKING! "+str(ctx.message.author))
    
    @commands.group(pass_context=True)
    async def log(self,ctx):
        if loging == 1:
            logger(ctx)
        if ctx.invoked_subcommand is None:
            await self.bot.say("Commandes disponibles: start, stop")
    
    
    @log.command(pass_context=True,name='start')
    async def log_start(self,ctx,type="no"):
        if type == "all":
            self.bot.load_extension("log_maker")
            await self.bot.say("logs complet en cours d'enregistement")
        else:
            loging = 1
            logger(ctx,1)
            await self.bot.say("log en cours d'enregistrement")
            
        
        
    @log.command(pass_context=True,name='stop')
    async def log_stop(self,ctx,type = "no"):
        if type == "all":
            self.bot.unload_extension("log_maker")
            await self.bot.say("fin de l'enregistrement des logs complets")
        else:
            loging = 0
            logger(ctx,2)
            await self.bot.say("fin de l'enregistrement des logs")


def setup(bot):
    bot.add_cog(Useless(bot))