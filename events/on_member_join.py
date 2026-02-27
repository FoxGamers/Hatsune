from discord.ext import commands

class Event_MemberJoin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):

        autorole_cog = self.client.get_cog("System_AutoRole")

        if autorole_cog:
            await autorole_cog.add_auto_role(member)

async def setup(client):
    await client.add_cog(Event_MemberJoin(client))