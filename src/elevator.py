class Elevator:
    """
    Elevator class
    """
    def __init__(self, max_floor, min_floor, current_floor, direction):
        self.max_floor = max_floor
        self.min_floor = min_floor
        self.current_floor = current_floor
        self.direction = direction

    def __str__(self):
        """Returns the elevator's current state"""
        return "Elevator is on floor {} going {}".format(self.current_floor, self.direction)


    def open_door(self):
        """Elevator door opens"""
        print("The door is open")

    def close_door(self):
        """Elevator door closes"""
        print("The door is closed")

    def go_up(self):
        """Elevator goes up"""
        self.current_floor += 1
        print("The elevator is going up to floor {}".format(self.current_floor))

    def go_down(self):
        """Elevator goes down"""
        self.current_floor -= 1
        print("The elevator is going down to floor {}".format(self.current_floor))

    def get_current_floor(self):
        """Returns the current floor"""
        print("The elevator is on floor {}".format(self.current_floor))

    def get_direction(self):
        """Returns the direction"""
        print("The elevator is going {}".format(self.direction))

    def set_direction(self, direction):
        """Sets the direction"""
        self.direction = direction
        print("The elevator is going {}".format(self.direction))

    def get_max_floor(self):
        """Returns the maximum floor"""
        print("The elevator can go up to floor {}".format(self.max_floor))

    def get_min_floor(self):
        """Returns the minimum floor"""
        print("The elevator can go down to floor {}".format(self.min_floor))

    def weight_capacity_observer(self, weight):
        """Observes the weight of the elevator"""
        if weight > 1000:
            print("The elevator is overloaded")
        else:
            print("The elevator is not overloaded")

    def number_of_people_observer(self, number_of_people):
        """Observes the number of people in the elevator"""
        if number_of_people > 8:
            print("The elevator is full")
        else:
            print("The elevator is not full")

    def floor_request_optimizer(self, floor_request):
        """Optimizes the floor request"""
        if self.current_floor == floor_request:
            print("The elevator is already on that floor")
        elif self.direction == "up" and floor_request > self.current_floor:
            self.go_up()
        elif self.direction == "down" and floor_request < self.current_floor:
            self.go_down()
        else:
            print("The elevator is already on that floor")

    def emergency_call_request(self):
        """Emergency call request"""
        self.direction = "stop"
        self.open_door()
        print("The elevator is stopped")
