class Automat:

    def __init__(self, matrix, start):
        self.__matrix = matrix
        self.__inputs = {
                            "a": 0, #odpovida prvnimu poli v matici: "[[a], []]"
                            "b": 1  #odpovida druhemu poli v matici: "[[], [b]]"
                        }  
        self.current = start
        self.start = start

    def move(self, inp: str) -> int:
        index = self.__inputs[inp]
        self.current = self.__matrix[index][self.current]
        return self.current

    def reset(self):
        self.current = self.start
        return self.current


def main():
    matrix1 = [[0, 0, 0, 3], [1, 2, 3, 3]]
    automat1 = Automat(matrix1)

    matrix2 = [[0, 0, 3, 0, 4], [1, 2, 2, 4, 4]]
    automat2 = Automat(matrix2)

    matrix3 = [[0, 0, 4, 3, 0, 7, 7, 7], [1, 2, 3, 3, 5, 6, 3, 5]]
    automat3 = Automat(matrix3)


if __name__ == "__main__":
    main()
