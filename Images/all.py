import cv2
import numpy as np

thisdict ={
  "1":"میں",
  "2":"تم" ,
  "3":"کیا" ,
  "4":"سب",
  "5":"صبر",
  "6":"اگر" ,
  "7":"کرسی",
  "8":"بوتل",
  "9":"موبائل",
  "0":"کمرہ",
}

x=0
y=0
while x<10:
    y=0
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
    
        


        


        


x=0
y=0
z=0
while x<10:
    y=0
    while y<10:
        z=0
        while(z<10):
            
            img1 = cv2.imread(str(x)+'.jpg')
            img2 = cv2.imread(str(y)+'.jpg')
            img3 = cv2.imread(str(z)+'.jpg')  
            vis = np.concatenate((img1, img2,img3), axis=1)
            cv2.imwrite(str(x)+str(y)+str(z)+'.png', vis)
            with open(str(x)+str(y)+str(z)+'.gt.txt', 'w',encoding="utf-8") as f:
                a = thisdict.get(str(x))
                b = thisdict.get(str(y))
                c = thisdict.get(str(z))
                f.write(str(c) + " "+str(b)+" "+str(a) )
            z=z+1
            print("z=" + str(z))
        print("y= "+str(y))
        y=y+1
    x=x+1
    print("x= "+str(x))

 


w=0
x=0
y=0
z=0

while x<10:
    y=0
    while y<10:
        z=0
        while(z<10):
            w=0
            while(w<10):
            
                img1 = cv2.imread(str(x)+'.jpg')
                img2 = cv2.imread(str(y)+'.jpg')
                img3 = cv2.imread(str(z)+'.jpg')
                img4 = cv2.imread(str(w)+'.jpg')
            
                vis = np.concatenate((img1, img2,img3,img4), axis=1)
                cv2.imwrite(str(x)+str(y)+str(z)+str(w)+'.png', vis)
                with open(str(x)+str(y)+str(z)+str(w)+'.gt.txt', 'w',encoding="utf-8") as f:
                    a = thisdict.get(str(x))
                    b = thisdict.get(str(y))
                    c = thisdict.get(str(z))
                    d = thisdict.get(str(w))
                
                    f.write(str(d) + " "+str(c)+" "+str(b)+" "+str(a) )
                    w=w+1
            z=z+1
            print("z=" + str(z))
        print("y= "+str(y))
        y=y+1
    x=x+1
    print("x= "+str(x))

 
