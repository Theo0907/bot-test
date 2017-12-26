import discord
from discord.ext import commands
import json
    #Paramètres

with open('config.json') as json_data_file:
    parameter = json.load(json_data_file)

deletion_minimal = -2       #quantité de votes totale nécessaire     
                            #pour supprimer un post.
                            #Prends en compte le nombre de votes 
                            #pour le conserver et pour le supprimer.
delet_symbole = "🗑"   #Réaction permettant la suppression du post.
cons_symbole = "♻"    #Réaction permettant la conservation du post.

authorized_to_start_deletion = ["True","156484695083843585","177393521051959306","170863227993849857"]#si premier terme = "True", fonctionnel.
grade_authorized_to_start_deletion = ["False"]


blocked_from_deleted = ["False","156484695083843585","384104235375001632"]#si premier terme = "True", fonctionnel.
grade_blocked_from_deleted = ["False"]


reactDict = {}
messageDict = {}




def authorized_verif(id):
    if authorized_to_start_deletion[0] == "True":
        if id in authorized_to_start_deletion[:]:
            return True
    if grade_authorized_to_start_deletion[0] == "True":
        if id in grade_authorized_to_start_deletion[:]:
            return True
    return False

def anti_delete(id):
    if blocked_from_deleted[0] == "True":
        if str(id) in blocked_from_deleted[:]:
            return False
    if grade_blocked_from_deleted[0] == "True":
        if str(id) in grade_blocked_from_deleted[:]:
            return False
    return True


async def first_reaction(self , reaction , user):
    if authorized_verif(user.id):
        print("creation")
        if reaction.emoji == delet_symbole:
            reactDict[reaction.message.id]=-1
        elif reaction.emoji == cons_symbole:
            reactDict[reaction.message.id]=1
        date,heure = timeCorrect(reaction.message.timestamp)
        
        
        message = str(reaction.message.author.mention)+" a recut un vote pour la suppression ou la conservation de son message du "+str(date)+" à "+str(heure)+".Si vous souhaitez voir son message supprimé, votez "+delet_symbole+". Si vous pensez que son message est correct, votez "+str(cons_symbole)+"."
        
        m = await self.bot.send_message(reaction.message.channel,message)
        messageDict[reaction.message.id]=m
        await self.bot.add_reaction(reaction.message,cons_symbole)
        await self.bot.add_reaction(reaction.message,delet_symbole)

async def delete(self , reaction , user):
    await self.bot.delete_message(reaction.message)
    await self.bot.delete_message(messageDict[reaction.message.id])


def timeCorrect(temps):
    date = ""
    heure = [0]*26
    
    listTemps = list(str(temps))
    for i in range(len(str(listTemps))):
        
        if listTemps[i] == " ":
            x = i
            break
        else:
            date += listTemps[i]
    del listTemps[:x+1]
    
    
    for i in range(len(str(listTemps))):
        if listTemps[i] == ".":
            break
        else:
            print(i)
            heure[i] = str(listTemps[i])
    del heure[i:]
    if heure[1] == 4:
        if heure[0] == 2:
            heure[0] = 0
            heure[1] = 0
    elif heure[1] == 9:
        heure[1] = 0
        heure[0] += 1
    else:
        heure[1] = str(int(heure[1])+1)

    h = str(heure[0])+str(heure[1])+" heures "+str(heure[3])+str(heure[4])+" minutes et "+str(heure[6])+str(heure[7])+" secondes"
    
    
    
    
    return date,h


class Ben:
    def __init__(self,bot):
        self.bot = bot
        f = open("log_test.txt","a")    #Montres le début de l'enregistrement dans les logs.
        f.write("\n\nDébut de l'enregistrement des réactions.\n\n\n")
        f.close
    
    
    
    @commands.group(pass_context = True)
    async def autoriser(self,ctx):
        if ctx.invoked_subcommand is None:
            await self.bot.say("Pas de commande,annulation")
    
    @autoriser.command(name="user",pass_context = True)
    async def autoriser_user(self,ctx,name):
        try:
            f = open("config.txt","r")
            r = f.read()
            print(r)
            f.close
        except:
            r = ""
        if r == "":
            g = open("config.txt","w")
            g.write('Fichier de config.\n\n\nPersonnes autorisées à démarer la fonction de suppression(la première valeur doit être True pour activer la whitelist ou False por la désactiver.\nauthorized_to_start_deletion = ["True"]\n\nGroupes qui sont autorisés à démarer la fonction de suppression(la première valeur doit être True pour activer la whitelist ou False por la désactiver.\ngrade_authorized_to_start_deletion = ["False"]\n\n')
            g.close
        print("test")
        
        
        
    
    
    
    
    async def on_reaction_remove(self,reaction,user):#Récupères la réaction
        print("-"+str(reaction.emoji))  #si on retire une réaction.
        print(reaction.count)
        print(user.name)
        print(reaction.message.id)
        if str(reaction.emoji) == cons_symbole:  #Vérifie si le caractère
            reactDict[reaction.message.id]-=1  #corresponds au symbole
        elif str(reaction.emoji) == delet_symbole:   #de suppression 
            reactDict[reaction.message.id]+=1  
                                                 #ou au symbole de conservation.
        print("num = "+str(reactDict[reaction.message.id]))                                         
        if reactDict[reaction.message.id]==deletion_minimal:    
            await delete(self , reaction , user)                  #si le 
                                                                #nombre est
                                                                #suppérieur,
                                                                #suppression.

        
    
    
    #def auto_deletion(self,Message):
    #    await self.bot.delete_message(Message)
    #    print(Message.content)

    

    async def on_reaction_add(self, reaction, user): #Récupères la réaction
        print("+"+str(reaction.emoji))      #si on ajoute une réaction.
        print(reaction.count)
        print(user.name)
        print(reaction.message.id)
        if anti_delete(reaction.message.author.id)== True:
            print("message autorise")
            if str(reaction.emoji) <= cons_symbole:  
                if reactDict.get(reaction.message.id)!=None:
                    reactDict[reaction.message.id]+=1
                    print("message present")
                else:
                    await first_reaction(self,reaction,user)
                
            
            
            if str(reaction.emoji) == delet_symbole:
                if reactDict.get(reaction.message.id)!=None:
                    reactDict[reaction.message.id]-=1
                    print("message present")
                else:
                    await first_reaction(self,reaction,user)
                
            
            
            if reactDict.get(reaction.message.id) != None :
                if reactDict[reaction.message.id]<=deletion_minimal:
                    await delete(self , reaction , user)
                else:
                    print(reactDict[reaction.message.id])
            
            print("tzdsqdzqs"+str(reactDict[reaction.message.id]))

def setup(bot):
    bot.add_cog(Ben(bot))