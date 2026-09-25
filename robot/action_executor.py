def execute_actions(robot, actions):

    for item in actions:

        action = item["action"]
        duration = item["duration"]

        if action == "stand_up":
            robot.stand_up()

        elif action == "stand_down":
            robot.stand_down()

        elif action == "forward":
            robot.forward(duration)

        elif action == "backward":
            robot.backward(duration)

        elif action == "turn_left":
            robot.turn_left(duration)

        elif action == "turn_right":
            robot.turn_right(duration)

        elif action == "spin_left":
            robot.spin_left(duration)

        elif action == "spin_right":
            robot.spin_right(duration)

        elif action == "hello":
            robot.hello()

        elif action == "sit":
            robot.sit()

        elif action == "stretch":
            robot.stretch()

        elif action == "dance":
            robot.dance()

        elif action == "backflip":
            robot.backflip()

        elif action == "stop":
            robot.stop()