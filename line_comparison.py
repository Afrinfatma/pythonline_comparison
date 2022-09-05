import logging
import math

logging.basicConfig(filename="line_comparison.log", filemode="a", level=logging.DEBUG)
print ("--------------welcome to line comparison program-------------------")

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

def check_length(line1, line2):
        if line1 == line2:
            print("both lines are equal")
        elif line1 > line2 :
            print("Line1 is greater than line 2")
        else:
            print("line2 is greater than line1")

if __name__ == '__main__':
    def draw_lines():
        try:

            print("Enter x,y cordinate of point 1")
            x1 = int(input("Enter the x1 coordinates : "))
            y1 = int(input("Enter the y1 coordinates : "))
            print("Enter x,y cordinate of point 2")
            x2 = int(input("Enter the x2 coordinates : "))
            y2 = int(input("Enter the y2 coordinates : "))
            line_dict = {'x1': x1, 'x2': x2, 'y1': y1, 'y2': y2}
            line_obj = Linecomparison(line_dict)
            distance = line_obj.calculate_distance()
            # print("the distance between the  point is " ,distance)
            return line_obj
        except Exception as e:
            logging.debug(e)

    print("Enter the coordinates of line 1: \n")
    line1 = draw_lines().calculate_distance()
    print(line1)
    print("Enter the coordinates of line 2: \n")
    line2 = draw_lines().calculate_distance()
    print(line2)
    check_length(line1,line2)

