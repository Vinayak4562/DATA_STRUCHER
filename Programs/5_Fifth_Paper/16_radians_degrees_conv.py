'''16. Write a function in Python that accepts one numeric parameter. This parameter will be the measure of an angle in radians. The function should convert the radians into degrees and then return that value. Do not use inbuilt functions.
Note : Angle in Radians × 180°/π = Angle in Degrees.
'''

def radians_to_degrees(angle_rad):
    return angle_rad * 180 / 3.142

angle_rad = float(input("Enter the Radiance: "))
angle_deg = radians_to_degrees(angle_rad)
print(f'The {angle_rad} Radiance is equal to {angle_deg} Degrees')

# Input:- Enter the Radiance: 1.5
# Output:-The 1.5 Radiance is equal to 85.9325270528326 Degrees