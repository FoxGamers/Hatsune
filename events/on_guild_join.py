from discord.ext import commands

class Event_GuildJoin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):

        server_cog = self.client.get_cog("System_Server")

        if server_cog:
            await server_cog.register_guild(guild)

async def setup(client):
    await client.add_cog(Event_GuildJoin(client))