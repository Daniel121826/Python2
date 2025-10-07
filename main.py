"""Implementaremos las fuciones para crear el juego de la palabra del dia"""
import carga_palabras
import wordle_funciones

def main():
    ruta = "palabras_5.txt"
    palabras = carga_palabras.cargar_palabras_limpias(ruta)
    palabra_secreta = wordle_funciones.elegir_palabra(palabras)
    
    print("¡Bienvenido al juego de la palabra del día!")
    print("Adivina la palabra de 5 letras.")
    
    intentos = 6
    while intentos > 0:
        intento = input("Introduce tu palabra: ")
        
        if wordle_funciones.validar_intento(intento, palabras):
            resultado = wordle_funciones.comprobar_intento(palabra_secreta, intento)
            wordle_funciones.mostrar_feedback(intento, resultado)

            if resultado == "¡Felicidades! Has adivinado la palabra.":
                break
        else:
            print("Palabra no válida. Asegúrate de que tiene 5 letras y está en la lista.")
        
        intentos -= 1
        print(f"Te quedan {intentos} intentos.")
    
    if intentos == 0:
        print(f"Lo siento, la palabra del día era: {palabra_secreta}")

if __name__ == "__main__":
    main()




