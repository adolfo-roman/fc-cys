# Arreglo de Polibio para cifrar y descifrar

polibio = [
     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  # 0-9
     0, 65, 66, 67, 68, 69,  0,  0,  0,  0,  # 10-19
     0, 70, 71, 72, 73, 74,  0,  0,  0,  0,  # 20-29
     0, 75, 76, 77, 78, 79,  0,  0,  0,  0,  # 30-39
     0, 80, 81, 82, 83, 84,  0,  0,  0,  0,  # 40-49
     0, 85, 86, 87, 88, 89,  0,  0,  0,  0,  # 50-59
     0,  0,  0,  0,  0, 11, 12, 13, 14, 15,  # 60-69
    21, 22, 23, 24, 25, 31, 32, 33, 34, 35,  # 70-79
    41, 42, 43, 44, 45, 51, 52, 53, 54, 55   # 80-89
]

def limpiar_texto(texto):
    # Convertir a mayúsculas y quitar acentos
    texto = texto.upper()
    reemplazos = {'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'}
    for con_acento, sin_acento in reemplazos.items():
        texto = texto.replace(con_acento, sin_acento)
        
    # Filtrar solo caracteres válidos
    texto_limpio = ""
    for letra in texto:
        ascii_val = ord(letra)
        if ascii_val >= 65 and ascii_val <= 89:
            texto_limpio += letra
            
    return texto_limpio

def descifrar(mensaje):
    numeros = mensaje.split()
    mensaje_descifrado = ""
    
    for num in numeros:
        indice = int(num)
        ascii_val = polibio[indice]
        mensaje_descifrado += chr(ascii_val)
        
    return mensaje_descifrado

def cifrar(mensaje):
    mensaje_limpio = limpiar_texto(mensaje)
    
    mensaje_cifrado = ""
    for letra in mensaje_limpio:
        ascii_val = ord(letra)
        codigo = polibio[ascii_val]
        mensaje_cifrado += f"{codigo} "
            
    return mensaje_cifrado.strip()

def main_resolver(mensaje):
    print(f"\nMensaje: {mensaje}")
    if mensaje.replace(" ", "").isdigit():
        print("Descifrando...")
        resultado = descifrar(mensaje)
    else:
        print("Cifrando...")
        resultado = cifrar(mensaje)

    print(f"Resultado: {resultado}")

def main():
    print("--- Cifrado de Polibio ---")
    mensaje_cifrado = "15 32 45 24 15 33 " \
    "41 35 34 35 15 44 41 15 43 11 11 34 " \
    "11 14 24 15"
    
    mensaje_a_cifrar = "Si la felicidad tuviera una forma, " \
    "tendría forma de cristal, porque puede estar a tu " \
    "alrededor sin que la notes. Pero si cambias de perspectiva, " \
    "puede reflejar una luz capaz de iluminarlo todo."
    
    main_resolver(mensaje_cifrado)
    main_resolver(mensaje_a_cifrar)

if __name__ == "__main__":
    main()



'''
from typing import Dict, Union

# Definición del Cuadrado de Polibio (Grid 5x5)
# Los números representan la fila y columna (ej: 11 = A, 55 = Z)
GRID = {
    "A": "11", "B": "12", "C": "13", "D": "14", "E": "15",
    "F": "21", "G": "22", "H": "23", "I": "24", "J": "25",
    "K": "31", "L": "32", "M": "33", "N": "34", "O": "35",
    "P": "41", "Q": "42", "R": "43", "S": "44", "T": "45",
    "U": "51", "V": "52", "W": "53", "X": "54", "Y": "55" # Ajuste lógico
}

# Mapeo inverso para descifrado rápido
REV_GRID = {v: k for k, v in GRID.items()}

def limpiar_texto(texto: str) -> str:
    """Normaliza el texto eliminando acentos y caracteres no alfanuméricos."""
    tabla = str.maketrans("ÁÉÍÓÚ", "AEIOU")
    return "".join([c for c in texto.upper().translate(tabla) if c in GRID])

def cifrar(mensaje: str) -> str:
    """Convierte texto plano a coordenadas del cuadrado."""
    mensaje = limpiar_texto(mensaje)
    return " ".join([GRID[letra] for letra in mensaje])

def descifrar(codigo: str) -> str:
    """Convierte coordenadas a texto plano."""
    partes = codigo.split()
    return "".join([REV_GRID.get(p, "?") for p in partes])

def main():
    print("--- Cifrado de Polibio ---")
    entrada = input("Mensaje (Texto o Números): ").strip()
    
    if not entrada:
        return

    # Determinación automática del modo
    if entrada.replace(" ", "").isdigit():
        resultado = descifrar(entrada)
        print(f"\n[Resultado Descifrado]: {resultado}")
    else:
        resultado = cifrar(entrada)
        print(f"\n[Resultado Cifrado]: {resultado}")

if __name__ == "__main__":
    main()
'''