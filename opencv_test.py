import cv2

yuz_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

goz_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

cap = cv2.VideoCapture(0)
cap.set(3, 640) # set Width
cap.set(4, 480) # set Height

font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, img = cap.read()

    gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    yuzler = yuz_cascade.detectMultiScale(gri, 1.3, 5)

    yuzSayac = 0

    for (x, y, w, h) in yuzler:
        yuzSayac += 1

        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(img, f'id: {yuzSayac} x:{x}, y:{y}', (x, y), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

        #print(f'id: {yuzSayac} x:{x}, y:{y}')

        roi_gri = gri[y:y + h, x:x + w] #her yuz icin gri yuz alani aliniyor detect islemi icin

        roi_color = img[y:y + h, x:x + w] #renkli hali geri ekrana basmak icin

        gozler = goz_cascade.detectMultiScale(roi_gri, 1.3, 5)

        for(gx, gy, gw, gh) in gozler: #goz bulma islemleri yuz icinde...
            cv2.circle(roi_color, (gx+int(gw/2), gy+int(gh/2)), int(gw/2), (0, 255, 0), 1)
            #cv2.putText(img, f'Goz x:{gx},Goz y:{gy}', (x, y-50), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)


    cv2.imshow('Goruntu tanima v2',img)

    k = cv2.waitKey(30)

    #ESC cikis Kontrolu
    if k == 27:
        break
