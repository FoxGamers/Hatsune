from discord.ext import commands
from controllers.cargo.CargoController import CargoController
import discord

class System_Server(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.cargo_controller = CargoController()

    async def register_guild(self, guild: discord.Guild):

        if not guild:
            return

        data = self.cargo_controller.load_data()
        guild_id = str(guild.id)

        # Se o servidor ainda não estiver registrado
        if guild_id not in data:
            data[guild_id] = {
                "cargo_verificacao": None
            }

            self.cargo_controller.save_data(data)

            print(f"Servidor registrado: {guild.name}")

async def setup(client):
    await client.add_cog(System_Server(client))