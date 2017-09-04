from gpiozero import LED



# Get leds
lights = {
    "yellow": LED(14),
    "green": LED(15),
    "red": LED(4),
}

def toggle_light(ref):

    # If not string, throw error
    if (type(ref) != type('')):
        return print("[ERR] String expected!")

    # Yellow led
    if ref in ["y", "yellow", "amarelo"]:
        ref = "yellow"

    # Green led
    elif ref in ["g", "green", "verde"]:
        ref = "green"

    # Red led
    elif ref in ["r", "red", "vermelho"]:
        ref = "red"

    # Light on/off & Change Status
    if lights[ref].is_active:
        lights[ref].off()
    else:
        lights[ref].on()
