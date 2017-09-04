from gpiozero import LED



def toggle_light(ref):
    # Get leds
    lights = {
        "yellow": LED(4),
        "green": LED(14),
        "red": LED(15),
    }

    # If not string, throw error
    if (type(ref) != type('')):
        return print("[ERR] String expected!")

    # Yellow led
    if ref in ["yellow", "amarelo"]:
        print("yellow", lights["yellow"])
        ref = "yellow"

    # Green led
    elif ref in ["green", "verde"]:
        print("green", lights["green"])
        ref = "green"

    # Red led
    elif ref in ["red", "vermelho"]:
        print("red", lights["red"])
        ref = "red"

    # Light on/off & Change Status
    if lights[ref].is_active:
        lights[ref].off()
    else:
        lights[ref].on()
