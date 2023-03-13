FROM python
RUN pip install requests python-hosts "python-socketio[client]"

COPY ./src /opt/src

WORKDIR /opt/src

ENTRYPOINT [ "python3", "/opt/src/app.py" ]
