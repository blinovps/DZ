import time


class TrafficLight:
    def __init__(self):
        self.__color = ["red", "yellow", "green", "yellow"]

    def running(self):
        while True:
            for c in list(self.__color):
                if c == "yellow":
                    print(f"\r{c}", end="")
                    time.sleep(2)
                else:
                    print(f"\r{c}", end="")
                    time.sleep(7)


tl = TrafficLight()
tl.running()
