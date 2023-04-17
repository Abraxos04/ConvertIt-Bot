import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self,client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
         print("Ping.py is ready!")

    @commands.hybrid_command(description="Prints the latency of the bot")
    async def ping (self, ctx):
        client_latency = round(self.client.latency * 1000)
        await ctx.send(f"Pong! {client_latency} ms.")   

async def setup(client):
    await client.add_cog(Ping(client))