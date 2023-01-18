import cv2

face_cascade = cv2.CascadeClassifier('xml.xml')
img = cv2.imread(r'hank2.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for(x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
cv2.imshow('Imagine:', img)
cv2.waitKey();
