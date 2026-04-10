abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# A B C D E F G H I J K  L  M  N  Ñ  O  P  Q  R  S  T  U  V  W  X  Y  Z
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26

def limpiar_texto(texto):
    # Convertir a mayúsculas y quitar acentos
    texto = texto.upper()
    reemplazos = {'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'}
    for con_acento, sin_acento in reemplazos.items():
        texto = texto.replace(con_acento, sin_acento)
            
    return texto

def descifrar(mensaje, salto):
    
    mensaje = limpiar_texto(mensaje)
    
    mensaje_descifrado = ""
    
    for letra in mensaje:
        if letra not in abc:
            mensaje_descifrado += " "
            continue
        indice = abc.index(letra)
        if indice + salto >= len(abc):
            mensaje_descifrado += abc[(indice + salto) % len(abc)]
        else:
            mensaje_descifrado += abc[indice + salto]
    
    return mensaje_descifrado

def fuerza_bruta(mensaje):
    for salto in range(1, len(abc)):
        print(f"Salto {salto}: {descifrar(mensaje, salto)}")

def relacion(letra_mensaje, letra_asociada):
    indice_mensaje = abc.index(letra_mensaje.upper())
    indice_asociada = abc.index(letra_asociada.upper())
    if indice_mensaje < indice_asociada:
        salto = indice_asociada - indice_mensaje
    else:
        salto = len(abc) - indice_mensaje + indice_asociada
    return salto

def conocimiento_adicional(mensaje, letra_mensaje, letra_asociada):
    salto = relacion(letra_mensaje, letra_asociada)
    print(f"Salto calculado: {salto}")
    return descifrar(mensaje, salto)

def frecuencia_letras(mensaje):

    frecuencia = {letra: 0 for letra in abc}
    
    for letra in mensaje:
        if letra in frecuencia:
            frecuencia[letra] += 1
    
    frecuencia = sorted(frecuencia.items(), key=lambda item: item[1], reverse=True)
            
    return frecuencia[0][0]

def frecuencia(mensaje):
    mensaje = limpiar_texto(mensaje)
    letra_mas_frecuente = frecuencia_letras(mensaje)
    print(f"Letra más frecuente: {letra_mas_frecuente}")
    frecuencia_letras_esp = ['E', 'A', 'O']
    for letra in frecuencia_letras_esp:
        resultado = conocimiento_adicional(mensaje, letra_mas_frecuente, letra)
        print(f"Resultado con frecuencia de '{letra}': {resultado}")  

def main():

    print("Ejercicio 1: Fuerza Bruta")
    mensaje_fuerza_bruta = "Nc xkfc gu dgnnc"
    print(f"Mensaje a descifrar: {mensaje_fuerza_bruta}")
    fuerza_bruta(mensaje_fuerza_bruta)
    
    print("\nEjercicio 2: Conocimiento Adicional")
    mensaje_conocimiento_adicional = "Zo qgweidugotío sh jb hsqgsid"
    letra_mensaje = "d"
    letra_asociada = "o"
    print(f"Mensaje a descifrar: {mensaje_conocimiento_adicional}")
    print(f"Letra en el mensaje: {letra_mensaje}")
    print(f"Letra asociada: {letra_asociada}")
    resultado = conocimiento_adicional(mensaje_conocimiento_adicional, letra_mensaje, letra_asociada)
    print(f"Resultado con conocimiento adicional: {resultado}")

    print("\nEjercicio 3: Frecuencia de Letras")
    mensaje_frecuencia = "Jx qzd kfhnp mjwnw f ptx " \
    "ijqfx xnr ifwxj hzjryf xtgwj ytit hzfrit jwjx ñtajr"
    print(f"Mensaje a descifrar: {mensaje_frecuencia}")
    frecuencia(mensaje_frecuencia)
    
if __name__ == "__main__":
    main()

'''
import collections

ABC = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def limpiar_texto(texto: str) -> str:
    """Elimina acentos y convierte a mayúsculas."""
    tabla = str.maketrans("ÁÉÍÓÚ", "AEIOU")
    return texto.upper().translate(tabla)

def descifrar(mensaje: str, salto: int) -> str:
    """Aplica desplazamiento cíclico."""
    mensaje = limpiar_texto(mensaje)
    resultado = []
    
    for char in mensaje:
        if char in ABC:
            idx = (ABC.index(char) + salto) % len(ABC)
            resultado.append(ABC[idx])
        else:
            resultado.append(" ")
            
    return "".join(resultado)

def mostrar_seccion(titulo: str):
    """Formateador estético para la terminal."""
    print(f"\n{'='*10} {titulo} {'='*10}")

def fuerza_bruta(mensaje: str):
    for salto in range(1, len(ABC)):
        print(f"Salto {salto:02d}: {descifrar(mensaje, salto)}")

def calcular_salto(letra_mensaje: str, letra_asociada: str) -> int:
    """Calcula la distancia modular entre dos letras."""
    idx_m = ABC.index(letra_mensaje.upper())
    idx_a = ABC.index(letra_asociada.upper())
    return (idx_a - idx_m) % len(ABC)

def resolver_frecuencia(mensaje: str):
    mensaje_limpio = limpiar_texto(mensaje)
    # Filtrar solo letras válidas y contar
    letras = [c for c in mensaje_limpio if c in ABC]
    conteo = collections.Counter(letras)
    letra_mas_frecuente = conteo.most_common(1)[0][0]
    
    print(f"[*] Letra detectada más frecuente: {letra_mas_frecuente}")
    
    for posible in ['E', 'A', 'O']:
        salto = calcular_salto(letra_mas_frecuente, posible)
        resultado = descifrar(mensaje, salto)
        print(f"    -> Probando '{posible}': {resultado}")

def main():
    # Ejercicio 1
    mostrar_seccion("FUERZA BRUTA")
    msg1 = "Nc xkfc gu dgnnc"
    print(f"Mensaje: {msg1}")
    fuerza_bruta(msg1)

    # Ejercicio 2
    mostrar_seccion("CONOCIMIENTO ADICIONAL")
    msg2 = "Zo qgweidugotío sh jb hsqgsid"
    salto = calcular_salto("d", "o")
    print(f"Mensaje: {msg2}")
    print(f"Resultado: {descifrar(msg2, salto)}")

    # Ejercicio 3
    mostrar_seccion("FRECUENCIA")
    msg3 = "Jx qzd kfhnp mjwnw f ptx ijqfx xnr ifwxj hzjryf xtgwj ytit hzfrit jwjx ñtajr"
    print(f"Mensaje: {msg3}")
    resolver_frecuencia(msg3)

if __name__ == "__main__":
    main()
'''