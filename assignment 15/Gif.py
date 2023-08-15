import os
import imageio

myfiles = os.listdir("assignment 15/IMG")
images = []

for i in range(len(myfiles)):
    image = imageio.imread("assignment 15/IMG/" + myfiles[i])
    images.append(image)
    
imageio.mimsave("Heart.gif" , images)
