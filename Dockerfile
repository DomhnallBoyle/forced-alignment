FROM ubuntu:18.04
MAINTAINER Domhnall Boyle {domhnallboyle@gmail.com}

ARG IP
ARG PORT
ENV IP ${IP}
ENV PORT ${PORT}

# core dependencies
RUN apt-get update && apt-get install -y \
    sox \
    gcc-multilib \
    python3 \
    python3-dev \
    python3-pip \
    git \
    vim \
    wget \
    curl \
    tar \
    zip

ENV HOME /app
WORKDIR $HOME
COPY . .

# install HTK 3.4
RUN tar -xvf htk.tar.gz
WORKDIR $HOME/htk
RUN ./configure --prefix=/usr/local --disable-hslab && make all && make install
WORKDIR $HOME

# check HTK installed properly
RUN tar -xvf htk-samples.tar.gz
WORKDIR $HOME/samples/HTKDemo
RUN mkdir accs hmms hmms/hmm.0 hmms/hmm.1 hmms/hmm.2 hmms/hmm.3 hmms/temp proto test
RUN ./runDemo configs/monPlainM1S1.dcf

# setup aliases
RUN ln -s $(which python3) /usr/bin/python
RUN ln -s $(which pip3) /usr/bin/pip

# install python dependencies
WORKDIR $HOME
RUN pip install -r requirements.txt

CMD python server.py --ip=${IP} --port=${PORT}

