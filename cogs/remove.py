import discord
from discord.ext import commands
import json

class remove(commands.Cog):
    def __init__(self,client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
         print("remove.py is ready!")
    #!c add "currency" "value in EUR"
    @commands.command()
    async def remove (self, ctx, *args):
        error=0
        with open("cogs/curr.json","r") as f:
            curren = json.load(f)   
        curr=str(args[0])
        
        #print (curren)
        if(str(ctx.guild.id) not in curren):
            curren[str(ctx.guild.id)]={}       
        del curren[str(ctx.guild.id)][curr.lower()]
        with open("cogs/curr.json","w") as f:
            json.dump(curren,f,indent=4)

        await ctx.send(f"{curr} has been removed")         
        

async def setup(client):
    await client.add_cog(remove(client))