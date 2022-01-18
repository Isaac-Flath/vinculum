# docker build -t datapipeline -f ./Dockerfile ./

# docker run -it --ipc=host -v $PWD:/vinculum/data-pipeline datapipeline

FROM python:3.10.1-buster

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
	    build-essential \
		libssl-dev \
		libffi-dev \
		libpq-dev \
		python3-dev \
		openssh-client

COPY requirements.pip /vinculum/
RUN pip install -r /vinculum/requirements.pip

VOLUME /vinculum/data-pipeline

RUN mkdir -p /vinculum/logs

WORKDIR /vinculum/data-pipeline/src

CMD ["/bin/bash"]

# CMD [ "run-task" ]
