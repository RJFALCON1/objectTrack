import cv2
import time
import math
vid = cv2.VideoCapture('bb3.mp4')
tracker = cv2.TrackerCSRT_create()
ret, frame = vid.read()
Bbox = cv2.selectROI('tracking', frame, False)
tracker.init(frame, Bbox)
print(Bbox)
p1 = 530
p2 = 300
xs=[]
ys=[]

def drawBox(frame,Bbox):
    x, y, w, h = int(Bbox[0]), int(Bbox[1]), int(Bbox[2]), int(Bbox[3])
    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3, 1)
    # cv2.putText(frame, 'tracking', (75, 90),
    # cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

def goalTrack(frame,Bbox) :
    x,y,w,h = int(Bbox[0]), int(Bbox[1]), int(Bbox[2]), int(Bbox[3])
    c1= x+int(w/2)
    c2 = y + int(h/2)
    # cv2.circle(frame,(c1,c2),2,(0,0,255),5)
    cv2.circle(frame,(p1,p2),2,(0,255,0),3)
    dis = math.sqrt(((c1-p1)**2)+((c2-p2)**2))
    if (dis < 20) :
        cv2.putText(frame, 'goal', (75, 90),
        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    xs.append(c1)
    ys.append(c2)
    for i in range (len(xs) - 1):
        cv2.circle(frame,(xs[i],ys[i]),2,(0,0,255),5)

while True :
    check, img = vid.read()
    success, Bbox = tracker.update(img)
    if (success == True) :
        drawBox(img,Bbox)
    else :
        cv2.putText(frame, 'lost', (75, 90),
        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    goalTrack(img,Bbox)
    cv2.imshow('result',img)
    if (cv2.waitKey(25)==32) :
        print('End of Video')
        break
vid.release()
cv2.destroyAllWindows()
