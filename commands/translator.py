from deep_translator import GoogleTranslator
from discord.ext import commands

class Trans(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(name="En", help="Tradução para inglês. (Requer argumento)")
    async def en_trans(self, ctx, *, message:str):
        translator = GoogleTranslator(source='auto', target='en')
        tr = translator.translate(message)
        await ctx.send(tr)
    
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(name="Pt", help="Tradução para português. (Requer argumento)")
    async def pt_trans(self, ctx, *, message:str):
        translator = GoogleTranslator(source='auto', target='pt')
        tr = translator.translate(message)
        await ctx.send(tr)

async def setup(client):
    await client.add_cog(Trans(client))