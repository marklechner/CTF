FROM alpine
RUN adduser -D gavin
RUN apk update && apk add --no-cache --update python3
COPY . /configparser
WORKDIR /configparser
RUN pip3 install -r requirements.txt
RUN chown -R gavin /configparser && chmod 755 /configparser/app.py
EXPOSE 5300
CMD ["su", "-", "gavin", "-c", "/configparser/app.py"]
