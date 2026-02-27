from discord.ext import commands
from controllers.cargo.CargoController import CargoController

class Command_AddCargo(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.cargo_controller = CargoController()
    
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(name="addcargo", help="Configura um cargo específico pelo ID (Apenas dono do servidor)")
    async def send_addcargo(self, ctx, cargo_id: int):

        if cargo_id is None:
            await ctx.send("❌ Você precisa informar o ID do cargo.")
            return

        # Apenas dono do servidor
        if ctx.author.id != ctx.guild.owner_id:
            await ctx.send("❌ Apenas o dono do servidor pode usar este comando.")
            return

        cargo = ctx.guild.get_role(cargo_id)

        if not cargo:
            await ctx.send("❌ Cargo não encontrado neste servidor.")
            return

        self.cargo_controller.set_cargo(ctx.guild.id, cargo_id)

        await ctx.send(f"✅ Cargo {cargo.name} configurado com sucesso.")

async def setup(client):
    await client.add_cog(Command_AddCargo(client))