import os
from dotenv import load_dotenv

from robot.robot_factory import create_robot
from robot.action_executor import execute_actions
from llm.llm_client import get_actions_from_llm
from robot.safety import secure_actions
from logger import log_command

load_dotenv()

robot_mode = os.getenv("ROBOT_MODE", "simulation")
network_interface = os.getenv("ROBOT_NETWORK_INTERFACE") or None

robot = create_robot(
    mode=robot_mode,
    network_interface=network_interface
)

print("=== Contrôle intelligent Unitree Go2 ===")
print("Écris 'quitter' pour fermer le programme.\n")


while True:

    command = input("Que doit faire le Go2 ? ")

    if command.lower() in ["quitter", "exit", "quit"]:
        print("Programme terminé.")
        break

    actions = get_actions_from_llm(command)

    print("Actions comprises :", actions)

    safe_actions = secure_actions(actions)

    print("Actions sécurisées :", safe_actions)

    log_command(
    command=command,
    actions=safe_actions,
    mode=robot_mode
)

    if not safe_actions:
        print("Aucune action comprise.\n")
        continue

    execute_actions(robot, safe_actions)

    print()