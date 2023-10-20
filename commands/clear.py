from discord.ext import commands
from typing import Optional

class Clear(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(name="Clear", help="Este comando irá limpar as msgs (Não requer argumento)")
    @commands.has_permissions(manage_roles=True)
    async def send_clear(self, ctx, amount: Optional[int] = None):
        await ctx.channel.purge(limit=amount)

async def setup(client):
    await client.add_cog(Clear(client))