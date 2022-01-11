# TD CONVOLUTION
# TEAM 4
# Remy BARBERET - Pierrot CAVALIER - Leo CHARDON - Gwennael FRANCOIS 


import sys
import cv2
import numpy as np


def filter_image(image):
    # Conversion en niveau de gris
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    

    # Filtre moyenneur
    img2 = img.copy()
    # Création du noyau
    moyenneur_kernel = np.array([[1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1]]) / 30
    # Application du filtre
    cv2.filter2D(src=img, dst=img2, ddepth=-1, kernel=moyenneur_kernel)

    # Filtre Sobel
    g_x = img.copy()
    g_y = img.copy()
    img_sobel = img.copy()
    # Création des noyaux
    sobel_kernel_x = np.array([[-1, 0, 1], 
                            [-2, 0, 2], 
                            [-1, 0, 1]])
    sobel_kernel_y = np.array([[-1, -2, -1], 
                            [0, 0, 0], 
                            [1, 2, 1]])
    # Création des gradients
    cv2.filter2D(src=img, dst=g_x, ddepth=-1, kernel=sobel_kernel_x)
    cv2.filter2D(src=img, dst=g_y, ddepth=-1, kernel=sobel_kernel_y)
    # Fusion des gradients
    cv2.addWeighted(g_x, 0.5, g_y, 0.5, 0, img_sobel)

    # Blur
    img_blur = cv2.blur(img, (20, 20))

    # Filtre bilateral
    # img_bil = cv2.bilateralFilter(src=img, d=-1, sigmaColor=75, sigmaSpace=75)
    
    return img, img2, img_sobel, img_blur#, img_bil


if sys.argv[1] not in ["image", "video", "webcam"]:
    print("Usage:\npython convulution.py image path/to/image.png \nOR\npython convolution.py video path/to/video.mp4\nOR\npython convolution.py webcam")
    exit(1)

# Image
if sys.argv[1] == "image":
    image = cv2.imread(sys.argv[2])

    # Application des filtres
    img, img2, img_sobel, img_blur = filter_image(image)

    # Affichage
    cv2.imshow("Entree", image)
    cv2.imshow("Gray", img)
    cv2.imshow("Moyenneur", img2)
    cv2.imshow("Sobel", img_sobel)
    cv2.imshow("Blur", img_blur)
    # cv2.imshow("Bilateral", img_bil)
    cv2.waitKey(0)

# Video
elif sys.argv[1] == "video":
    cap = cv2.VideoCapture(sys.argv[2])
    while True:
        success, image = cap.read()
        if cv2.waitKey(20) == ord('q') or not success:
            break

        # Application des filtres
        img, img2, img_sobel, img_blur = filter_image(image)

        # Affichage
        cv2.imshow("Entree", image)
        cv2.imshow("Gray", img)
        cv2.imshow("Moyenneur", img2)
        cv2.imshow("Sobel", img_sobel)
        cv2.imshow("Blur", img_blur)
        # cv2.imshow("Bilateral", img_bil)

# Webcam
elif sys.argv[1] == "webcam":
    cameraCapture = cv2.VideoCapture(0)
    success, image = cameraCapture.read()
    while success and cv2.waitKey(1) == -1:
        # Application des filtres
        img, img2, img_sobel, img_blur = filter_image(image)

        # Affichage
        cv2.imshow("Entree", image)
        cv2.imshow("Gray", img)
        cv2.imshow("Moyenneur", img2)
        cv2.imshow("Sobel", img_sobel)
        cv2.imshow("Blur", img_blur)
        # cv2.imshow("Bilateral", img_bil)
        
        success, image = cameraCapture.read()

cv2.destroyAllWindows()