<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:1a0a2e,100:16213e&height=200&section=header&text=👻%20DarkHash&fontSize=60&fontAlignY=38&desc=Hash%20Cracker%20Educativo%20para%20Kali%20Linux&descAlignY=58&fontColor=ffffff&animation=fadeIn"/>

</div>

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=flat-square&logo=kalilinux&logoColor=white)
![Hacking Ético](https://img.shields.io/badge/Hacking_Ético-00FF41?style=flat-square&logo=hackthebox&logoColor=black)
![Educativo](https://img.shields.io/badge/Uso-Solo_Educativo-red?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-purple?style=flat-square)

</div>

---

> ⚠️ **AVISO LEGAL:** DarkHash es una herramienta desarrollada **exclusivamente con fines educativos** y de aprendizaje en ciberseguridad. Úsala **únicamente en sistemas y hashes de tu propiedad o con autorización explícita**. El uso indebido de esta herramienta puede ser ilegal. El autor no se hace responsable del mal uso.

---

## 🧠 ¿Qué es DarkHash?

**DarkHash** es una herramienta de línea de comandos escrita en Python para Kali Linux que permite:

- **Identificar** automáticamente el tipo de hash (MD5, SHA-1, SHA-256, etc.)
- **Crackear** hashes usando ataques de diccionario (wordlist)
- **Generar** hashes desde texto plano para pruebas
- Aprender cómo funcionan los ataques de fuerza bruta por diccionario

Es ideal para estudiantes de ciberseguridad, CTFs y práctica en entornos controlados.

---

## ⚡ Características

| Feature | Descripción |
|---|---|
| 🔐 Multi-algoritmo | MD5, SHA-1, SHA-224, SHA-256, SHA-384, SHA-512 |
| 🕵️ Auto-detección | Identifica el tipo de hash por su longitud |
| 📂 Ataque por diccionario | Usa cualquier wordlist `.txt` |
| ⚙️ Generador de hashes | Crea hashes desde texto plano |
| 🎨 Interfaz visual | Colores ANSI, progreso en tiempo real |
| 🖥️ CLI completo | Modo interactivo + argumentos (`argparse`) |
| 🚀 Alto rendimiento | Muestra velocidad en hashes/segundo |

---

## 🛠️ Instalación

```bash
# Clonar el repositorio
git clone https://github.com/YeinerParraRincon/DarkHash.git

# Entrar al directorio
cd DarkHash

# Dar permisos de ejecución
chmod +x darkhash.py

# Ejecutar
python3 darkhash.py
```

> No requiere librerías externas. Funciona con Python 3 estándar.

---

## 🚀 Uso

### Modo interactivo
```bash
python3 darkhash.py
```

### Crackear un hash desde terminal
```bash
python3 darkhash.py -c <HASH> -w wordlist.txt
python3 darkhash.py -c <HASH> -w wordlist.txt -a sha256
```

### Generar un hash
```bash
python3 darkhash.py -g "mipassword" -a md5
python3 darkhash.py -g "mipassword" -a sha256
```

### Ver ayuda
```bash
python3 darkhash.py --help
```

---

## 🔢 Algoritmos soportados

| Algoritmo | Longitud del hash |
|---|---|
| MD5 | 32 caracteres |
| SHA-1 | 40 caracteres |
| SHA-224 | 56 caracteres |
| SHA-256 | 64 caracteres |
| SHA-384 | 96 caracteres |
| SHA-512 | 128 caracteres |

---

## 📂 Estructura del proyecto

```
DarkHash/
├── darkhash.py       # Herramienta principal
├── wordlist.txt      # Wordlist incluida
└── README.md         # Este archivo
```

---

## 📋 Ejemplo de uso

```
  ██████╗  █████╗ ██████╗ ██╗  ██╗██╗  ██╗ █████╗ ███████╗██╗  ██╗
  ...

  [ Hash Cracker — Herramienta Educativa de Ciberseguridad ]
  by Yeiner Parra Rincón | WorldSkills 🥈 | SENA ADSO
  ⚠️  Solo para uso ético y autorizado.

[*] Hash objetivo  : 5f4dcc3b5aa765d61d8327deb882cf99
[*] Tipo detectado : MD5
[*] Algoritmo usado: MD5
[*] Wordlist       : wordlist.txt

[✓] ¡HASH CRACKEADO!
    Hash     : 5f4dcc3b5aa765d61d8327deb882cf99
    Texto    : password
    Intentos : 42
    Tiempo   : 0.003s
```

---

## 👤 Autor

**Yeiner Parra Rincón**
- 🏆 Subcampeón Nacional WorldSkills Colombia 2025
- 🎓 SENA — Tecnólogo ADSO
- 📍 La Dorada, Caldas, Colombia 🇨🇴

[![GitHub](https://img.shields.io/badge/GitHub-YeinerParraRincon-181717?style=flat-square&logo=github)](https://github.com/YeinerParraRincon)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-yeinerparrarincon-0077B5?style=flat-square&logo=linkedin)](https://linkedin.com/in/yeinerparrarincon)

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:16213e,50:1a0a2e,100:0f0c29&height=100&section=footer&animation=fadeIn"/>
</div>