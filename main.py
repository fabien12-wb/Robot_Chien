import os
from dotenv import load_dotenv

from robot.robot_factory import create_robot
from robot.action_executor import execute_actions

from llm.llm_client import (
    chat_with_robot,
    remember_executed_actions
)

from robot.safety import secure_actions
from logger import log_command


load_dotenv()


robot_mode = os.getenv(
    "ROBOT_MODE",
    "simulation"
)


network_interface = (
    os.getenv("ROBOT_NETWORK_INTERFACE")
    or None
)


robot = create_robot(
    mode=robot_mode,
    network_interface=network_interface
)


print("=== Assistant Unitree Go2 ===")
print("Tu peux discuter normalement avec le robot.")
print("Écris 'quitter' pour fermer le programme.\n")


while True:

    user_message = input("Vous : ")

    if user_message.lower() in [
        "quitter",
        "exit",
        "quit"
    ]:
        print("Programme terminé.")
        break


    # Le LLM analyse le message et répond
    response = chat_with_robot(user_message)


    # Réponse conversationnelle
    print(f"\nGo2 : {response['message']}")


    # Actions physiques éventuellement demandées
    actions = response["actions"]


    if actions:

        print(
            "Actions demandées :",
            actions
        )


        # Passage par la couche de sécurité
        safe_actions = secure_actions(actions)


        print(
            "Actions sécurisées :",
            safe_actions
        )


        # Enregistrement dans les logs
        log_command(
            command=user_message,
            actions=safe_actions,
            mode=robot_mode
        )


        # Exécution sur le simulateur ou le vrai Go2
        execute_actions(
            robot,
            safe_actions
        )


        # Informe la mémoire conversationnelle
        # des actions qui viennent d'être exécutées
        remember_executed_actions(
            safe_actions
        )


    print()