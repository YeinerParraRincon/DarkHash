import hashlib

def generar_hash(texto, tipo="md5"):
    texto = texto.encode()
    
    if tipo == "md5":
        return hashlib.md5(texto).hexdigest()
    elif tipo == "sha256":
        return hashlib.sha256(texto).hexdigest()
    else:
        return None

def crack_hash(hash_objetivo, wordlist, tipo):
    try:
        with open(wordlist, "r", encoding="utf-8", errors="ignore") as f:
            for linea in f:
                palabra = linea.strip()
                
                hash_prueba = generar_hash(palabra, tipo)
                
                if hash_prueba == hash_objetivo:
                    print(f"\n[+] Contraseña encontrada: {palabra}")
                    return
            
        print("\n[-] No encontrada en la wordlist")

    except FileNotFoundError:
        print("[!] Wordlist no encontrada")

if __name__ == "__main__":
    print("=== GhostCrack ===")
    
    hash_usuario = input("Ingresa el hash: ")
    tipo = input("Tipo (md5/sha256): ").lower()
    ruta_wordlist = input("Ruta del diccionario: ")
    
    crack_hash(hash_usuario, ruta_wordlist, tipo)