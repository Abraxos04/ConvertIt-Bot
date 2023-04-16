import discord
from discord.ext import commands

class HelpCommand(commands.Cog):
    def __init__(self,client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
         print("helpcommand.py is ready!")

    @commands.command()
    async def help (self, ctx):

        embed_message= discord.Embed(title="List of Commands", description="These are the commands that can be used for this bot and how to use them", color=discord.Color.blue())
        embed_message.add_field(name="ping",value="Returns the latency of the bot",inline=False)
        embed_message.add_field(name="support",value="Displays the list of supported virtual currency for the bot",inline=False)
        embed_message.add_field(name="convert",value="Used to convert between two currencies. Example: \n !c convert (amount) (currency 1) to (currency 2) ",inline=False)
        embed_message.add_field(name="add",value="Used to add new currency. Example: \n !c add (name of currency) (value of 1 unit of currency in EUR) ",inline=False)
        embed_message.add_field(name="remove",value="Used to remove a server currency. Example: \n !c remove (name of currency) ",inline=False)
        
        
        
        await ctx.send(embed=embed_message)   
 

async def setup(client):
    await client.add_cog(HelpCommand(client))