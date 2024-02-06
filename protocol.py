from typing import Protocol, runtime_checkable

@runtime_checkable
class Device(Protocol):
    def turn_on(self) -> None:
        pass
    
    def turn_off(self) -> None:
        pass

class Camera:
    def turn_on(self) -> None:
        print("Camera is ON")

    def turn_off(self) -> None:
        print("Camera is OFF")

class Monitor:
    def turn_on(self) -> None:
        print("Monitor is ON")

    def turn_off(self) -> None:
        print("Monitor is OFF")

def main():
    # Creating instances of classes that conform to the Device protocol
    camera = Camera()
    monitor = Monitor()

    # Using the protocol methods
    camera.turn_on()
    camera.turn_off()

    monitor.turn_on()
    monitor.turn_off()

if __name__ == "__main__":
    main()
