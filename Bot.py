import discord
from discord.ext import commands
#from Token import *
from dotenv import load_dotenv
import os
import asyncio
import json

def configure():
    load_dotenv()
def get_server_prefix(client,message):
    with open("prefixes.json","r") as f:
        prefix = json.load(f)
    
    return prefix[str(message.guild.id)]

client = commands.Bot(command_prefix=get_server_prefix, intents=discord.Intents.all())

client.remove_command("help")

@client.event
async def on_guild_join(guild):
    with open("prefixes.json","r") as f:
        prefix = json.load(f)
    
    prefix[str(guild.id)]= "!c "

    with open("prefixes.json","w") as f:
       json.dump(prefix,f,indent=4)

@client.event
async def on_guild_remove(guild):
    with open("prefixes.json","r") as f:
        prefix = json.load(f)
    
    prefix.pop(str(guild.id))

    with open("prefixes.json","w") as f:
       json.dump(prefix,f,indent=4)

@client.hybrid_command(description="Set a new prefix for the bot in the server")
async def setprefix(ctx, newprefix):
    with open("prefixes.json","r") as f:
        prefix = json.load(f)
    
    prefix[str(ctx.guild.id)]= f"{newprefix} "

    with open("prefixes.json","w") as f:
       json.dump(prefix,f,indent=4)
    
    await ctx.send(f"Prefix changed")

@client.event
async def on_ready():
    await client.tree.sync()
    print("Success: Bot is connected to Discord.")

async def load():
    for filename in os.listdir("./cogs"):
        if(filename.endswith(".py")):
            await client.load_extension(f"cogs.{filename[:-3]}")
            print(f"{filename} is loaded")

async def main():
    configure()
    await load()
    await client.start(str(os.getenv('TOKEN')))


asyncio.run(main())