from googletrans import Translator
from discord.ext import commands

class Trans(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(name="En", help="Tradução para inglês. (Requer argumento)")
    async def en_trans(self, ctx, message):
        translator = Translator()
        tr = translator.translate(message, dest="en")
        await ctx.send(f"Inglês: {tr.text.upper()}")
    
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(name="Pt", help="Tradução para português. (Requer argumento)")
    async def pt_trans(self, ctx, message):
        translator = Translator()
        tr = translator.translate(message, dest="pt")
        await ctx.send(f"Português: {tr.text.upper()}")

async def setup(client):
    await client.add_cog(Trans(client))