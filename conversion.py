# -*-coding:Latin-1 -*
# TD CONVOLUTION
# TEAM 4
# Remy BARBERET - Pierrot CAVALIER - Leo CHARDON - Gwennael FRANCOIS 


import sys
import cv2
import numpy as np

def filter_image(image):
    # Conversion en niveau de gris
    
    #Conversion par openCV
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #Conversion par formule
    '''
    img = image.copy()
    #On récupère les dimensions de l'image
    (largeur, hauteur) = img.shape[:2]
    for x in range(largeur):
        for y in range(hauteur):
	# On modifie chaque pixel avec la formule donnée
            r,v,b = img[x,y]
            img[x,y] = (0.2989*r, 0.5870*v, 0.1140*b)
	'''

    return img


if sys.argv[1] not in ["image", "video", "webcam"]:
    print("Usage:\npython convulution.py image path/to/image.png \nOR\npython convolution.py video path/to/video.mp4\nOR\npython convolution.py webcam")
    exit(1)

# Image
if sys.argv[1] == "image":
    image = cv2.imread(sys.argv[2])

    # Application du filtre
    img = filter_image(image)

    # Affichage
    cv2.imshow("Entree", image)
    cv2.imshow("Gray", img)
    cv2.waitKey(0)

# Video
elif sys.argv[1] == "video":
    cap = cv2.VideoCapture(sys.argv[2])
    while True:
        success, image = cap.read()
        if cv2.waitKey(20) == ord('q') or not success:
            break

        # Application du filtre
        img = filter_image(image)

        # Affichage
        cv2.imshow("Entree", image)
        cv2.imshow("Gray", img)

# Webcam
elif sys.argv[1] == "webcam":
    cameraCapture = cv2.VideoCapture(0)
    success, image = cameraCapture.read()
    while success and cv2.waitKey(1) == -1:
        # Application du filtre
        img = filter_image(image)

        # Affichage
        cv2.imshow("Entree", image)
        cv2.imshow("Gray", img)
        # cv2.imshow("Bilateral", img_bil)
        
        success, image = cameraCapture.read()

cv2.destroyAllWindows()