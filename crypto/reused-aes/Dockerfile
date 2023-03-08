FROM python:3.10-slim-buster

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -yqq xinetd
RUN pip install pycryptodome
RUN groupadd -r ctf && useradd -r -g ctf ctf

RUN echo '#!/bin/bash\n\
service xinetd restart && /bin/sleep infinity' > /etc/init.sh
RUN echo 'service ctf\n\
{\n\
  type = UNLISTED\n\
  disable = no\n\
  socket_type = stream\n\
  protocol = tcp\n\
  wait = no\n\
  user = ctf\n\
  bind = 0.0.0.0\n\
  port = 9999\n\
  server = /home/ctf/server.sh\n\
}' > /etc/xinetd.d/ctf
RUN chmod 500 /etc/init.sh
RUN chmod 444 /etc/xinetd.d/ctf
RUN chmod 1733 /tmp /var/tmp /dev/shm

WORKDIR /home/ctf
ADD distfiles/server.py .
RUN echo '#!/bin/bash\n\
FLAG=RTACTF{name_it_AES-SDGs} python /home/ctf/server.py' > server.sh
RUN chmod +440 server.py
RUN chmod +555 server.sh

RUN chown -R root:ctf /home/ctf
RUN service xinetd restart
