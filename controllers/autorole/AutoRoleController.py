import discord
from discord.ext import commands
from controllers.cargo.CargoController import CargoController

class AutoRoleController(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cargo_controller = CargoController()

    # Quando um membro entra
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):

        data = self.cargo_controller.load_data()
        guild_id = str(member.guild.id)

        if guild_id not in data:
            return

        cargo_id = data[guild_id].get("cargo_verificacao")

        if not cargo_id:
            return

        cargo = member.guild.get_role(cargo_id)

        if not cargo:
            return

        try:
            await member.add_roles(cargo)
        except discord.Forbidden:
            print(f"Sem permissão em {member.guild.name}")
        except Exception as e:
            print(f"Erro: {e}")


async def setup(bot):
    await bot.add_cog(AutoRoleController(bot))