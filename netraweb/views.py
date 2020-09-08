from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import change_d
import cv2
from PIL import Image
import numpy as np
from cv2 import cv2
import os
from netra.settings import MEDIA_ROOT
import base64
import requests
import time
flag=0
w=0
h=0
# Create your views here.

def index(request):
    return render(request,"index.html")   

def surveillance(request):  
    return render(request,"surveillance.html")      

def change_det(request):
  return render(request,"change_det.html")
  
def time_det(request):
  return render(request,"time_det.html")

def fea_ext(request):
  return render(request,"fea_ext.html")

def change_detection_result(request):
  
        render(request,"change_detection_result.html")
  

def feature_extraction_result(request,i3):
  return render(request,"feature_extraction_result.html")

def feature_extraction_result2(request):

  return render(request,"feature_extraction_result2.html")
    
def new_login(request):
  return render(request,"new_login.html")


def change_detection(request):

    
        for file in request.FILES.getlist('myfile'):
                fs = FileSystemStorage()
                file1=file.name
                filename = fs.save(file.name, file)
                f1=os.path.abspath(os.path.join(MEDIA_ROOT, file1))


        i1 = change_d()
        i1.img=filename
     
        
        for file in request.FILES.getlist('myfile2'):
                fs2 = FileSystemStorage()
                file2=file.name
                filename2 = fs2.save(file.name, file)
                f2=os.path.abspath(os.path.join(MEDIA_ROOT, file2))

        i2 = change_d()
        i2.img=filename2
        print(os.path.splitext(file1)[0])
        beforeimagename_wo_ext=os.path.splitext(file1)[0]
        afterimagename_wo_ext=os.path.splitext(file2)[0]
      
        beforeimagename=beforeimagename_wo_ext+'.jpg'
        afterimagename=afterimagename_wo_ext+'.jpg'

        diff_in_image=changedetection(beforeimagename,afterimagename_wo_ext)
        next=reversefoto(diff_in_image)
        next2=reversefotoa(next)
        merge(afterimagename, 'F&F '+afterimagename_wo_ext+'.png',next2, position=(0,0))

      
        i3 = change_d()
        i3.img='F&F '+afterimagename_wo_ext+'.png'

        return render(request,"change_detection_result.html",{'i1':i1,'i2':i2,'w':w,'h':h,'i3':i3,'diff_in_image':diff_in_image}) 
        


def feature_extraction(request):

    
        for file in request.FILES.getlist('fmyfile'):
                fs = FileSystemStorage()
                filename = fs.save(file.name, file)
                print("##3444",filename)

        start = time.time()
        responsez = str(base64.b64encode(open('media/'+filename,'rb').read()))
        responsez=responsez[2:]
        data = {"imageUrl":responsez, "mode": "1"}
        #ip address of azure-VM instance
        app_url = "http://13.68.181.120:5000/app/score-image"
        response = requests.post(app_url, json={"imageUrl":responsez, "mode": "1"})
        
        img=response.json()
        img=img[2:]
        fh =open('media/mohit.jpg',mode='wb')
        fh.write(base64.b64decode(img))
        end = time.time()
        print('Time Required:'+str(end - start))
        base_image = Image.open('media/mohit.jpg')
        base_image.show()
        
        wi,hi=base_image.size
        if wi >=1920:
          w=600
          h=340
        else:
          w=wi
          h=hi
        i3 = change_d()
        i3.img='mohit.jpg'

        
    
        return render(request,"feature_extraction_result.html",{'i3':i3,'w':w,'h':h})
        

def feature_extraction2(request):

    if request.method == 'POST':
        i1=request.POST.get("i1")
        i3=request.POST.get("i3")
        ima1=request.POST.get("image1")
        ima2=request.POST.get("image2")
        diff_in_image=request.POST.get("diff_in_image")
       
        start = time.time()
        responsez = str(base64.b64encode(open('media/'+i1,'rb').read()))
        responsez=responsez[2:]
        app_url = "http://13.68.181.120:5000/app/score-image"
        response = requests.post(app_url, json={"imageUrl":responsez, "mode": "0"})
    
        img=response.json()
        img=img[2:]
        fh =open('media/OutDetect.jpg',mode='wb')
        fh.write(base64.b64decode(img))
        end = time.time()
        print('Time Required:'+str(end - start))

        
        next22=reversefotoDetectron('media/'+diff_in_image)
        
        output_image_path2=mergeDetectron('media/OutDetect.jpg', 'Some.png',next22, position=(0,0))
        next33=reversefotoDetectron2(output_image_path2)
        mergeDetectron('media/'+i1, 'O.D.png',next33, position=(0,0))
          
        return render(request,"feature_extraction_result2.html",{'i1':i1,'i3':i3,'w':w,'h':h,'ima1':ima1,'ima2':ima2,'diff_in_image':diff_in_image})
        
