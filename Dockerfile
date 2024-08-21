FROM python

ADD main.py .

RUN pip install pyttsx3
RUN apt-get update
RUN apt-get install libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev -y
RUN pip install -r requirements.txt

CMD ["python", "./main.py"]