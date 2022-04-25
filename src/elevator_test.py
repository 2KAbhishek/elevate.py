from elevator import Elevator

class ElevatorTest:
    def __init__(self):
        self.elevator = Elevator(10, 1, 1, "up")
        self.elevator.open_door()
        self.elevator.close_door()
        self.elevator.go_up()
        self.elevator.go_down()
        self.elevator.get_current_floor()
        self.elevator.get_direction()
        self.elevator.set_direction("down")
        self.elevator.get_max_floor()
        self.elevator.get_min_floor()
        self.elevator.weight_capacity_observer(1000)
        self.elevator.weight_capacity_observer(1200)

if __name__ == "__main__":
    elevator_test = ElevatorTest()
