from discord.ext import commands

class Event_Message(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        # Ignorar mensagens de bot
        if message.author.bot:
            return
        
        # 🚫 Ignorar comandos
        if message.content.startswith(("!", "?", ".", "/")):
            return

        # chama funções que estão no outro cog
        detox_cog = self.client.get_cog("System_Detox")
        translator_cog = self.client.get_cog("System_Translator")

        if detox_cog:
            await detox_cog.send_detox(message)
        
        if translator_cog:
            await translator_cog.send_trans(message)

async def setup(client):
    await client.add_cog(Event_Message(client))