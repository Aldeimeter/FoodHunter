FROM python:3.12

WORKDIR /app

COPY . .

ENV HOST_IP=0.0.0.0

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
