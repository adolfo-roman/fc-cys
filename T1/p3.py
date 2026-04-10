def contar_patrones(texto, longitud):
    conteo = {}
    
    for i in range(len(texto) - (longitud - 1)):
        patron = texto[i:i+longitud]
        
        if patron in conteo:
            conteo[patron] += 1
        else:
            conteo[patron] = 1

    elementos = []
    for patron, cantidad in conteo.items():
        if cantidad > 1:  
            elementos.append(f"{patron}")
            print(f"Patrón: '{patron}' - Ocurrencias: {cantidad}")
        
    return " ".join(elementos)

def encontrar_distancia(texto, patron):
    indices = []
    for i in range(len(texto) - (len(patron) - 1)):
        if texto[i:i+len(patron)] == patron:
            indices.append(i)
    if len(indices) < 2:
        return -1
    return indices[1] - indices[0]

def encontrar_factores(distancia):
    factores = []
    for i in range(1, distancia + 1):
        if i == 1 or i == distancia:
            continue 
        if distancia % i == 0:
            factores.append(i)
    return factores

def probable_longitud_llave(texto):
    patrones = contar_patrones(texto, 3).split()
    factores_totales = []
    
    for patron in patrones:
        print(f"\nAnalizando patrón: {patron}")
        distancia = encontrar_distancia(texto, patron)
        print(f"Distancia entre ocurrencias: {distancia}")
        if distancia > 0:
            factores = encontrar_factores(distancia)
            print(f"Factores de la distancia: {factores}")
            factores_totales.extend(factores)
            print(f"Factores acumulados: {factores_totales}")
    
    conteo_factores = {}
    for factor in factores_totales:
        if factor in conteo_factores:
            conteo_factores[factor] += 1
        else:
            conteo_factores[factor] = 1

    conteo_factores = dict(sorted(conteo_factores.items(), key=lambda item: item[1], reverse=True))

    print("\nProbable longitud de llave:")
    for factor, conteo in conteo_factores.items():
        print(f"Longitud: {factor} (conteo: {conteo})")  

def main():
    print("--- Análisis de Kasiski ---\n")
    
    texto = "ECISCRVSWVLGDDWUEFHFNGESXUVTI" \
    "COKQOTAJPHWAKFBNAEUONOJFHONCPHRZNSCOK" \
    "EWLSUFPFEEUWOMHPQFAEEDOLDBQROKFZLNQBS" \
    "XVMFZZNMQQSACESDDVMONHBROUEBGMOCVISLZ" \
    "AOXDGTJDAQVZLDRTOVAKDDWOKJTFEJBBFNHBG" \
    "LCRJRLSKVEVUDBXOPVDVZADBGSLCPOKUWSSJC" \
    "RQWCOLFOKUC"

    print(f"Texto a analizar: {texto}\n")

    probable_longitud_llave(texto)

if __name__ == "__main__":
    main()