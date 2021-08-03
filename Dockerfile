FROM python:3.8

COPY main.py .

RUN pip install fastapi uvicorn opencv-python-headless urllib3 pytesseract numpy

EXPOSE 80



CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
