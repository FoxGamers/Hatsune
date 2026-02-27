# import discord
from controllers.translator.TranslatorController import TranslateView
from discord.ext import commands

class System_Translator(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def send_translator(self, message):
        if not message.guild:
            return

        view = TranslateView(message.content)

        # Comando sem embed!
        await message.channel.send(view=view)

        # Comando com embed!
        # embed = discord.Embed(
        #     description=message.content,
        #     color=0x2b2d31
        # )
        # embed.set_author(
        #     name=message.author.display_name,
        #     icon_url=message.author.display_avatar.url
        # )

        # await message.channel.send(embed=embed, view=view)

async def setup(client):
    await client.add_cog(System_Translator(client))