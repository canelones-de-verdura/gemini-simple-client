import google.generativeai as gemini
import os
from secret import apikey


def configure_gemini() -> object:
    gemini.configure(api_key=apikey.API_KEY)
    bot = gemini.GenerativeModel("gemini-1.5-flash")
    return bot


def chat(bot: object) -> None:
    bot = gemini.GenerativeModel("gemini-1.5-flash")
    chat = bot.start_chat()

    while True:
        promt = input(" >>> ")

        if promt == "/terminar":
            break

        res = chat.send_message(
            content=promt,
            stream=True,
            generation_config=gemini.types.GenerationConfig(
                temperature=2.0,  # Controla la "creatividad" de la respuesta. 2 es el máximo.
            ),
        )

        print("\n\033[1mGemini ✨:\033[0m")
        for cacho_respuesta in res:
            print(cacho_respuesta.text, end="")

        print()


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    chat(bot=configure_gemini())
