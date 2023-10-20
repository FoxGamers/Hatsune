from discord.ext import commands

listas = [{"title": "Spotify", "link": "https://open.spotify.com/playlist/0auScDhnLNk9QbLZc3Fw1p?si=7283fbaee73d4079"},
          {"title": "YouTube", "link": "https://www.youtube.com/"}]

class Playlist(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(name="playlist", help="Envia uma lista de reprodução. (Não requer argumento)")
    async def playlist(self, ctx):
        for lista in listas:
            await ctx.send(lista["title"])

    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(name="play", help="Envia os links das listas de reprodução. (Argumentos em !playlist)")
    async def play(self, ctx, message=None):
        if message is not None:
            message = message.lower()
            for lista in listas:
                if message == lista["title"].lower():
                    await ctx.send(lista["link"])
                    return
        await ctx.send("Lista de reprodução não encontrada.")

async def setup(client):
    await client.add_cog(Playlist(client))
