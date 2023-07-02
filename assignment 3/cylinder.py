Radius = float(input('please enter radius: '))
cylinder_height = float(input('please enter height: '))

Base_environment = (2*3.14*Radius)
Side_area = (cylinder_height*Base_environment)
print('The area of the cylinder is:',Side_area)

Base_area = (Radius*Radius*3.14)
Volume = (Base_area*cylinder_height)
print('The volume of the cylinder is:',Volume)
