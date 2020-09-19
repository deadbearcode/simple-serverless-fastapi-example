# Simple Serverless FastAPI Example

A simple serverless [FastAPI](https://fastapi.tiangolo.com/) application using [Mangum](https://pypi.org/project/mangum/) to run on an AWS [Lambda](https://aws.amazon.com/lambda/).

## Complete Walkthrough

### [Simple Serverless FastAPI with AWS Lambda Complete Walkthrough](https://deadbearcode.com/simple-serverless-fastapi-with-aws-lambda/)


### [Serverless FastAPI CICD with CircleCi Complete Walkthrough](https://deadbearcode.com/serverless-fastapi-cicd-circleci/)

## Installation

### Setup Virtual Environment

```shell
virtualenv -p python3.7 env
source ./env/bin/activate
```

### Install Dependencies

```shell
pip install -r requirements.txt
```

## Run the application

```shell
uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
```

## Deploy

### Package Dependencies

```shell
cd env/lib/python3.7/site-packages
zip -r9 /path/to/root/function.zip
```

### Package Lambda

```shell
cd /path/to/root
zip -g function.zip lambda_function.py
```
