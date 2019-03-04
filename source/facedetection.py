import cv2

class FaceDetection:
   face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
   img = cv2.imread("D:\\PythonWebProject\\images\\TestImage.jpg", 1)

   #gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

   faces = face_cascade.detectMultiScale(img, scaleFactor = 1.05, minNeighbors = 5)

   font = cv2.FONT_HERSHEY_SIMPLEX
   for x,y,w,h in faces:
      img = cv2.rectangle(img, (x,y), (x + w, y + h), (0, 0 , 255), 3)
      cv2.putText(img, str(x) + "," + str(y), (x - 3, y + 3), font, 2, (255, 0, 0), 2, cv2.LINE_AA)
      cv2.putText(img,  str(x + w) + "," + str(y), ((x + w) - 3, y + 3), font, 2, (255, 0, 0), 2, cv2.LINE_AA)
      cv2.putText(img, str(x) + "," + str(y + h), (x - 3, (y + h) + 3), font, 2, (255, 0, 0), 2, cv2.LINE_AA)
      cv2.putText(img, str(x + w) + "," + str(y + h), ((x + w) - 3, (y + h) + 3), font, 2, (255, 0, 0), 2, cv2.LINE_AA)

   cv2.imshow("MyPuttani", img)
   #cv2.waitKey(0)

   #cv2.destroyAllWindows()

   #print(faces)