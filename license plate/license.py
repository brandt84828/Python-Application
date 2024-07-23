import cv2
import license_module as m

capture = cv2.VideoCapture(0)   # create camera object
if capture.isOpened():
    while True:
        sucess, img = capture.read()
        if sucess:
            cv2.imshow('Frame', img)        # show image
        k = cv2.waitKey(100)                # wait for keyboard input
        if k == ord('s') or k == ord('S'):  
            cv2.imwrite('shot.jpg', img)    
            text = m.get_license(img)        
            print('車牌:', text)

        if k == ord('q') or k == ord('Q'): 
            print('exit')
            cv2.destroyAllWindows()         # close window
            capture.release()               # release camera object
            break
else:
    print('開啟攝影機失敗')
