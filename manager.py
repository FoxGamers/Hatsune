import discord
from discord.ext.commands import errors
from discord.ext import commands

class Manager(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.client.user.name} is online!")
        await self.client.change_presence(activity=discord.Game(name="!Ievan Polkka"))

    @commands.Cog.listener()
    async def on_message(self, message):
        arq = "commands/files/detox.txt"

        with open(arq) as file:
            lines = sorted(set(line.rstrip().lower() for line in file))

        with open(arq, 'w') as file:
            file.writelines(line + '\n' for line in lines)

        for line in lines:
            if message.author == self.client.user:
                return
            
            if line in message.content.lower():
                await message.delete()
                await message.channel.send(f"Por favor, {message.author.name}, não ofenda os demais usuários!")
        file.close()
    
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
    await client.add_cog(Manager(client))