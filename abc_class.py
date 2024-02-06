from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass

class Camera(Device):
    def turn_on(self):
        print("Camera is ON")

    def turn_off(self):
        print("Camera is OFF")

class Monitor(Device):
    def turn_on(self):
        print("Monitor is ON")

    def turn_off(self):
        print("Monitor is OFF")

def main():
    # Creating instances of derived classes
    camera = Camera()
    monitor = Monitor()

    # Using abstract methods
    camera.turn_on()
    camera.turn_off()

    monitor.turn_on()
    monitor.turn_off()

if __name__ == "__main__":
    main()
