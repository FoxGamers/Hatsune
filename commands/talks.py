import openai
from decouple import config
from discord.ext import commands

openai.api_key = config('TOKEN_CHAT_GPT')

class Talks(commands.Cog):
    def __init__(self, client):
        self.client = client

    def get_ai_response(self, user_message):
        message = [{'role': 'user', 'content': str(user_message)}]
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = message,
            max_tokens = 1024,
            temperature = 1,
        )
        return response.choices[0].message.content
    
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(name="Hello", help="Envia um Olá. (Não requer argumento)")
    async def send_hello(self, ctx):
        await ctx.send(f"Olá, {ctx.author.name}! :relaxed: ")
    
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(name="Cat", help="Agradece pelo elogio. (Não requer argumento)")
    async def send_cat(self, ctx):
        await ctx.send(f"Muito obrigada {ctx.author.name}! :heart_eyes: ")
    
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(name="PGT", help="Gera mensagem igual o ChatGPT. (Requer argumento)")
    async def send_gpt(self, ctx, *, message:str):
        gpt_message = self.get_ai_response(message)
        await ctx.send(gpt_message)

async def setup(client):
    await client.add_cog(Talks(client))