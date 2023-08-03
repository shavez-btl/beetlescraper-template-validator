FROM public.ecr.aws/lambda/python:3.9
COPY . /validateApp
WORKDIR /validateApp

RUN yum -y install amazon-linux-extras
RUN PYTHON=python2 amazon-linux-extras install epel -y
RUN yum -y install chromium chromedriver
	
COPY . ${LAMBDA_TASK_ROOT}

RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
CMD ["handler.hello"]