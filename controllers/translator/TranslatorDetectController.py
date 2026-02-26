import discord
from deep_translator import GoogleTranslator, single_detection
import time


class TranslateView(discord.ui.View):
    def __init__(self, original_text):
        super().__init__(timeout=None)
        self.original_text = original_text
        self.translation_cache = {}
        self.cooldowns = {}
        self.COOLDOWN_TIME = 5

    def get_flag(self, language_code):
        flags = {
            "en": "🇺🇸",
            "fr": "🇫🇷",
            "pt": "🇧🇷",
            "es": "🇪🇸",
            "de": "🇩🇪",
            "it": "🇮🇹",
            "ja": "🇯🇵",
            "ko": "🇰🇷",
            "ru": "🇷🇺",
            "zh": "🇨🇳"
        }
        return flags.get(language_code, "🌍")

    @discord.ui.button(label="Traduzir", emoji="🌎", style=discord.ButtonStyle.secondary)
    async def translate_button(self, interaction: discord.Interaction, button: discord.ui.Button):

        user_id = interaction.user.id
        current_time = time.time()

        # 🔥 Cooldown
        if user_id in self.cooldowns:
            if current_time - self.cooldowns[user_id] < self.COOLDOWN_TIME:
                await interaction.response.send_message(
                    "⏳ Aguarde alguns segundos.",
                    ephemeral=True
                )
                return

        self.cooldowns[user_id] = current_time

        try:
            # 🌎 Idioma do usuário
            user_locale = str(interaction.locale)
            target_lang = user_locale.split("-")[0]

            # 🔎 Detectar idioma original
            detected_lang = single_detection(self.original_text, api_key=None)

            if detected_lang == target_lang:
                await interaction.response.send_message(
                    f"✔ A mensagem já está em {target_lang.upper()}",
                    ephemeral=True
                )
                return

            cache_key = (self.original_text, target_lang)

            # 📦 Cache
            if cache_key in self.translation_cache:
                translated_text = self.translation_cache[cache_key]
            else:
                translated_text = GoogleTranslator(
                    source=detected_lang,
                    target=target_lang
                ).translate(self.original_text)

                self.translation_cache[cache_key] = translated_text

            flag = self.get_flag(target_lang)

            # ✨ Embed formatada
            embed = discord.Embed(color=0x00ff99)

            embed.add_field(
                name="📝 Original",
                value=self.original_text,
                inline=False
            )

            embed.add_field(
                name=f"{flag} Tradução",
                value=translated_text,
                inline=False
            )

            embed.set_footer(
                text=f"Traduzido de {detected_lang.upper()} para {target_lang.upper()}"
            )

            await interaction.response.send_message(
                embed=embed,
                ephemeral=True
            )

        except Exception as e:
            print("Erro na tradução:", e)
            await interaction.response.send_message(
                "❌ Erro ao traduzir.",
                ephemeral=True
            )