def reversefotoDetectron(diffimage):
  img = Image.open(diffimage)
  img = img.convert("RGBA")
  datas = img.getdata()

  newData = []
  for item in datas:
      if item[0] == 255 and item[1] == 0 and item[2] == 0:
          newData.append((255, 255, 255, 0))
      else:
          newData.append((255, 0, 0, 255))
        
  img.putdata(newData)
  img.save('media/nextDetectron.png', "PNG")

  return 'media/nextDetectron.png'

def reversefotoDetectron2(diffimage):
  img = Image.open(diffimage)
  img = img.convert("RGBA")
  datas = img.getdata()

  newData = []
  for item in datas:
      if item[0] == 255 and item[1] == 0 and item[2] == 0:
          newData.append((255, 255, 255, 0))
      else:
          newData.append(item)
        
  img.putdata(newData)
  img.save('media/nextDetectron.png', "PNG")

  return 'media/nextDetectron.png'


def mergeDetectron(input_image_path,output_image_path,png_image_path,position):

    base_image = Image.open(input_image_path)
    png = Image.open(png_image_path)
    width, height = base_image.size

    transparent = Image.new('RGBA', (width, height), (0,0,0,0))
    transparent.paste(base_image, (0,0))
    transparent.paste(png, position, mask=png)
    if(output_image_path=='O.D.png'):
      transparent.show()
    transparent.save('media/'+output_image_path)

    return 'media/'+output_image_path



def change_detection2(request):

      
        file1=request.GET.get("inputfile")
        file2=request.GET.get("inputfile2")
        
        i1 = change_d()
        i1.img=file1
        i2 = change_d()
        i2.img=file2

        beforeimagename_wo_ext=os.path.splitext(file1)[0]
        afterimagename_wo_ext=os.path.splitext(file2)[0]
      
        beforeimagename=beforeimagename_wo_ext+'.jpg'
        afterimagename=afterimagename_wo_ext+'.jpg'
      
        diff_in_image=changedetection(beforeimagename,afterimagename_wo_ext)
      
        next=reversefoto(diff_in_image)
      
        next2=reversefotoa(next)
      
        merge(afterimagename, 'F&F '+afterimagename_wo_ext+'.png',next2, position=(0,0))
        
        i3 = change_d()
        i3.img='F&F '+afterimagename_wo_ext+'.png'

        return render(request,"change_detection_result.html",{'i1':i1,'i2':i2,'w':w,'h':h,'i3':i3,'diff_in_image':diff_in_image})




def reversefoto(diffimage):
  img = Image.open(diffimage)
  img = img.convert("RGBA")
  datas = img.getdata()

  newData = []
  for item in datas:
      if item[0] == 255 and item[1] == 0 and item[2] == 0:
          
          newData.append(item)
      else:
          newData.append((255, 255, 255, 0))
          
        
  img.putdata(newData)
  img.save('next'+diffimage, "PNG")

  return 'next'+diffimage


def merge(input_image_path,output_image_path,png_image_path,position):
    img=os.path.abspath(os.path.join(MEDIA_ROOT, input_image_path))
    base_image = Image.open(img)
    png = Image.open(png_image_path)
    width, height = base_image.size

    transparent = Image.new('RGBA', (width, height), (0,0,0,0))
    transparent.paste(base_image, (0,0))
    transparent.paste(png, position, mask=png)
    transparent.save('media/'+output_image_path)
    transparent.show() #to pop up changed detected image.

def changedetection(beforeimagename,afterimagename_wo_ext):
  f1=os.path.abspath(os.path.join(MEDIA_ROOT, beforeimagename))

  image1 = cv2.imread(f1)
  f2=os.path.abspath(os.path.join(MEDIA_ROOT, afterimagename_wo_ext+".jpg"))
  
  image2 = cv2.imread(f2)
  i1shape=round(image1.shape[1] / 4)
  if image1.shape[1] >= 1920 :
    
    image1 = cv2.resize(image1, ((round(image1.shape[1] / 4)), round(image1.shape[0] / 4))) 
    image2 = cv2.resize(image2, (round(image2.shape[1] / 4), round(image2.shape[0] / 4))) 
  difference = cv2.absdiff(image1, image2)
  # color the mask red
  Conv_hsv_Gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
  ret, mask = cv2.threshold(Conv_hsv_Gray, 0, 255,cv2.THRESH_BINARY_INV |cv2.THRESH_OTSU)

  difference[mask != 255] = [0, 0, 255]

  image1[mask != 255] = [0, 0, 255]
  image2[mask != 255] = [0, 0, 255]

  boundingBox = 10
  percent = 20

  rows, cols = (image1.shape[0]-boundingBox,image2.shape[1]-boundingBox) 
  for k in range(boundingBox,rows-boundingBox):#pixel
      for l in range(boundingBox,cols-boundingBox):#reddot
          if(difference[k][l][2] == 255):
              x=k-boundingBox
              y=l-boundingBox
              count = 0
              flg = False
              count2 = boundingBox*boundingBox*4
              for i in range(0,boundingBox*2):#boundbox
                  for j in range(0,boundingBox*2):#boundbox
                      if(difference[x+i][y+j][2] == 255):
                          count += 1

                          if(((count * 100) / count2) > percent):#percentage
                              flg = True
                              break

              if(flg == False):
                  for i in range(0,boundingBox*2):
                      for j in range(0,boundingBox*2):
                          difference[x+i][y+j][2] = 0
                          
  global w,h
  w=256
  h=256
  if difference.shape[1] == i1shape :
    w=600
    h=340
    difference = cv2.resize(difference,(round(difference.shape[1] * 4),round(difference.shape[0] * 4)))
  
  cv2.imwrite('media/diff in ' + afterimagename_wo_ext+'.png', difference)
  cv2.imwrite('diff in ' + afterimagename_wo_ext+'.png', difference)

  return 'diff in ' + afterimagename_wo_ext+'.png'


