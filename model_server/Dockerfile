FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get install -y libgl1-mesa-glx

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
