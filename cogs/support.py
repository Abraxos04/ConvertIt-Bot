import discord
from discord.ext import commands
import sys
import os
path = os.getcwd()
sys.path.insert(1, os.path.abspath(os.path.join(path, os.pardir)))
import Currency
import json
class support(commands.Cog):
    def __init__(self,client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
         print("support.py is ready!")

    @commands.command()
    async def support (self, ctx):
        embed_message= discord.Embed(title="List of Supported Currencies", description="You can add or remove currencies using the add or remove commands", color=discord.Color.random())
        
        supp=[]
        for i in range(len(Currency.value)):
            supp.append(list(Currency.value)[i])
        supp.sort()
        l=len(supp)
        serv=str(ctx.guild.id)
        with open("cogs/curr.json","r") as f:
            curren = json.load(f)   
        if(str(ctx.guild.id) not in curren):
            curren[str(ctx.guild.id)]={} 
        for key,value in curren[serv].items():
            supp.append(key)
        
        cnt=0
        for x in supp:
            if(cnt<l):
                embed_message.add_field(name=str(x),value="Gaming Currency",inline=False)
            else:
                embed_message.add_field(name=str(x),value="Custom Currency for Server",inline=False)
            cnt+=1

        
        await ctx.send(embed=embed_message)   
        


async def setup(client):
    await client.add_cog(support(client))