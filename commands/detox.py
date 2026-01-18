import os
from discord.ext import commands

class Detox(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.detox_file = "commands/files/detox.txt"
        if not os.path.exists(self.detox_file):
            open(self.detox_file, "w").close()

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(name="Detox", help="Insira uma palavra ofensiva na blacklist. (Requer argumento)")
    async def send_detox(self, ctx, message):
        if not message:
            await ctx.send("Por favor, insira uma palavra para ser adicionada à blacklist.")
            return
        with open(self.detox_file, "r") as arquivo:
            if message.lower() in arquivo.read().lower():
                await ctx.send("Essa palavra já está na blacklist!")
                return
        with open(self.detox_file, "a") as arquivo:
            arquivo.write(message.lower() + "\n")
        await ctx.send("Palavra adicionada à blacklist!")

async def setup(client):
    await client.add_cog(Detox(client))
