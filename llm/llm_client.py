import os
import json

from dotenv import load_dotenv
from openai import OpenAI
from robot.action_model import validate_actions


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Capacités physiques que le LLM peut demander au robot
ALLOWED_ACTIONS = [
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

    "stop"
]


# Historique de la conversation
conversation_history = []


SYSTEM_PROMPT = f"""
Tu es l'assistant conversationnel incarné dans un robot quadrupède Unitree Go2.

Ton rôle principal est de converser naturellement avec l'utilisateur.
Tu peux discuter, répondre aux questions, comprendre le contexte de la
conversation et tenir compte des échanges précédents.

Tu disposes également d'un corps robotique et de capacités physiques.

Lorsque le contexte de la conversation justifie réellement une action physique,
tu peux décider d'utiliser une ou plusieurs de tes capacités disponibles.

Capacités physiques disponibles :
{ALLOWED_ACTIONS}

Signification des capacités :
- stand_up : se lever
- stand_down : se baisser
- forward : avancer
- backward : reculer
- turn_left : tourner à gauche
- turn_right : tourner à droite
- spin_left : effectuer une rotation sur place vers la gauche
- spin_right : effectuer une rotation sur place vers la droite
- hello : effectuer un geste physique de salutation
- sit : s'asseoir
- stretch : s'étirer
- dance : effectuer une danse
- backflip : effectuer un salto arrière
- stop : arrêter le mouvement

Règles concernant les actions physiques :
- Une conversation normale ne nécessite généralement aucune action physique.
- Ne déclenche une action que lorsque le contexte de la conversation la justifie.
- Comprends les intentions à partir du langage naturel et du contexte de la conversation.
- Lorsque tu parles d'une action physique exécutée, décris uniquement ce qui est
  connu à partir de son nom et de l'historique. N'invente pas de détails sur les
  mouvements précis, les articulations ou le résultat physique de l'action.
- L'utilisateur n'a pas besoin d'utiliser le nom exact d'une capacité.
- Si l'utilisateur pose seulement une question sur une capacité, tu peux répondre sans nécessairement l'exécuter.
- N'invente jamais une capacité physique qui n'est pas disponible.
- Pour un déplacement sans durée précisée, utilise 1 seconde.
- Une action de déplacement ne doit jamais dépasser 3 secondes.
- Pour les actions qui ne dépendent pas d'une durée, utilise duration = 0.

Tu dois répondre exclusivement avec un objet JSON valide.

Sans action physique :

{{
    "message": "ta réponse naturelle à l'utilisateur",
    "actions": []
}}

Avec une ou plusieurs actions physiques :

{{
    "message": "ta réponse naturelle à l'utilisateur",
    "actions": [
        {{"action": "nom_action", "duration": nombre}}
    ]
}}

Le champ "message" contient ce que tu souhaites dire naturellement à l'utilisateur.
Le champ "actions" contient uniquement les actions physiques que tu souhaites exécuter.
"""


def chat_with_robot(user_message):

    # Enregistre le message de l'utilisateur
    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    # Construction du contexte conversationnel
    history_text = ""

    for message in conversation_history:

        if message["role"] == "user":
            role = "Utilisateur"

        elif message["role"] == "assistant":
            role = "Assistant"

        else:
            role = "Événement physique"

        history_text += (
            f"{role}: {message['content']}\n"
        )

    prompt = f"""
{SYSTEM_PROMPT}

Voici la conversation jusqu'à présent :

{history_text}

Produis maintenant la prochaine réponse.
"""

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    result = response.output_text.strip()

    try:
        data = json.loads(result)

    except json.JSONDecodeError:
        return {
            "message": result,
            "actions": []
        }

    message = data.get("message", "")
    raw_actions = data.get("actions", [])

    if not isinstance(raw_actions, list):
        raw_actions = []

    # Validation Pydantic des actions demandées par le LLM
    actions = validate_actions(raw_actions)

    # Enregistre la réponse conversationnelle
    conversation_history.append({
        "role": "assistant",
        "content": message
    })

    return {
        "message": message,
        "actions": actions
    }


def remember_executed_actions(actions):
    """
    Enregistre dans l'historique les actions physiques
    effectivement envoyées au robot.
    """

    if not actions:
        return

    # On ignore STOP car il est souvent ajouté
    # automatiquement par la couche Safety.
    executed_actions = [
        item["action"]
        for item in actions
        if item["action"] != "stop"
    ]

    if not executed_actions:
        return

    conversation_history.append({
        "role": "system",
        "content": (
            "Actions physiques exécutées par le robot : "
            + ", ".join(executed_actions)
        )
    })