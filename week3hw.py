import cv2
import sys
import numpy as np
if (sys.argv[0] == "-i")
	fileLocation = "image.png"
	img = cv2.imread(fileLocation)
	cv2.imshow("Here is the image", img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
else if (sys.argv[0] == "-l")
	cv2.NamedWindow("Camera Feed", cv2.CV_WINDOW_AUTOSIZE)
	capture = cv2.CaptureFromCAM(0)
	While True:
		frame = cv2.QueryFrame(capture)
		cv2.ShowImage("Camera Feed", frame)
		key = cv2.waitKey(10)
		if key == 27:
			break
	cv2.destroyWindow("preview")