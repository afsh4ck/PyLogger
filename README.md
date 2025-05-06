# PyLogger - Simple Python Keylogger

```
    ____          __                                   
   / __ \ __  __ / /   ____   ____ _ ____ _ ___   _____
  / /_/ // / / // /   / __ \ / __ `// __ `// _ \ / ___/
 / ____// /_/ // /___/ /_/ // /_/ // /_/ //  __// /    
/_/     \__, //_____/\____/ \__, / \__, / \___//_/     
       /____/              /____/ /____/               

```

**PyLogger** es un keylogger ligero y discreto desarrollado en Python utilizando la librería `pynput`. Captura las pulsaciones de teclas en tiempo real y las registra en un archivo de forma continua, imitando un texto escrito naturalmente. Ideal para fines educativos, pruebas de seguridad o monitoreo en entornos controlados.

---

## 🚀 Características

- 🧠 Registro en tiempo real de pulsaciones del teclado.
- 📄 Almacenamiento de texto continuo (mantiene espacios, mayúsculas y caracteres especiales).
- 🔒 Discreto y fácil de ocultar como proceso.
- 🛠️ Basado en `pynput`, compatible con Windows, Linux y macOS.
- 📁 Salida configurable en archivo local.


## 📦 Instalación

```bash
git clone https://github.com/afsh4ck/PyLogger.git
cd PyLogger
pip3 install -r requirements.txt
python3 pylogger.py
```

## 🚀 Uso

```bash
# Ejecución normal (terminal abierta)
python3 pylogger.py

# Ejecución en modo oculto (como proceso)
nohup python3 pylogger.py >/dev/null 2>&1 &
```
- `nohup` evita que se cierre si cierras la terminal.
- `>/dev/null 2>&1` oculta toda salida (stdout y stderr).
- `&` lo ejecuta en segundo plano.

🔍 Verifica que está corriendo:

```bash
ps aux | grep pylogger.py
```

El archivo `keylog.txt` se generará en el mismo directorio, con las pulsaciones registradas en forma de texto plano continuo.

## ⚠️ Aviso Legal
Este software se proporciona únicamente con fines educativos y de auditoría de seguridad en sistemas propios o con consentimiento explícito. No está permitido su uso malintencionado o ilegal. El autor no se hace responsable del uso indebido del mismo.

## 👨🏻‍💻 Créditos
- Autor:       afsh4ck 
- Instagram:   <a href="https://www.instagram.com/afsh4ck">afsh4ck</a>
- Youtube:     <a href="https://youtube.com/@afsh4ck">afsh4ck</a>

## ❤️ Soporte

<a href="https://www.buymeacoffee.com/afsh4ck" rel="nofollow"><img width="250" align="left">
![buy-me-a-coffe](https://github.com/user-attachments/assets/8c8f9e81-334e-469e-b25e-29888cfc9fcc)
</a>

