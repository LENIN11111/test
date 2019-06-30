import discord
from discord.ext import commands
client = commands.Bot(command_prefix = "=")

@client.command()
async def aa(ctx):
    await ctx.send("@everyone")


client.run("NTcyODUwMzM1NjM5NTM1NjI2.XRj6vg.bD7QPpy7K-6cTCT-a9zL6Smtys8")