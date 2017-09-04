from gpiozero import LED

# Get leds
lights["yellow"]  = { "led": LED(4),    status: False }
lights["green"]   = { "led": LED(14),   status: False }
lights["red"]     = { "led": LED(15),   status: False }


def toggle_light(ref):

    # If not string, throw error
    if (type(ref) != type('')):
        return print("[ERR] String expected!")

    # Yellow led
    if ref in ["yellow", "amarelo"]:
        ref = "yellow"

    # Green led
    elif ref in ["green", "verde"]:
        ref = "green"

    # Red led
    elif ref in ["red", "vermelho"]:
        ref = "red"

    # Light on/off
    if lights[ref].status:
        lights[ref].led.off()
    else:
        lights[yellow].led.on()

    # Change Status
    lights[ref].status = !lights[ref].status
