import discord
from discord.ext import commands
from currency_converter import CurrencyConverter
c = CurrencyConverter()
import sys
import json
sys.path.insert(1, 'D:\COPS Week\ConvertIt')
import Currency


class convert(commands.Cog):
    def __init__(self,client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
         print("convert.py is ready!")

    @commands.command()
    async def convert (self, ctx, *args):
        amount= float(args[0])
        curr1=args[1]
        curr2=args[3]
        serv=str(ctx.guild.id)
        with open("cogs/curr.json","r") as f:
            curren = json.load(f) 
        try:
            con1=float(c.convert(1,curr1.upper(),"EUR"))
        except:
            try:
               con1=Currency.value[curr1.lower()]
            except:
                try:
                    con1=float(curren[serv][curr1.lower()])
                except:
                    con1=-1
        try:
            con2=float(c.convert(1,curr2.upper(),"EUR"))
        except:
            try:
               con2=Currency.value[curr2.lower()]
            except:
                try:
                    con2=float(curren[serv][curr2.lower()])
                except:
                    con2=-1

        out=amount*((1/con2)*con1)
        if(round(out, 5)!=0.0):
            out=round(out, 5)
        if(con1==-1):
            embed_message= discord.Embed(title="Error", description=f"{curr1} Currency does not exist", color=discord.Color.red())
            await ctx.send(embed=embed_message)
        elif(con2==-1):
            embed_message= discord.Embed(title="Error", description=f"{curr2} Currency does not exist", color=discord.Color.red())
            await ctx.send(embed=embed_message)
        else:
            embed_message= discord.Embed(title="Conversion", description=f"{amount} {curr1} = {out} {curr2}", color=discord.Color.green())
            embed_message.set_footer(text=f"Requested by @{ctx.author}", icon_url=ctx.author.avatar)
            await ctx.send(embed=embed_message)

async def setup(client):
    await client.add_cog(convert(client))