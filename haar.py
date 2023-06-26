import cv2

def detect():
	face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
	face_cascade.load('./haarcascade_frontalface_default.xml')
	eye_cascade = cv2.CascadeClassifier('./haarcascade_eye.xml')
	eye_cascade.load('./haarcascade_eye.xml')
	camera = cv2.VideoCapture(0)
	scaling_factor = 0.5 
	while True:
		ret, frame =camera.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		frame = cv2.resize(frame, None, fx=scaling_factor, 
 fy=scaling_factor, interpolation=cv2.INTER_AREA)
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		for (x, y, w, h) in faces:
			img = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
			roi_gray = gray[y:y+h, x:x+w]
			eyes = eye_cascade.detectMultiScale(roi_gray, 1.03, 5, 0, (40,40))
			for (ex, ey, ew, eh) in eyes:
				cv2.rectangle(img, (ex, ey), (ex+ew, ey+ eh), (0,255, 0), 2)
		cv2.imshow('camera', frame)
		if cv2.waitKey(1000//12) & 0xff == ord('q'):
			break

	camera.release()
	cv2.desstroyAllWindows()
if __name__ == '__main__':
	detect()
detect()



