import json
import numpy as np
import win32api
import time
import math

#the function recieve the json file and returs a new list with 2 list inside
# the first nested list is of the adult and the second is for the child.
def newList(points):
    pointsList=[]
    tmpList=[]
    tmpList.append(points[0].get('keypoints'))
    pointsList.append(tmpList[0][30:33])
    tmpList.append(points[1].get('keypoints'))
    pointsList.append(tmpList[1][0:3])
    return pointsList
    
#--------------------------------------------------------------------------------------------------------------------------------------------

#the function recieve a list with 6 point-points 0-2 are the coardinates of the hand
#and the points 3-5 are the coardinates of the child noise
#with the format x,w,z,x,w,z
def calculateDistance (listPoints):
    dist=math.sqrt((listPoints[0][0] - listPoints[1][0]) ** 2 + (listPoints[0][1] - listPoints[1][1]) ** 2 + (listPoints[0][2] - listPoints[1][2]) ** 2) 
    return dist   

#---------------------------------------------------------------------------------------------------------------------------------------------

#load the json file to a variable (data)
with open(r'C:\Users\user\OneDrive\Escritorio\results2.json') as f:
    data = json.load(f)
keyList=[]
tmp=0
vel=0 #the velocity of the slap
length=len(data)
flag=False #flag if the hand is on the children face
for i in range (length):
    
    if (data[i].get('image_id')==(str(tmp)+".jpg")):
        keyList.append(data[i].get('keypoints'))
    if (data[i].get('image_id')!=(str(tmp)+".jpg")):
        rHand=[]
        rHand.append(keyList[0][30:33])
        lHand=[]
        lHand.append(keyList[0][27:30])
        lengthKey=len(keyList)
        
        
        #the loop compare the coardinets of the adult object to the others objects
        for t in (t+1 for t in range (lengthKey-1)):
           lEar= np.array(keyList[t][12:15])
           nouse= np.array(keyList[t][0:3])
           radius=np.linalg.norm(lEar-nouse)
           nX=nouse[0]
           nY=nouse[1]
           nZ=nouse[2]
           nXr=nX+radius
           nYr=nY+radius
           nZr=nZ+radius
           #print(count)
           
           #if the hand of the adults is on the face of the children then check the velocity
           if(((lHand[0][0]<nXr) and (lHand[0][0]>nX) and (lHand[0][1]<nYr) and (lHand[0][1]>nY) and (lHand[0][2]<nZr ) and (lHand[0][2]>nZ)) or ((rHand[0][0]<nXr) and (rHand[0][0]>nX) and (rHand[0][1]<nYr) and (rHand[0][1]>nY) and (rHand[0][2]<nZr) and (rHand[0][2]>nZ))):
               sec=tmp/20
               tmpList=newList(data)
               dist=calculateDistance(tmpList)
               vel=dist/sec
               if(vel>7):
                   flag=True
               

               break
   
        tmp=tmp+1
        keyList=[]
        rHand=[]
        lHand=[]
        lEar=[]
        nouse=[]

        
        if (flag):
            print("slap")
            break
    
#print(count)  

  
            
           
            
            

        
