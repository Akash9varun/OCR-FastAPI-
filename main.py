from typing import Optional
from fastapi import FastAPI
import pytesseract
import numpy as np
import cv2
import urllib.request
from pydantic import BaseModel

app = FastAPI()

class DataModel(BaseModel):
    url:str

def url_to_image(url):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
	resp = urllib.request.urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	# return the image
	return image

@app.get('/')
def serverstatus():
    return {"status": "Running"}

@app.post("/text/")
def read_root(dm:DataModel):
    baseurl = dm.url
    image = url_to_image(baseurl)
    text = pytesseract.image_to_string(image)
    return { "result": text}
    

