from selenium import webdriver
import time
import requests
import urllib.request
import cv2
import imutils

from bs4 import BeautifulSoup

from io import BytesIO
from io import StringIO
import sys
import os

from wand.image import Image
from wand.display import display

# Optional
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

opts = webdriver.ChromeOptions()
opts.headless = True

driver = webdriver.Chrome(options = opts)

# Change this URL to choose where to get the images (Does not work with gifs)
driver.get("https://www.reddit.com/r/dankmemes/top/?t=day")

time.sleep(6)
soup = BeautifulSoup(driver.page_source, 'html.parser')

memes = []

# Extract the memes
for img in soup.find_all("img"):
    if "https://i.redd.it" or "https://preview.redd.it/" in img['src']:
        if "https://www.redditstatic.com" not in img['src'] :
            if "https://styles.redditmedia.com" not in img['src']:
                if "https://preview.redd.it/award_images/" not in img['src']:
                    if "data:image/png;base64" not in img['src']:
                        memes.append(img['src'])
                    
bg = "bg.png"

def generate(index, index2):
    with Image(filename=bg) as bg_img:
        meme = urllib.request.urlopen(memes[index])
        with Image(file=meme) as meme1:
            
            # Resize the meme to fit in the background
            img = imutils.url_to_image(memes[index])
            h, w, c = img.shape
            if w >= 536:
                diff = w - 536
                w = w - diff
                
                percent = diff/536
                h = round(h* (1 - percent))
            elif w <= 536:
                diff = 536 - w 
                w = w + diff
            
                percent = diff/536
                h =  round(h*(percent +1))
                
            else:
                pass
            meme1.resize(w, h)
            bg_img.composite(meme1, left=100, top=100)
            
        meme.close() 
        meme = urllib.request.urlopen(memes[index2])
        with Image(file=meme) as meme2:
            
            img2 = imutils.url_to_image(memes[index2])
            h2, w2, c2 = img2.shape
            if w2 >= 536:
                diff = w2 - 536
                w2 = w2 - diff
            
                percent = diff/536
                h2 = round(h2* (1 - percent))
            elif w2 <= 536:
                diff = 536 - w2
                w2 = w2 + diff
            
                percent = diff/536
                h2 =  round(h2*(percent +1))
        
            else:
                pass
                
            meme2.resize(w, h)
            bg_img.composite(meme2, left=100, top=150 + h)
        
            
            # Add the logo
            with Image(filename="logo.png") as fg_img3:
                name = "meme" + str(index) + "+" + str(index2)
                
                bg_img.composite(fg_img3, left=10, top=0)
                print(os.getcwd())
                bg_img.save(filename= os.getcwd() +"\\images\\" + name + ".png")
                
                # Generate the video
                vrc = os.getcwd() + "\\images\\" +name+ ".png"
                frames = [vrc, vrc, vrc, vrc, vrc, vrc, vrc, vrc, vrc]
                video = cv2.VideoWriter(os.getcwd() + "\\videos\\" + name + ".avi", 0, 1, frameSize=(736, 1308))
                for frame in frames:
                    video.write(cv2.imread(frame))
                    
                cv2.destroyAllWindows()
                os.system('cmd /k "ffmpeg -i videos/' + name + '.avi -i Buttercup.mp3 -c copy -map 0:v:0 -map 1:a:0 upload/' + name + '.avi"')
                

if sys.argv[1]:
    if sys.argv[2]:
        generate(int(sys.argv[1]),int(sys.argv[2]))
else:
    print("Enter what memes you want, starting from index 0")

