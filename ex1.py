# On importe les librairies
import cv2
import numpy as np

# On boucle
for i in range(3):
	# On creer notre matrice de 512x512
	img = np.zeros((512, 512, 3), np.uint8)

	# On prepare nos matrice pour appliquer le masque
	red, green, blue = img[:,:,0], img[:,:,1], img[:,:,2]

	# On creer notre masque
	mask = (red == 0) & (green == 0) & (blue == 0)

	# On met a jour notre image en appliquant le masque
	img[:,:,:3][mask] = [
		255 if i == 0 else 0,
		255 if i == 1 else 0,
		255 if i == 2 else 0,
	]

	# On ajoute les formes
	# cv2.line(image, start_point, end_point, color, thickness)
	cv2.line(img, (100, 200), (100, 300), (0, 0, 0), 10)
	# cv2.circle(image, center_coordinates, radius, color, thickness)
	cv2.circle(img, (100, 100), 100, (0, 0, 0), 3)
	# cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
	cv2.putText(img, '5I-IN7', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1, cv2.LINE_AA)

	# On affiche l'image
	cv2.imshow(str(i), img)

# On attend un input et on ferme les fenetres
cv2.waitKey(0)
cv2.destroyAllWindows()
