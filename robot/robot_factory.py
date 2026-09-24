from robot.robot_simulator import RobotSimulator


def create_robot(mode="simulation", network_interface=None):

    if mode == "simulation":
        print("MODE : SIMULATION")
        return RobotSimulator()

    elif mode == "dry_run":
        print("MODE : DRY RUN")
        print("Aucune commande ne sera envoyée au vrai Go2.")
        return RobotSimulator()

    elif mode == "real":
        if not network_interface:
            raise ValueError(
                "Une interface réseau est nécessaire pour le vrai Go2."
            )

        from robot.go2_controller import Go2Controller

        print("MODE : GO2 RÉEL")
        return Go2Controller(network_interface)

    else:
        raise ValueError("Mode inconnu.")