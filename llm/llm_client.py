import os
import json

from robot.action_model import validate_actions
from dotenv import load_dotenv
from openai import OpenAI


# Charge les variables contenues dans le fichier .env
load_dotenv()

# Récupère la clé API sans l'écrire directement dans le code
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Seules ces actions peuvent être envoyées à notre robot
ALLOWED_ACTIONS = [
    "stand_up",
    "stand_down",
    "forward",
    "backward",
    "turn_left",
    "turn_right",
    "spin_left",
    "spin_right",
    "stop"
]


def get_actions_from_llm(command):

    prompt = f"""
Tu es le système de commande d'un simulateur du robot Unitree Go2.

Transforme la demande de l'utilisateur en une liste JSON.

Chaque élément doit avoir exactement cette forme :
{{"action": "nom_action", "duration": nombre}}

Actions autorisées :
{ALLOWED_ACTIONS}

Règles :
- Réponds uniquement avec une liste JSON.
- Utilise uniquement les actions autorisées.
- Respecte l'ordre demandé.
- duration représente une durée en secondes.
- Pour stand_up, stand_down et stop, utilise duration = 0.
- Si l'utilisateur ne précise pas de durée pour un déplacement, utilise 1 seconde.
- Pour cette simulation, une durée de déplacement ne peut pas dépasser 3 secondes.
- turn_left et turn_right représentent un virage.
- spin_left et spin_right représentent une rotation sur place.
- Termine tout déplacement par une action stop.
- Si la demande n'est pas comprise, retourne [].

Demande utilisateur :
{command}
"""

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    result = response.output_text.strip()

    try:
        actions = json.loads(result)
    except json.JSONDecodeError:
        return []

    if not isinstance(actions, list):
        return []

    return validate_actions(actions)

 