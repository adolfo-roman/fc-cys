from des import des

# ==============================================================================
# P6 - Prueba de Cifrado y Descifrado con DES
# Descripción: Este script demuestra el funcionamiento básico del algoritmo DES 
# importado. Toma un mensaje en texto plano y una llave específica para generar 
# el criptograma. Posteriormente, toma ese mismo criptograma y aplica el modo 
# de descifrado con la misma llave para validar que se recupera el texto original.
# ==============================================================================

message = "noche697"
key = "data7Qa="  
encrypted = des(message, key)
decrypted = des(encrypted, key, "d")

print(f"P6: Cifrado y Descifrado con DES")
print("-" * 40)
print(f"Mensaje original: {message}")
print(f"Llave utilizada: {key}")
print(f"Mensaje cifrado DES 'des(message, key)': {encrypted}")
print(f"Mensaje descifrado DES 'des(message, key, \"d\")': {decrypted}")
print("-" * 40)