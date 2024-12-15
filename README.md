# Text Summarizer Project
This Text Summarizer Project aims to develop an advanced natural language processing (NLP) model capable of automatically generating concise and coherent summaries from large volumes of text using huggingface tranformers text summarizer api to get the text summaries as an output. The main motive to build this application is to understand how the transformer actually works and how we can use apis to get or list out the summary of the text data. This project is solely for the purpose of learning.

---

## Table of Contents
1. [Workflows](#workflows)
2. [Steps to run the project](#steps-to-run-the-project)
3. [AWS CI-CD Deployment using Github actions](#AWS-CI-CD-Deployment-using-Github-actions)

## Workflows
- Setup github repository
- Create README.md
- Create template.py
- Create setup.py
- Setup and install requirements.txt
- Setup Logging and Exception handling files
- Perform Data Ingestion
- Perform Data Transformation using Pipelines
- Perform Model Training and Model Evaluating Component
- Undergo Model Hyper Parameter Training
- Create Prediction Pipeline using FAST API
- Update config.yaml
- Update params.yaml
- Update entity
- Update the configuration manager in src config
- Update the components
- Update the pipeline
- Update the main.py
- Update the app.py

---

## Steps to run the project
Clone this project
```bash
git clone https://github.com/SwarnavaBanerjee24/text-summarizer
```

Create anaconda environment after cloning the repository
```bash
conda create -n venv python=3.8 -y
```
```bash
conda activate venv
```

Install the requirements
```bash
pip install -r requirements.txt
```

Run the application
```bash
python app.py
```

Open your local host and the port mentioned to use the app.

---

## AWS CI-CD Deployment using Github actions
### 1. Login to AWS Console
### 2. Create IAM user for deployment
We need two specific accesses:
1. EC2 Access: It is a virtual Machine
2. ECR: Elastic Container Registry, it is used to save docker file in aws.

These accesses can be given to a user with the help of the following two policies:
1. AmazonEC2ContainerRegistryFullAccess
2. AmazonEC2FullAccess

Steps to be followed for deployment:
1. Build docker image of the source code.
2. Push your docker image to ECR.
3. Launch Your EC2. 
4. Pull Your image from ECR in EC2.
5. Lauch your docker image in EC2.

### 3. Create ECR Repository to save docker image
905418328431.dkr.ecr.eu-north-1.amazonaws.com/text-summarizer

### 4. Create Ubuntu EC2 machine
### 5. Open EC2 and install Docker in EC2 Machine
Run the following commands
```bash
sudo apt-get update -y
sudo apt-get upgrade
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

### 6. Configure EC2 machine as a self-hosted runner
### 7. Setup Github secrets
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_REGION = eu-north-1
- AWS_ECR_LOGIN_URI = ec2-16-170-230-226.eu-north-1.compute.amazonaws.com
- ECR_REPOSITORY_NAME = text-summarizer
