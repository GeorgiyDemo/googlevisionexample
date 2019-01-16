import os, cv2

image_folder = 'images'
video_name = 'video.mp4'

images = []
for i in range (0,1669):
    images.append("outputframe"+str(i)+".jpg.png")
frame = cv2.imread(images[0])
height, width, layers = frame.shape
video = cv2.VideoWriter(video_name, -1, 1, (width,height))

for image in images:
    video.write(cv2.imread(image))

cv2.destroyAllWindows()
video.release()