import discord
from discord import app_commands
from discord.ext import commands
import json

class add(commands.Cog):
    def __init__(self,client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
         print("add.py is ready!")
    #!c add "currency" "value in EUR"   

    @commands.hybrid_command(description="Adds a custom currency for the server")   
    async def add (self, ctx, name, value):
        
        error=0
        with open("cogs/curr.json","r") as f:
            curren = json.load(f)   
        curr=str(name)
        val=float(value)
        embed_message= discord.Embed(title=f"{curr} currency added.", description=f"Value = {val} EUR", color=discord.Color.dark_green())
        #print (curren)
        if(str(ctx.guild.id) not in curren):
            curren[str(ctx.guild.id)]={}       
        curren[str(ctx.guild.id)][curr.lower()]=val
        with open("cogs/curr.json","w") as f:
            json.dump(curren,f,indent=4)

        await ctx.send(embed=embed_message)         
        

async def setup(client):
    await client.add_cog(add(client))