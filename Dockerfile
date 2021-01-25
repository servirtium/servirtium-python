FROM python:3.9-slim
COPY servirtium/ servirtium/
COPY definitions.py .
COPY setup.py .
COPY requirements.txt .
COPY test/compatibility-suite.py .
WORKDIR /
RUN pip install -r requirements.txt
EXPOSE 61417
ENTRYPOINT ["python", "compatibility-suite.py"]
CMD ["record"]
# tODO record/playback & port args
