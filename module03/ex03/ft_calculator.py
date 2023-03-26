class calculator:

    def __init__(self, vector):
        self.vector = vector

    def __add__(self, scalar):
        """
        Adds a scalar to each element of the vector
        """
        self.vector = [element + scalar for element in self.vector]
        print(self.vector)
        return self.vector

    def __mul__(self, scalar):
        """
        Multiplies each element of the vector by a scalar
        """
        self.vector = [element * scalar for element in self.vector]
        print(self.vector)
        return self.vector

    def __sub__(self, scalar):
        """
        Subtracts a scalar from each element of the vector
        """
        self.vector = [element - scalar for element in self.vector]
        print(self.vector)
        return self.vector

    def __truediv__(self, scalar):
        """
        Divides each element of the vector by a scalar
        """
        self.vector = [element / scalar for element in self.vector]
        print(self.vector)
        return self.vector
