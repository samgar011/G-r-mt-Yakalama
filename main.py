# Import required libraries
import cv2
import numpy as np
import dlib
 
 
# Pc ye bağlı kamerayı çalıştırma
cap = cv2.VideoCapture(0)
 
 
# Kordinatları Yakala
detector = dlib.get_frontal_face_detector()
 
 
# Yüzde Kare Oluştur
while True:
 
    # Kare kare Yakalama
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
 
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
 
    # Yüz Hesaplama
    i = 0
    for face in faces:
 
        # Yüzü Kare Çerçeve İçerisine Alma 
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)
 
        
        i = i+1
 
        # Yüzü Gördüğünde Kare ve Yazı Oluşturma
        cv2.putText(frame, 'Taninan Yuz'+str(i), (x-10, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        print(face, i)
 
    # Yüz numaralandırma
    cv2.imshow('frame', frame)
 
    # q tuşunu çıkış olarak atama
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
 
# Pencereli Kapat
cap.release()
cv2.destroyAllWindows()