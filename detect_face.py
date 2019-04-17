#! /usr/bin/env python
import cv2
import sys

def find_face_image():
	# image to analyze/Cascade for opencv to perform analysis
	imagePath = "YourImagePath"
  
  # You need to download this xml file. It's necessary for the program to run
	cascPath = "/YourPath/haarcascade_frontalface_default.xml"

	# Read the image and convert to grayscale
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# Create the haar cascade. Used for algorithm to find faces
	face_cascade = cv2.CascadeClassifier(cascPath)

	# Detect faces in the image
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
	    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
	    roi_gray = gray[y:y+h, x:x+w]
	    roi_color = image[y:y+h, x:x+w]

	# Print out how many faces were found in the image
	print("Found {0} faces!".format(len(faces)))

	# Show the image with the selected faces. If user enters ESC key then exit program
	while True:
		cv2.imshow("Faces found", image)
		
		if cv2.waitKey(1) & 0xFF == 27:
			break

	cv2.destroyAllWindows()
