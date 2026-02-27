from discord.ext import commands
from controllers.cargo.CargoController import CargoController
import discord

class System_AutoRole(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.cargo_controller = CargoController()

    async def add_auto_role(self, member: discord.Member):

        if not member.guild:
            return

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
            print(f"Erro ao adicionar cargo: {e}")

async def setup(client):
    await client.add_cog(System_AutoRole(client))