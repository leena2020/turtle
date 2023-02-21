import turtle

class TurtleInterpreter:
    def __init__(self):
        self.turtles = {}
        self.screen = turtle.Screen()
        self.screen.setup(800, 600)
        self.screen.bgcolor('white')

    def run(self, code):
        for line in code.split('\n'):
            line = line.strip()
            if not line:
                continue
            command, *args = line.split()
            try:
                getattr(self, command)(*args)
            except AttributeError:
                print(f"Invalid command: {command}")

    def turtle(self, name):
        self.turtles[name] = turtle.Turtle()

    def move(self, name, distance):
        self.turtles[name].forward(float(distance))

    def left(self, name, angle):
        self.turtles[name].left(float(angle))

    def right(self, name, angle):
        self.turtles[name].right(float(angle))

    def pen(self, name, state):
        if state == 'up':
            self.turtles[name].penup()
        elif state == 'down':
            self.turtles[name].pendown()

    def color(self, name, color):
        self.turtles[name].pencolor(color)

if __name__ == '__main__':
    code = """
    turtle alice
    move alice 100
    left alice 90
    move alice 100
    left alice 90
    move alice 100
    left alice 90
    move alice 100

    turtle bob
    color bob red
    pen bob up
    move bob -50
    pen bob down
    move bob 100
    left bob 90
    move bob 100
    left bob 90
    move bob 100
    left bob 90
    move bob 100
    """
    i = TurtleInterpreter()
    i.run(code)
    turtle.done()
