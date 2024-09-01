FROM python:3.10.6-slim

WORKDIR /app

ENV DOCKER_OPERATE=""

COPY /streamlit .

RUN pip install --no-cache -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "main_app.py", "--server.port=8501", "--server.address=0.0.0.0"]