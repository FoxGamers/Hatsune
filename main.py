import os, discord
from decouple import config
from discord.ext import commands

TOKEN = config("TOKEN_DISCORD")

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", case_insensitive=True, intents = discord.Intents.all())

    async def setup_hook(self):
        for file in os.listdir("commands"):
            if file.endswith(".py"):
                cog = file[:-3]
                await self.load_extension(f"commands.{cog}")
        
        for file in os.listdir("events"):
            if file.endswith(".py"):
                cog = file[:-3]
                await self.load_extension(f"events.{cog}")

        for file in os.listdir("systems"):
            if file.endswith(".py"):
                cog = file[:-3]
                await self.load_extension(f"systems.{cog}")

client = MyBot()
client.run(TOKEN)