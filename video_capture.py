import cv2

cap = cv2.VideoCapture(0)
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))   # width
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # height
print('w {}'.format(width))
print('h {}'.format(height))
mid_x = int(width/2)
mid_y = int(height/2)
while True:
    if(cap.isOpened()):
        # Capture frame
        ret, frame = cap.read()
        if ret:
            cv2.line(frame,(mid_x,0),(mid_x,height),(255,0,0),3)
            cv2.line(frame,(0,mid_y),(width,mid_y),(255,0,0),3)
            cv2.imshow('Frame',frame)
            if( cv2.waitKey(1) == ord('q')):
                break
            

cap.release()
cv2.destroyAllWindows()