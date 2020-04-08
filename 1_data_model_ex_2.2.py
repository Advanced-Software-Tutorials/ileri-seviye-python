class Line:
    def __init__(self, length):
        self.length = length

    def __add__(self, other_line):
        return Line(self.length + other_line.length)

    def __mul__(self, digit):
        return Line(self.length * digit)
