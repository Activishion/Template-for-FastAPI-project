FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app


COPY requirements.txt .

RUN pip install --upgrade pip && pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .
    
CMD alembic upgrade head

RUN chmod a+x /app/docker/*.sh
