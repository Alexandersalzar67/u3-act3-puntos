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
print("+-+-+-+puntos de la imagen+-+-+-+")
mi_imagen = cv2.imread("pacheco blanco y negro.png")
plt.imshow(mi_imagen)
x = [200,200,500,500,200]
y = [500,100,200,500,500]
plt.scatter(x,y,c="blue")
plt.show()
mi_imagen = cv2.imread("pacheco blanco y negro.png")

mi_imagen = cv2.cvtColor(mi_imagen, cv2.COLOR_BGR2RGB)

plt.imshow(mi_imagen)
plt.title("pacheco shaggy Alexander Salazar 0139")
plt.show()

print("+-+-+-+puntos de la imagen+-+-+-+")

plt.imshow(mi_imagen)
x = [100,100,300]
y = [100,400,500]
plt.scatter(x,y,s=20,c="red")
plt.show()

print("+-+-+-+puntos de la imagen+-+-+-+")

plt.imshow(mi_imagen)
x = [200,200,500,500,200]
y = [500,100,200,500,500]
plt.scatter(x,y,c="blue")
plt.show()

print("+-+-+-+cuadro en la imagen+-+-+-+")

plt.imshow(mi_imagen)

cuadro = plt.Rectangle((100,100),200,200,
                       linewidth=3,
                       edgecolor="red",
                       facecolor="none")

plt.gca().add_patch(cuadro)
plt.show()

print("+-+-+-+circulo en la imagen+-+-+-+")

plt.imshow(mi_imagen)

circulo = plt.Circle((300,300),100,
                     linewidth=3,
                     edgecolor="blue",
                     facecolor="none")

plt.gca().add_patch(circulo)
plt.show()
