import cv2


yuz_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
gulumseme_cascade = cv2.CascadeClassifier("Nariz.xml")

cap = cv2.VideoCapture(0)
cap.set(3, 640) # set Width
cap.set(4, 480) # set Height

font = cv2.FONT_HERSHEY_SIMPLEX

k = 0
while k != 27:
    ret, img = cap.read()

    gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    yuzler = yuz_cascade.detectMultiScale(gri, 1.3, 5)

    yuzSayac = 0
    for (x, y, w, h) in yuzler:
        yuzSayac += 1

        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 1)
        cv2.putText(img, f'id: {yuzSayac} x:{x}, y:{y}', (x, y), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

        gulumsemeler = gulumseme_cascade.detectMultiScale(gri[y:y + h, x:x + w], 1.3, 5)

        for(sx, sy, sw, sh) in gulumsemeler:
            cv2.rectangle(img[y:y + h + 100, x:x + w + 100], (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)


    cv2.imshow('Mutluluk tanima - press ESC to EXIT',img)

    k = cv2.waitKey(30)

print("Program ended..")