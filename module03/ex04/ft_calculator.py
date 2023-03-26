class Calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
            Calculates the dot product of two vectors of equal length
        """
        result = sum([V1[i] * V2[i] for i in range(len(V1))])
        print(f"{result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
            Adds two vectors of equal length
        """
        result = [float(V1[i] + V2[i]) for i in range(len(V1))]
        print(f"{result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
            Subtracts two vectors of equal length
        """
        result = [float(V1[i] - V2[i]) for i in range(len(V1))]
        print(f"{result}")
