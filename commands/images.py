import discord
from discord.ext import commands

class Image(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name="Image", help="Envia uma foto no privado. (Não requer argumento)")
    async def get_random_image(self, ctx):
        width = 1920
        height = 1080
        url_image = f"https://picsum.photos/{width}/{height}"
        
        embed_image = discord.Embed(
            title = "Resultado da busca de imagem",
            description = "PS: A busca é totalmente aleatória",
            color = 0x00FFFF
        )

        embed_image.set_author(name=self.client.user.name, icon_url=self.client.user.avatar)
        embed_image.set_footer(text=(f"Criado por {self.client.user.name}"), icon_url=self.client.user.avatar)
        
        embed_image.add_field(name="API", value="Usamos a API do https://picsum.photos")
        embed_image.add_field(name="Parâmetros", value=f"{width}/{height}")
        
        embed_image.add_field(name="Exemplo", value=url_image, inline=False)

        embed_image.set_image(url = url_image)
        
        await ctx.send(embed = embed_image)

async def setup(client):
    await client.add_cog(Image(client))