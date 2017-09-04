from gpiozero import LED



def toggle_light(ref):
    # Get leds
    lights = {
        "yellow": {
            "led": LED(4),
            "status": False
        },
        "green": {
            "led": LED(14),
            "status": False
        },
        "red": {
            "led": LED(15),
            "status": False
        },
    }

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
    led = lights[ref]["led"]
    if lights[ref]["status"]:
        led.off()
        led = lights[ref]["status"] = False
    else:
        led.on()
        led = lights[ref]["status"] = True
