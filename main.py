"""Implementaremos las fuciones para crear el juego de la palabra del dia"""
import carga_palabras
import wordle_funciones

def main():
    """Establecemos la lista de palabras que vamos a tomar y las cargamos """
    ruta = "palabras_5.txt"
    palabras = carga_palabras.cargar_palabras_limpias(ruta)
    """Elegimos la palabra secreta"""
    palabra_secreta = wordle_funciones.elegir_palabra(palabras)
    
    
    print("¡Bienvenido al juego de la palabra del día!")
    print("Adivina la palabra de 5 letras.")
    """Establecemos los intenteos permitidos para divinar la palabra secreta"""
    intentos = 6
    while intentos > 0:
        intento = input("Introduce tu palabra: ")

        """Validamos que el intento sea de 5 letras y este en la lista de palabras"""
        if wordle_funciones.validar_intento(intento, palabras):
            """Comprobamos el intento, estableciendo el color de las letras en funcicon de unos parametros"""
            resultado = wordle_funciones.comprobar_intento(palabra_secreta, intento)
            """Mostramos los colores de las letras"""
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




