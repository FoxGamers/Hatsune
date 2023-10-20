import os, discord
from decouple import config  
from discord.ext import commands

TOKEN = config("TOKEN")

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", case_insensitive=True, intents = discord.Intents.all())

    async def setup_hook(self):
        await self.load_extension("manager")

        for file in os.listdir("commands"):
            if file.endswith(".py"):
                cog = file[:-3]
                await self.load_extension(f"commands.{cog}")

client = MyBot()
client.run(TOKEN)
