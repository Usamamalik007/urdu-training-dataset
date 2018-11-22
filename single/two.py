import cv2
import numpy as np

thisdict ={
  "1":"ا",
  "2":"ب" ,
  "3":"ت" ,
  "4":"ث",
  "5":"ج",
  "6":"ح",
  "7":"خ",
  "8":"د",
  "9":"ذ"

}

       


x=1
y=1
while x<10:
    y=1
    while y<10:
        img1 = cv2.imread(str(x)+'.jpg')
        img2 = cv2.imread(str(y)+'.jpg')
        vis = np.concatenate((img1, img2), axis=1)
        cv2.imwrite(str(x)+str(y)+ '.png', vis)
        with open(str(x)+str(y)+'.gt.txt', 'w',encoding="utf-8") as f:
            a = thisdict.get(str(x))
            b = thisdict.get(str(y))
            f.write(str(b) + " "+str(a) )
        print("y= "+str(y))
        y=y+1
    x=x+1
    print("x= "+str(x))
    

