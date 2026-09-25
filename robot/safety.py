ALLOWED_ACTIONS = {
    "stand_up",
    "stand_down",
    "forward",
    "backward",
    "turn_left",
    "turn_right",
    "spin_left",
    "spin_right",

    # Actions avancées
    "hello",
    "sit",
    "stretch",
    "dance",
    "backflip",

    "stop",
}


MOVEMENT_ACTIONS = {
    "forward",
    "backward",
    "turn_left",
    "turn_right",
    "spin_left",
    "spin_right",
}


MAX_DURATION = 3.0
MAX_TOTAL_MOVEMENT_DURATION = 5.0


def secure_actions(actions):
    safe_actions = []
    total_movement_duration = 0.0

    for item in actions:
        action = item.get("action")
        duration = item.get("duration", 0)

        # Refuse toute action inconnue
        if action not in ALLOWED_ACTIONS:
            print(f"SECURITE : action refusée -> {action}")
            continue

        try:
            duration = float(duration)
        except (TypeError, ValueError):
            print(f"SECURITE : durée invalide -> {duration}")
            continue

        duration = max(0.0, duration)

        # Les déplacements sont limités dans le temps
        if action in MOVEMENT_ACTIONS:

            duration = min(duration, MAX_DURATION)

            remaining = (
                MAX_TOTAL_MOVEMENT_DURATION
                - total_movement_duration
            )

            if remaining <= 0:
                print("SECURITE : durée totale maximale atteinte.")
                break

            duration = min(duration, remaining)

            total_movement_duration += duration

        # Les actions prédéfinies n'utilisent pas de durée
        else:
            duration = 0.0

        safe_actions.append({
            "action": action,
            "duration": duration
        })

    # Toujours terminer par STOP
    if not safe_actions or safe_actions[-1]["action"] != "stop":
        safe_actions.append({
            "action": "stop",
            "duration": 0.0
        })

    return safe_actions