import discord
from discord.ext import commands
from controllers.cargo.CargoController import CargoController

class ServerController(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cargo_controller = CargoController()

    # Quando o bot entra em um servidor
    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):

        data = self.cargo_controller.load_data()
        guild_id = str(guild.id)

        if guild_id not in data:
            data[guild_id] = {
                "cargo_verificacao": None
            }
            self.cargo_controller.save_data(data)


async def setup(bot):
    await bot.add_cog(ServerController(bot))