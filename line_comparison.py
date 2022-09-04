import logging
import math

logging.basicConfig(filename="line_comparison.log", filemode="a", level=logging.DEBUG)


class Linecomparison:
    def __init__(self, coordinate_dict):
        self.x1 = coordinate_dict.get('x1')
        self.y1 = coordinate_dict.get('y1')
        self.x2 = coordinate_dict.get('x2')
        self.y2 = coordinate_dict.get('y2')

    def calculate_distance(self):
        """
        this function is used to calculate distance between two points

        :return: distance
        """
        logging.debug("execute the program")
        try:
            distance = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
            # print(distance)
            return distance
        except Exception as e:
            logging.exception(e)


if __name__ == '__main__':
    print("Enter x,y cordinate of point 1")
    x1 = int(input("Enter the x1 coordinates : "))
    y1 = int(input("Enter the y1 coordinates : "))
    print("Enter x,y cordinate of point 2")
    x2 = int(input("Enter the x2 coordinates : "))
    y2 = int(input("Enter the y2 coordinates : "))
    line_dict = {'x1': x1, 'x2': x2, 'y1': y1, 'y2': y2}
    line_obj = Linecomparison(line_dict)
    distance = line_obj.calculate_distance()
    print("the distance between the  point is " ,distance)