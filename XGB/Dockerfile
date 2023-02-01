FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# CMD ["python", "main.py"]
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


# docker build -t rfr .   
# docker run -p 8001:8001 rfr