# PyLogger - Simple Python Keylogger

**PyLogger** es un keylogger ligero y discreto desarrollado en Python utilizando la librería `pynput`. Captura las pulsaciones de teclas en tiempo real y las registra en un archivo de forma continua, imitando un texto escrito naturalmente. Ideal para fines educativos, pruebas de seguridad o monitoreo en entornos controlados.

---

## 🚀 Características

- 🧠 Registro en tiempo real de pulsaciones del teclado.
- 📄 Almacenamiento de texto continuo (mantiene espacios, mayúsculas y caracteres especiales).
- 🔒 Discreto y fácil de ocultar como proceso.
- 🛠️ Basado en `pynput`, compatible con Windows, Linux y macOS.
- 📁 Salida configurable en archivo local.

---

## 📦 Requisitos

- Python 3.x
- Librería `pynput`

Instalación de dependencias:

```bash
pip3 install -r requirements.txt
```

## 🚀 Uso
Ejecuta el script principal:

```bash
# Ejecución normal
python3 pylogger.py

# Ejecución en modo oculto (como proceso)
nohup python3 pylogger.py >/dev/null 2>&1 &
```

El archivo `keylog.txt` se generará en el mismo directorio, con las pulsaciones registradas en forma de texto plano continuo.

## ⚠️ Aviso Legal
Este software se proporciona únicamente con fines educativos y de auditoría de seguridad en sistemas propios o con consentimiento explícito. No está permitido su uso malintencionado o ilegal. El autor no se hace responsable del uso indebido del mismo.

