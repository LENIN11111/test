import discord
from discord.ext import commands
client = commands.Bot(command_prefix = "=")

@client.command()
async def aa(ctx):
    await ctx.send("@everyone")


client.run("NTc3NDc3NzQ0OTM4NDUxMDA1.XRnaRA.jswCN_rejfFl34sez3PGAmidlC4")
