import discord
from discord.ext import commands

class Event_Ready(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.client.user.name} is online!")
        await self.client.change_presence(activity=discord.Game(name="!Ievan Polkka"))

async def setup(client):
    await client.add_cog(Event_Ready(client))