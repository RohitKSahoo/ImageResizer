import cv2

#configurable parameters
source = "elizabth_olsen.jpeg"
destination = "Resized_image.png"
scale_percent = 400  # percent of original size

image = cv2.imread(source, cv2.IMREAD_UNCHANGED)
#cv2.imshow("title", image)

print('Original Dimensions : ', image.shape)

new_width = int(image.shape[1] * scale_percent / 100)
new_height = int(image.shape[0] * scale_percent / 100)

# resize image
resized = cv2.resize(image, (new_width, new_height))

print('Resized Dimensions : ', resized.shape)

cv2.imwrite(destination, resized)
#cv2.waitKey(0)
cv2.destroyAllWindows()