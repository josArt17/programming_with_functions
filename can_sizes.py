import math

def main():
    
 radius = float(input("Enter the radius: "))
 height = float(input("Enter the height: "))

 volume = compute_volume(radius, height)
 surface_area = compute_surface_area(radius, height)

 storage_efficiency = volume / surface_area

 print(f"The storage efficiency is: {storage_efficiency:.2f}")




def compute_volume(radius, height):
 volume = (math.pi * (radius**2) * height)

 return volume



def compute_surface_area(radius, height):
 surface_area = ((2*math.pi) * radius) * (radius + height)
 
 return surface_area


main()