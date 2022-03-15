from bs4 import BeautifulSoup
import os
from urllib.request import urlopen
import shutil
import tempfile
import urllib.request

'''
def imagefiles(soup_var,user_url):
    Find all images and files and save to directory
    i=1
    user_url = input('Enter Directory Path ')

    if not os.path.exists(user_url):
        os.makedirs(user_url,mode = 777)
        os.chdir(user_url)
    else:
        if (os.path.exists(user_url)):
            tmp = tempfile.mktemp(directory=os.path.dirname(user_url))
            shutil.move(user_url, tmp)
            shutil.rmtree(tmp)
            os.makedirs(user_url)
            os.chdir(user_url)
            
    for img in soup_var.findAll('img'):
         try:
            temp=img.get('src')
            if temp[1:]=="C":
                image = user_url + temp
            else:
                image = temp

            nametemp = img.get('alt')
            if nametemp is None:
                filename=str(i)
                i=i+1
            else:
                filename=nametemp

            #print number of images with the images, add space after 
            print(image)
            print(f'Downloading file: {image}')
            print()
    
            imagefile = open(filename,'wb')
            imagefile.write(urlopen(image).read())
            imagefile.close()

         except urllib.error.HTTPError as err:
             print('404 Error - Couldnt Download Image')
             continue
         except ValueError:
            print('Unable to download file')
            continue
         except FileNotFoundError:
             print('File Not Found')
             continue
         

#https://youtu.be/m_agcM_ds1c
#code used
#imagefile = open(filename,'wb')
#imagefile.write(urlopen(image).read())
#imagefile.close()
'''
