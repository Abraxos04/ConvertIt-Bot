import discord
from discord.ext import commands
import json

class add(commands.Cog):
    def __init__(self,client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
         print("add.py is ready!")
    #!c add "currency" "value in EUR"
    @commands.command()
    async def add (self, ctx, *args):
        error=0
        with open("cogs/curr.json","r") as f:
            curren = json.load(f)   
        curr=str(args[0])
        val=float(args[1])
        #print (curren)
        if(str(ctx.guild.id) not in curren):
            curren[str(ctx.guild.id)]={}       
        curren[str(ctx.guild.id)][curr.lower()]=val
        with open("cogs/curr.json","w") as f:
            json.dump(curren,f,indent=4)

        await ctx.send(f"{curr} has been added")         
        

async def setup(client):
    await client.add_cog(add(client))