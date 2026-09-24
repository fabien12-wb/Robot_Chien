def parse_command(text):
    text = text.lower()

    actions = []

    if "lève" in text or "debout" in text:
        actions.append("stand_up")

    if "avance" in text:
        actions.append("forward")

    if "recule" in text:
        actions.append("backward")

    if "gauche" in text:
        actions.append("turn_left")

    if "droite" in text:
        actions.append("turn_right")

    if "arrête" in text or "stop" in text:
        actions.append("stop")

    return actions