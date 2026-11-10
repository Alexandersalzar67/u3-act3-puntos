import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

#Alexander Salazar NC = 0139
print("Alexander Salazar NC 0139")
print("UIII Act 3 colocar puntos a una imagen en blanco y negro")
mi_imagen = cv2.imread("pacheco blanco y negro.png")
plt.imshow(mi_imagen)
plt.title("pacheco shaggy Alexander Salazar 0139")
plt.show()

print("+-+-+-+puntos de la imagen+-+-+-+")
plt.imshow(mi_imagen)
x = [100,100,300]
y = [100,400,500]
plt.scatter(x,y,s=20,c="red")
plt.show()