import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
img = cv2.imread("D:\\PythonWebProject\\images\\TestImage.jpg", 1)

#gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img, scaleFactor = 1.05, minNeighbors = 5)

font = cv2.FONT_HERSHEY_SIMPLEX
for x,y,w,h in faces:
   img = cv2.rectangle(img, (x,y), (x + w, y + h), (0, 0 , 255), 3)
   #cv2.putText(img, x, (x - 3, y + 3), font, 4, (255, 0, 0), 2, cv2.LINE_AA, True)



cv2.imshow("MyPuttani", img)
cv2.waitKey(0)

cv2.destroyAllWindows()

print(faces)