FROM python:3.8-slim-buster


RUN apt-get update; \
    apt-get install -y software-properties-common; \
    apt-get install -y git \
    add-apt-repository ppa:mscore-ubuntu/mscore-stable; \
    apt-get update; \
    apt-get install -y musescore; \
    rm -rf /var/lib/apt/lists/* 
    		

RUN apt-get update && apt-get install -y git
RUN python -m pip install git+https://github.com/jaworiwanow/trop
RUN python -m pip install streamlit 
RUN python -m pip install music21


COPY ./EZPsaltica.TTF ./
RUN mkdir -p /usr/share/fonts/truetype/
RUN install -m644 EZPsaltica.TTF /usr/share/fonts/truetype/
RUN rm ./EZPsaltica.TTF

WORKDIR /app
ADD troparion .

EXPOSE 8501
ENTRYPOINT ["streamlit", "run"]
CMD ["troparion.py"]

