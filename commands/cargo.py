import discord
from discord.ext import commands

class Cargo(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name="Cargo", help="Envia uma foto no privado. (Não requer argumento)")
    async def get_random_cargo(self, ctx):
        width = 1920
        height = 1080
        url_image = f"https://picsum.photos/{width}/{height}"
        exe = f"Caso sejá dispositivo móvel segure em cima essa msg!"
        
        embed_image = discord.Embed(
            title = "Como receber o cargo!",
            description = "Para receber o cargo siga os exemplos abaixo.",
            color = 0x00FFFF
        )

        embed_image.set_author(name=self.client.user.name, icon_url=self.client.user.avatar)
        embed_image.set_footer(text=(f"Criado por {self.client.user.name}"), icon_url=self.client.user.avatar)
        
        embed_image.add_field(name="Receber cargo", value="Usando a reação nessa msg!")
        embed_image.add_field(name="EMOJI", value="👍")
        
        embed_image.add_field(name="Exemplo", value=exe, inline=False)

        embed_image.set_image(url = url_image)
        
        await ctx.send(embed = embed_image)

async def setup(client):
    await client.add_cog(Cargo(client))