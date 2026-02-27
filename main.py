import os
import discord
from decouple import config
from discord.ext import commands

# Pega o token do arquivo .env
TOKEN = config("TOKEN_DISCORD")


class MyBot(commands.Bot):
    def __init__(self):
        # Inicializa o bot com prefixo, intents e config básica
        super().__init__(
            command_prefix="!",
            case_insensitive=True,
            intents=self.get_intents()
        )

    def get_intents(self) -> discord.Intents:
        # Define quais permissões de eventos o bot vai usar
        intents = discord.Intents.default()
        intents.message_content = True  # Permite ler mensagens
        intents.members = True  # Permite acessar membros (remova se não usar)
        return intents

    async def load_cogs_from(self, folder: str):
        # Percorre a pasta e subpastas procurando arquivos .py
        for root, _, files in os.walk(folder):
            for file in files:
                # Carrega apenas arquivos .py que não começam com "_"
                if file.endswith(".py") and not file.startswith("_"):

                    # Converte caminho do arquivo em módulo Python
                    path = os.path.join(root, file)
                    module = path.replace(os.sep, ".")[:-3]

                    try:
                        # Carrega a extensão (cog)
                        await self.load_extension(module)
                        print(f"✅ Cog carregada: {module}")
                    except Exception as e:
                        # Mostra erro sem quebrar o bot
                        print(f"❌ Erro ao carregar {module}: {e}")

    async def setup_hook(self):
        # Executa antes do bot ficar online
        # Aqui carregamos todas as cogs automaticamente
        for folder in ["commands", "events", "systems"]:
            if os.path.isdir(folder):
                await self.load_cogs_from(folder)


# Cria a instância do bot
client = MyBot()

# Inicia o bot com o token
client.run(TOKEN)