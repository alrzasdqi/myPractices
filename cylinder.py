pi = 22 / 7
height = float (input("Height of Cylinder : "))
radian = float(input("Radian of Cylinder : "))

volume = height * radian * radian * pi
sur_area = ((2 * pi * radian) * height) + ((pi * radian ** 2) * 2)


print("Volume is : ", str(volume))
print("surface area is : ", str(sur_area))