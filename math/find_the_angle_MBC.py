import math
 
def areaOfTriangle():

    ab = int(input())
    bc = int(input())
    
    #doing perpendicular/base to find the tan angle
    tan_angle_value = ab / bc
    
    #taking the exact value of the degree by applying tan inverse function

    #in rad
    angle = math.atan(tan_angle_value)

    #then converting it to degree
    degree_value = math.degrees(angle)

    #taking it to the interger form with exact round off process
    exact_value = round(degree_value) 
    print(f'{exact_value}°')

areaOfTriangle()


