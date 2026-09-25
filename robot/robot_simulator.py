import time


class RobotSimulator:

    def stand_up(self):
        print("SIMULATION : le Go2 se lève")

    def stand_down(self):
        print("SIMULATION : le Go2 se baisse")

    def forward(self, duration=1):
        print(f"SIMULATION : le Go2 avance pendant {duration} seconde(s)")
        time.sleep(duration)

    def backward(self, duration=1):
        print(f"SIMULATION : le Go2 recule pendant {duration} seconde(s)")
        time.sleep(duration)

    def turn_left(self, duration=1):
        print(f"SIMULATION : le Go2 tourne à gauche pendant {duration} seconde(s)")
        time.sleep(duration)

    def turn_right(self, duration=1):
        print(f"SIMULATION : le Go2 tourne à droite pendant {duration} seconde(s)")
        time.sleep(duration)

    def spin_left(self, duration=1):
        print(f"SIMULATION : le Go2 effectue une rotation à gauche pendant {duration} seconde(s)")
        time.sleep(duration)

    def spin_right(self, duration=1):
        print(f"SIMULATION : le Go2 effectue une rotation à droite pendant {duration} seconde(s)")
        time.sleep(duration)

    # Actions avancées

    def hello(self):
        print("SIMULATION : le Go2 effectue un geste de salutation")

    def sit(self):
        print("SIMULATION : le Go2 s'assoit")

    def stretch(self):
        print("SIMULATION : le Go2 s'étire")

    def dance(self):
        print("SIMULATION : le Go2 effectue une danse")

    def backflip(self):
        print("SIMULATION : le Go2 effectue un salto arrière")

    def stop(self):
        print("SIMULATION : arrêt du Go2")