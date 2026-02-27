import os
from discord.ext import commands

class System_Detox(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def send_detox(self, message):
        # Pega a pasta raiz do projeto (HATSUNE)
        base_dir = os.path.dirname(os.path.dirname(__file__))
        
        # Monta o caminho corretamente
        arq = os.path.join(base_dir, "commands", "files", "detox.txt")

        with open(arq, encoding="utf-8") as file:
            lines = sorted(set(line.rstrip().lower() for line in file))

        for line in lines:
            if line in message.content.lower():
                await message.delete()
                await message.channel.send(f"Por favor, {message.author.name}, não ofenda os demais usuários!")
                return

async def setup(client):
    await client.add_cog(System_Detox(client))