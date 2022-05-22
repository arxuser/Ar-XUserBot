# We're using Ubuntu 20.10
FROM vckyouuu/geezprojects:buster

RUN git clone -b Ar-Xuserbot https://github.com/arxuser/Ar-XUserBot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/arxuser/Ar-XUserBot/Ar-XUserBot/requirements.txt

CMD ["python3","-m","userbot"]
