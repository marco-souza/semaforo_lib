from gpiozero import LED



def toggle_light(ref):
    # Get leds
    lights = {}
    lights["yellow"].led = LED(4)
    lights["yellow"].status = False
    lights["green"].led = LED(14)
    lights["green"].status = False
    lights["red"].led = LED(15)
    lights["red"].status = False

    # If not string, throw error
    if (type(ref) != type('')):
        return print("[ERR] String expected!")

    # Yellow led
    if ref in ["yellow", "amarelo"]:
        print("yellow")
        ref = "yellow"

    # Green led
    elif ref in ["green", "verde"]:
        print("green")
        ref = "green"

    # Red led
    elif ref in ["red", "vermelho"]:
        print("red")
        ref = "red"

    # Light on/off & Change Status
    if lights[ref].status:
        lights[ref].led.off()
        lights[ref].status = False
    else:
        lights[ref].led.on()
        lights[ref].status = True
