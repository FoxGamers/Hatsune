from discord.ext import commands

class Talks(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(name="Hello", help="Envia um Olá. (Não requer argumento)")
    async def send_hello(self, ctx):
        await ctx.send(f"Olá, {ctx.author.name}! :relaxed: ")
    
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(name="Cat", help="Agradece pelo elogio. (Não requer argumento)")
    async def send_cat(self, ctx):
        await ctx.send(f"Muito obrigada {ctx.author.name}! :heart_eyes: ")

async def setup(client):
    await client.add_cog(Talks(client))