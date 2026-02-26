from discord.ext import commands

class Event_Reaction(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.emoji == "👍":
            role = user.guild.get_role(1118292839315542066)
            await user.add_roles(role)

async def setup(client):
    await client.add_cog(Event_Reaction(client))