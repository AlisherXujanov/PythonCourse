import cv2
# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# Open default camera
cap = cv2.VideoCapture(0)
while True:
	# Read frame
	ret, frame = cap.read()
	if not ret:
		break
	# Convert to grayscale for face detection
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# Detect faces
	faces = face_cascade.detectMultiScale(gray, 1.1, 4)
	# Draw rectangles around faces
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
	# Display the frame
	cv2.imshow('Testing emotion detection', frame)
	# Break loop with 'q' key
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()