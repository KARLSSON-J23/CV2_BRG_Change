# •請將一段由攝影機攝得的視訊(或視訊檔案)，經由色彩通道重新安排後，儲存成立另一個新的視訊檔案
# •繳交新視訊檔案


import cv2
import numpy as np
import time

cam = cv2.VideoCapture(0)
video = cv2.VideoWriter()
s_time = time.time()

 
fps = 6
sec = 5
channel = 3
fourcc = cv2.VideoWriter_fourcc(*'MP42')
ret, img = cam.read()
div = int(img.shape[0]/3)

width = img.shape[1]
hieght = img.shape[0]

def re_write(img):
  for row in range(img.shape[0]):
      for col in range(img.shape[1]):
        val = img[row][col]
        if(col > width/2 ):
          if(row > 2 * div):
            img[row][col] = [ 0,0,val[2]]
          elif(row < div):
            img[row][col] = [ 0,val[1],0]
          else:
            img[row][col] = [ val[0],0,0]
  return img
def re_writeRGB(img):
  for row in range(img.shape[0]):
      for col in range(img.shape[1]):
        if(col > width/2 ):
          img[row][col] = [img[row][col][2],img[row][col][1],img[row][col][0]]
  return img


video = cv2.VideoWriter('test.mp4', fourcc, float(fps), (width, hieght))

while True:
  ret, img = cam.read()
  img = re_write(img)
  video.write(img)
          
  if ret:
    cv2.imshow('123',img)
  if cv2.waitKey(1) == ord('q') or (time.time() - s_time) >= 10:
    break
video.release()
