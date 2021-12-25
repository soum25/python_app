<<<<<<< HEAD
FROM python:3.8-slim
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD ["python", "./main.py"]
>>>>>>> 527ab00488a7c072aa3ef12b19a24e0443ec37f9
