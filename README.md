# OCR-FastApi






Libraries required to install :


pip install fastpi

pip install opencv-python

pip install pytesseract ( for mac : brew install tesseract)

pip install urllib

pip install uvicorn


Docker Commands : 

docker build . -t ocr:latest

docker run -it -p 80:80 ocr:latest
