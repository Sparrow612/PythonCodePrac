# class Car:
#     def __init__(self, t):
#         self.carType = t


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spaces = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.spaces[carType - 1]:
            self.spaces[carType - 1] -= 1
            return True
        return False


if __name__ == '__main__':
    p = ParkingSystem(1, 1, 0)
    print(p.addCar(1), p.addCar(3))
# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