def reversefotoa(diffimage):
  img = Image.open(diffimage)
  img = img.convert("RGBA")
  datas = img.getdata()

  newData = []
  for item in datas:
      if item[0] == 255 and item[1] == 0 and item[2] == 0:
          newData.append((255, 0, 0, 99))
         
      else:
          newData.append((255, 255, 255, 0))
        
        
  img.putdata(newData)
  img.save('just'+diffimage, "PNG")

  return 'just'+diffimage

############### surva ###########################################################


def alerts(request):

    
        for file in request.FILES.getlist('myfile'):
                fs = FileSystemStorage()
                file1=file.name
                filename = fs.save(file.name, file)
                f1=os.path.abspath(os.path.join(MEDIA_ROOT, file1))


        i1 = change_d()
        i1.img=filename
     
        for file in request.FILES.getlist('myfile2'):
                fs2 = FileSystemStorage()
                file2=file.name
                filename2 = fs2.save(file.name, file)
                f2=os.path.abspath(os.path.join(MEDIA_ROOT, file2))

        i2 = change_d()
        i2.img=filename2
        print(os.path.splitext(file1)[0])
        beforeimagename_wo_ext=os.path.splitext(file1)[0]
        afterimagename_wo_ext=os.path.splitext(file2)[0]
      
        beforeimagename=beforeimagename_wo_ext+'.jpg'
        afterimagename=afterimagename_wo_ext+'.jpg'

        start = time.time()

        diff_in_image=changedetection(beforeimagename,afterimagename_wo_ext)

        next=reversefoto(diff_in_image)
        next2=reversefotoa(next)
        merge(afterimagename, 'F&F '+afterimagename_wo_ext+'.png',next2, position=(0,0))
        end = time.time()
        print('Time Required change:'+str(end - start))
        i3 = change_d()
        i3.img='F&F '+afterimagename_wo_ext+'.png'

        #################feature_ext2###########
        

        start = time.time()
        responsez = str(base64.b64encode(open('media/'+filename2,'rb').read()))
        responsez=responsez[2:]
        app_url = "http://13.68.181.120:5000/app/score-image"
        # app_url = "http://127.0.0.1:5000/app/score-image" #for localhost
        response = requests.post(app_url, json={"imageUrl":responsez, "mode": "0"})
        
        img=response.json()
        img=img[2:]
        fh =open('media/OutDetect.jpg',mode='wb')
        fh.write(base64.b64decode(img))

        
        next22=reversefotoDetectron('media/'+diff_in_image)
        
        output_image_path2=mergeDetectron('media/OutDetect.jpg', 'Some.png',next22, position=(0,0))
        next33=reversefotoDetectron2(output_image_path2)
        alt=mergeDetectron('media/'+filename2, 'O.D.png',next33, position=(0,0))
        end = time.time()
        print('Time Required:'+str(end - start))


        start = time.time()

        img = Image.open(alt)
        width, height = img.size
        if width >= 1920 :
          img = img.resize((round(width / 4 ),round(height / 4)))
        img = img.convert("RGBA")
        datas = img.getdata()

        newData = []
        building=False
        
        for item in datas:
            if (item[0]>222 and item[0]<251) and (item[1]>162 and item[1]<245) and (item[2]>40 and item[2]<145):
                
                building=True
                
            else:
              if building==True:
                break

              else:
                newData.append((255, 255, 255, 0))
                
                building=False

        end = time.time()
        print('Time Required:'+str(end - start)) 
   
        ima1=filename2
        ima2=filename

    
        return render(request,"surv_det.html",{'w':w,'h':h,'building':building})
        

