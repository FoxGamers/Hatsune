from deep_translator import GoogleTranslator

# Traduzir do português para o inglês
try:
    texto = "Olá, como você está?"
    traducao = GoogleTranslator(source='auto', target='en').translate(texto)
    print(f"Texto original: {texto}")
    print(f"Tradução: {traducao}")
except Exception as e:
    print("Erro ao traduzir:", e)
