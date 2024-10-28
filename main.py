import google.generativeai as gemini
import os
import ast
from secret import apikey

clear = "cls" if os.name == "nt" else "clear"


def main_menu() -> str:
    opts = (
        "Seleccionar opción:\n"
        "   1. Generar respuesta a partir de promt\n"
        "   2. Buscar palabra en promts guardadas\n"
        "   3. Ver las palabras que más aparecen en respuestas guardadas\n"
        "   4. Ver todas las promts guardadas y sus respuestas\n"
        "   5. Salir\n"
        " >>> "
    )

    return input(opts)


def save_exchange(convos: list) -> None:
    with open("history.txt", "a") as file:
        for dicc in convos:
            file.write(f"{str(dicc)}\n")


def load_history(hist) -> None:
    with open("history.txt", "r") as file:
        for line in file:
            hist.append(ast.literal_eval(line))


def print_history(previous_history: list) -> None:
    for dicc in previous_history:
        print(dicc, "\n")


def search(previous_history: list) -> None:
    usr_input = input("Buscar\n" " >>> ")

    for convo in previous_history:
        if usr_input in convo["user"]:
            print("\n", convo)


def histograma(previous_history: list) -> None:
    histogram = {}

    for convo in previous_history:
        for palabra in convo["user"].split(" "):
            histogram[palabra] = histogram.get(palabra, 0) + 1
        for palabra in convo["gemini"].split(" "):
            histogram[palabra] = histogram.get(palabra, 0) + 1

    for clave in histogram:
        if clave != " " and clave != "\n" and clave != "":
            print(f"{clave} : ", "#" * histogram[clave])


def configure_gemini() -> object:
    gemini.configure(api_key=apikey.API_KEY)
    bot = gemini.GenerativeModel("gemini-1.5-flash")
    return bot


def chat(bot: object, current_history: list, previous_history: list) -> None:
    os.system(clear)
    while True:
        promt = input(" >>> ")

        if promt == "/exit":
            save = input("Guardar? S/n ")
            if save.lower() == "s":
                save_exchange(current_history)
                previous_history.clear()
                load_history(previous_history)
            break

        res = bot.generate_content(
            contents=promt,
            stream=True,
            generation_config=gemini.types.GenerationConfig(
                candidate_count=1,
                temperature=2.0,  # Controla la "creatividad" de la respuesta. 2 es el máximo.
            ),
        )

        print("\n\033[1mGemini ✨:\033[0m")
        for cacho_respuesta in res:
            print(cacho_respuesta.text, end="")

        print()

        current_history.append({"user": promt, "gemini": res.text})


if __name__ == "__main__":
    current_history = []
    previous_history = []
    load_history(previous_history)

    while True:
        os.system(clear)
        match main_menu():
            case "1":
                chat(configure_gemini(), current_history, previous_history)
            case "2":
                os.system(clear)
                search(previous_history)
                pause = input("\nPresiona una tecla para volver al menu...")
            case "3":
                os.system(clear)
                histograma(previous_history)
                pause = input("\nPresiona una tecla para volver al menu...")
            case "4":
                os.system(clear)
                print_history(previous_history)
                pause = input("\nPresiona una tecla para volver al menu...")
            case "5":
                break
            case _:
                print("Opción inválida")
