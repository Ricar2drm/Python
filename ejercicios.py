#Crear una función que reciba una frase y cuente
# cuántas palabras tiene en total. Guarde todas las palabras en una lista.
# Pregunte al usuario por una palabra de la frase que quiera reemplazar
# y por la nueva palabra que desea poner en su lugar. Retorne la lista
# de palabras modificada y el número de palabras que tenía la frase antes del cambio.

frase = "Primera frase"
palabra = "Primera"
palabraNueva= "Segunda"
def contar_palabras(frase):
    palabras = frase.split()
    return len(palabras)

def cambiar_palabra(frase, palabra, palabraNueva):
    palabras = frase.split()
    try:
        indice = palabras.index(palabra)
        palabras[indice] = palabraNueva
        return " ".join(palabras)
    except ValueError:
        print("Palabra no encontrada")

print(cambiar_palabra(frase, palabra, palabraNueva))


#Crea una función que al pasar le una frase cuente el numero de vocales
# que tiene en total y que pregunte por que otra vocal quiere cambiar
# todas las vocales de la frase, que retorne la frase cambiada y el numero
# de vocales de la frase antes de cambiarlas.

cantidad = frase.lower().count('a') + frase.lower().count('e') + frase.lower().count('i') + frase.lower().count('o') + frase.lower().count('u')
print(cantidad)
vocalNueva = "i"


#hora


