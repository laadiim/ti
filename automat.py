# model class for a finite automat
class Automat:

    def __init__(self, matrix, start):
        self.__matrix = matrix
        self.__inputs = {
                            "a": 0, #odpovida prvnimu poli v matici: "[[a], []]"
                            "b": 1  #odpovida druhemu poli v matici: "[[], [b]]"
                        }  
        self.current = start
        self.start = start

    # move the automat
    def move(self, inp: str) -> int:
        index = self.__inputs[inp]
        self.current = self.__matrix[index][self.current]
        return self.current

    # reset the automat
    def reset(self):
        self.current = self.start
        return self.current
