import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

finger_tips = [8, 12, 16, 20]
thumb_tip = 4


while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    h, w, c = img.shape
    results = hands.process(img)

    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            lm_list = []
            for id, lm in enumerate(hand_landmark.landmark):
                lm_list.append(lm)
        # stop working properly 🖐️
            if lm_list[4].y < lm_list[2].y and \
                lm_list[8].y < lm_list[6].y and \
                lm_list[12].y < lm_list[10].y and \
                lm_list[16].y < lm_list[14].y and \
                lm_list[20].y < lm_list[18].y and \
                lm_list[8 and 12 and 16 and 20].y < lm_list[4].y and \
                lm_list[17].x > lm_list[0].x > lm_list[5].x and \
                lm_list[4].x < lm_list[5].x :
                cv2.putText(img, "Stop", (550, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                #print("Stop")        
            if lm_list[4].y < lm_list[2].y and \
                lm_list[8].y < lm_list[6].y and \
                lm_list[12].y < lm_list[10].y and \
                lm_list[16].y < lm_list[14].y and \
                lm_list[20].y < lm_list[18].y and \
                lm_list[17].x < lm_list[0].x < lm_list[5].x and \
                lm_list[4].x > lm_list[5].x :
                cv2.putText(img, "Stop", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                #print("Stop")

        # Like working properly 👍
            if lm_list[thumb_tip].y < lm_list[thumb_tip - 1].y < lm_list[thumb_tip - 2].y and \
                lm_list[0].x>lm_list[3].x and \
                lm_list[8].x>lm_list[5].x and \
                lm_list[12].x>lm_list[9].x and \
                lm_list[16].x>lm_list[13].x and \
                lm_list[8 and 12 and 16 and 20].y>lm_list[4].y and \
                lm_list[1 and 2].x>lm_list[5 and 9].x and \
                lm_list[5].y<lm_list[17].y and \
                lm_list[8].y<lm_list[20].y and \
                lm_list[0].x>lm_list[9].x and \
                lm_list[20].x>lm_list[17].x:
                cv2.putText(img, "LIKE", (550, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                #print("LIKE")
            if lm_list[thumb_tip].y < lm_list[thumb_tip - 1].y < lm_list[thumb_tip - 2].y and \
                lm_list[0].x<lm_list[3].x and \
                lm_list[8].x<lm_list[5].x and \
                lm_list[12].x<lm_list[9].x and \
                lm_list[16].x<lm_list[13].x and \
                lm_list[5 and 9 and 13 and 17].x>lm_list[0].x and \
                lm_list[5].y<lm_list[17].y and \
                lm_list[20].x<lm_list[17].x:
                cv2.putText(img, "LIKE", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                #print("LIKE")
                    
        # Dislike working properly 👎
            if lm_list[thumb_tip].y > lm_list[thumb_tip - 1].y > lm_list[thumb_tip - 2].y and \
                lm_list[0].y < lm_list[3].y and \
                lm_list[0].x > lm_list[3].x and \
                lm_list[8].x>lm_list[5].x and \
                lm_list[12].x>lm_list[9].x and \
                lm_list[16].x>lm_list[13].x and \
                lm_list[20].x>lm_list[17].x:
                cv2.putText(img, "DISLIKE", (500, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                #print("DISLIKE")
            if lm_list[thumb_tip - 2].y > lm_list[thumb_tip - 3].y > lm_list[thumb_tip - 4].y and \
                lm_list[0].y < lm_list[3].y and \
                lm_list[0].x < lm_list[3].x and \
                lm_list[8].x<lm_list[5].x and \
                lm_list[12].x<lm_list[9].x and \
                lm_list[16].x<lm_list[13].x and \
                lm_list[0].x<lm_list[17].x and \
                lm_list[20].x<lm_list[17].x:
                cv2.putText(img, "DISLIKE", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                #print("DISLIKE")
            
        # Victory working properly ✌️
            if  lm_list[5].y > lm_list[6].y > lm_list[7].y > lm_list[8].y and \
                lm_list[9].y > lm_list[10].y > lm_list[11].y > lm_list[12].y and \
                lm_list[20].y > lm_list[19].y > lm_list[18].y and \
                lm_list[20].y > lm_list[17].y and \
                lm_list[16].y > lm_list[13].y and \
                lm_list[5].x < lm_list[17].x and \
                lm_list[4].x > lm_list[5].x and \
                lm_list[8].x < lm_list[12].x and \
                lm_list[16].y > lm_list[4].y:
                cv2.putText(img, "Victory", (500, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                #print("Victory")
            if  lm_list[5].y > lm_list[6].y > lm_list[7].y > lm_list[8].y and \
                lm_list[9].y > lm_list[10].y > lm_list[11].y > lm_list[12].y and \
                lm_list[20].y > lm_list[19].y > lm_list[18].y and \
                lm_list[20].y > lm_list[17].y and lm_list[16].y > lm_list[13].y and \
                lm_list[5].x > lm_list[17].x and \
                lm_list[4].x < lm_list[5].x and \
                lm_list[8].x > lm_list[12].x and \
                lm_list[16].y > lm_list[4].y:
                cv2.putText(img, "Victory", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                #print("Victory")
            
        # Party working properly 🤟
            if lm_list[4].y < lm_list[2].y and \
                lm_list[8].y < lm_list[6].y and \
                lm_list[10].y < lm_list[12].y and \
                lm_list[14].y < lm_list[16].y and \
                lm_list[20].y < lm_list[18].y and \
                lm_list[17].x > lm_list[5].x and \
                lm_list[4].x < lm_list[5].x :
                cv2.putText(img, "Party", (550, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                #print("Party")
            if lm_list[4].y < lm_list[2].y and \
                lm_list[8].y < lm_list[6].y and \
                lm_list[10].y < lm_list[12].y and \
                lm_list[14].y < lm_list[16].y and \
                lm_list[20].y < lm_list[18].y and \
                lm_list[17].x < lm_list[5].x and \
                lm_list[4].x > lm_list[5].x :
                cv2.putText(img, "Party", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                #print("Party")
            
        # Super working properly 👌
            if lm_list[4].y < lm_list[2].y and \
                lm_list[6].y < lm_list[8].y and \
                lm_list[12].y < lm_list[10].y and \
                lm_list[16].y < lm_list[14].y and \
                lm_list[2].x < lm_list[17].x and \
                lm_list[5 and 9].x < lm_list[0].x and \
                lm_list[20].y < lm_list[18].y :
                cv2.putText(img, "Super", (540, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                #print("Super")
            if lm_list[4].y < lm_list[2].y and \
                lm_list[6].y < lm_list[8].y and \
                lm_list[12].y < lm_list[10].y and \
                lm_list[16].y < lm_list[14].y and \
                lm_list[2].x > lm_list[17].x and \
                lm_list[20].y < lm_list[18].y :
                cv2.putText(img, "Super", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                #print("Super")
        
        # Call working properly 🤙
            if lm_list[4].y < lm_list[2].y and \
                lm_list[6].y < lm_list[8].y and \
                lm_list[10].y < lm_list[12].y and \
                lm_list[14].y < lm_list[16].y and \
                lm_list[20].y < lm_list[18].y and \
                lm_list[17].x > lm_list[0].x > lm_list[5].x and \
                lm_list[4].x < lm_list[5].x :
                cv2.putText(img, "Call", (550, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                #print("Call")
            if lm_list[4].y < lm_list[2].y and \
                lm_list[6].y < lm_list[8].y and \
                lm_list[10].y < lm_list[12].y and \
                lm_list[14].y < lm_list[16].y and \
                lm_list[20].y < lm_list[18].y and \
                lm_list[17].x < lm_list[0].x < lm_list[5].x and \
                lm_list[4].x > lm_list[5].x :
                cv2.putText(img, "Call", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                #print("Call")
        
        # Gun working properly 👈
            if lm_list[4].x < lm_list[3].x and \
                lm_list[8].x < lm_list[6].x and \
                lm_list[12].x < lm_list[10].x and \
                lm_list[14].x < lm_list[16].x and \
                lm_list[20 and 16].y > lm_list[5].y and \
                lm_list[18].x < lm_list[20].x:
                cv2.putText(img, "Gun", (550, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                #print("Gun")
            if lm_list[4].x > lm_list[3].x and \
                lm_list[8].x > lm_list[6].x and \
                lm_list[12].x > lm_list[10].x and \
                lm_list[14].x > lm_list[16].x and \
                lm_list[20 and 16].y > lm_list[5].y and \
                lm_list[18].x > lm_list[20].x:
                cv2.putText(img, "Gun", (550, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                #print("Gun")
                
        # Smile working properly 👈
            if lm_list[4].x > lm_list[3].x and \
                lm_list[8].x < lm_list[6].x and \
                lm_list[12].x > lm_list[10].x and \
                lm_list[14].x < lm_list[16].x and \
                lm_list[20 and 16].y > lm_list[5].y and \
                lm_list[18].x < lm_list[20].x:
                cv2.putText(img, "Smile", (550, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                #print("Smile")
            if lm_list[4].x < lm_list[3].x and \
                lm_list[8].x > lm_list[6].x and \
                lm_list[12].x < lm_list[10].x and \
                lm_list[14].x > lm_list[16].x and \
                lm_list[20 and 16].y > lm_list[5].y and \
                lm_list[18].x > lm_list[20].x:
                cv2.putText(img, "Smile", (550, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                #print("Smile")
        
        # Small working properly 🤏
            if lm_list[thumb_tip].x < lm_list[thumb_tip - 1].x < lm_list[thumb_tip - 2].x and \
                lm_list[6].x>lm_list[8].x and \
                lm_list[10].x<lm_list[12].x and \
                lm_list[14].x<lm_list[16].x and \
                lm_list[11 and 15 and 19].y>lm_list[6].y and \
                lm_list[12 and 16 and 20].y>lm_list[6].y and \
                lm_list[2 and 5 and 9].x<lm_list[0].x and \
                lm_list[5].x<lm_list[17].x and \
                lm_list[18].x<lm_list[20].x :
                cv2.putText(img, "Small", (540, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                #print("Small")
            if lm_list[thumb_tip].x > lm_list[thumb_tip - 1].x > lm_list[thumb_tip - 2].x and \
                lm_list[6].x<lm_list[8].x and \
                lm_list[10].x>lm_list[12].x and \
                lm_list[14].x>lm_list[16].x and \
                lm_list[11 and 15 and 19].y>lm_list[6].y and \
                lm_list[17].x<lm_list[5].x and \
                lm_list[9].y<lm_list[12].y and \
                lm_list[18].x>lm_list[20].x :
                cv2.putText(img, "Small", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                #print("Small")
        
        # Punch working properly 👊
            if lm_list[5].y < lm_list[6].y > lm_list[8].y and \
                lm_list[9].y < lm_list[10].y > lm_list[12].y and \
                lm_list[13].y < lm_list[14].y > lm_list[16].y and \
                lm_list[17].y < lm_list[18].y > lm_list[20].y and \
                lm_list[2].y < lm_list[3].y and \
                lm_list[17].x > lm_list[5].x and \
                lm_list[3].x < lm_list[4].x :
                cv2.putText(img, "Punch", (520, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                #print("Punch")
            if lm_list[5].y < lm_list[6].y > lm_list[8].y and \
                lm_list[9].y < lm_list[10].y > lm_list[12].y and \
                lm_list[13].y < lm_list[14].y > lm_list[16].y and \
                lm_list[17].y < lm_list[18].y > lm_list[20].y and \
                lm_list[2].y < lm_list[3].y and \
                lm_list[17].x < lm_list[5].x and \
                lm_list[3].x > lm_list[4].x :
                cv2.putText(img, "Punch", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                #print("Punch")
        
        # Raise working properly ✊
            if lm_list[6].y < lm_list[7].y and \
                lm_list[10].y < lm_list[11].y and \
                lm_list[14].y < lm_list[15].y and \
                lm_list[18].y < lm_list[19].y and \
                lm_list[17].x > lm_list[5].x and \
                lm_list[7 and 11 and 15 and 19].y < lm_list[0].y and \
                lm_list[3].x < lm_list[4].x:
                cv2.putText(img, "Raise", (550, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                #print("Raise")
            if lm_list[6].y < lm_list[7].y and \
                lm_list[10].y < lm_list[11].y and \
                lm_list[14].y < lm_list[15].y and \
                lm_list[18].y < lm_list[19].y and \
                lm_list[17].x < lm_list[5].x and \
                lm_list[7 and 11 and 15 and 19].y < lm_list[0].y and \
                lm_list[3].x > lm_list[4].x:
                cv2.putText(img, "Raise", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                #print("Raise")
        
        # Good luck 🤞
            if lm_list[5].y > lm_list[6].y > lm_list[7].y > lm_list[8].y and \
                lm_list[9].y > lm_list[10].y > lm_list[11].y > lm_list[12].y and \
                lm_list[20].y > lm_list[19].y > lm_list[18].y and \
                lm_list[20].y > lm_list[17].y and \
                lm_list[16].y > lm_list[13].y and \
                lm_list[5].x < lm_list[17].x and \
                lm_list[4].x > lm_list[5].x and \
                lm_list[8].x > lm_list[12].x and \
                lm_list[16].y > lm_list[4].y:
                cv2.putText(img, "Good luck", (450, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                #print("Good luck")
            if lm_list[5].y > lm_list[6].y > lm_list[7].y > lm_list[8].y and \
                lm_list[9].y > lm_list[10].y > lm_list[11].y > lm_list[12].y and \
                lm_list[20].y > lm_list[19].y > lm_list[18].y and \
                lm_list[20].x > lm_list[17].x and \
                lm_list[16].y > lm_list[13].y and \
                lm_list[5].x > lm_list[17].x and \
                lm_list[4].x < lm_list[5].x and \
                lm_list[8].x < lm_list[12].x and \
                lm_list[16].y > lm_list[4].y:
                cv2.putText(img, "Good luck", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                #print("Good luck") 1=font size, 3=thickness
        

            mp_draw.draw_landmarks(img, hand_landmark,
                                   mp_hands.HAND_CONNECTIONS,
                                   mp_draw.DrawingSpec((0, 0, 0), 5, 2),
                                   mp_draw.DrawingSpec((255, 255, 255), 4, 20)
                                   )

    cv2.imshow("Hand Sign Detection", img)
    keypress=cv2.waitKey(1)
    if keypress == ord("q"):
        break
        
        

