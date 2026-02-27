from discord.ext.commands import errors
from discord.ext import commands

class Event_Error(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, errors.MissingRequiredArgument):
            await ctx.send("Favor enviar todos os argumentos. Digite !help para ver os parâmetros de cada comando")
        
        elif isinstance(error, errors.CommandNotFound):
            await ctx.send("O comando não existe. Digite !help para ver os comandos")
        
        elif isinstance(error, errors.MissingPermissions):
            await ctx.send(f"Desculpe {ctx.author.name}, você não tem permissão para fazer isso!")
        
        elif isinstance(error, errors.CommandInvokeError):
            #await ctx.send(f"Desculpe {ctx.author.name}, Você excedeu sua cota atual. Verifique seu plano e detalhes de cobrança!")
            await ctx.send(f"Desculpe {ctx.author.name} \n{error}")
        
        else:
            raise error

async def setup(client):
    await client.add_cog(Event_Error(client))