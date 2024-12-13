# MLOps - ML System
*Patcharanat p.*

## Introduction
Starting an MLOps project is essential for organizations aiming to operationalize or productionize machine learning models to their own business. MLOps bridges the gap between data science and IT operations, ensuring that machine learning models are efficiently deployed, monitored, and maintained in a scalable production environment.

This project aims to introduce the implementation details of machine learning lifecycle management and deployment processes with sub-projects, emphasizing bringing AI to real-world applications over AI development techniques and researchs.

## Table of Contents
1. [Getting Started](#1-getting-started)
2. [Projects and Development](#2-projects-and-development)
3. [Conclusion](#3-conclusion)
4. [References](#4-references)

## 1. Getting Started
This repository contains multiple sub-projects related to MLOps practices (or data science and data engineering as required). Each project has their own comprehensive documentation focused on implementation rather than principles. You may find what to expect from each project in [2. Projects and Development](#2-projects-and-development) topic, and some note and research on MLOps in:
- [MLOps Note & Research](./docs/mlops_principle.md)

To run projects in this repository, it's required to have some relevant dependencies on runtime. It's recommended to use a separate python environment, such as *venv* for installing [requirements.txt](requirements.txt) located in the root working directory to be able to run all the sub-projects on your local machine.

1. Python Environment
    - In the root working directory, there's a [requirements.txt](requirements.txt) for development, containing python dependencies that are not all necessary in deployment. But instead, in each sub-directory will have a seperate `requirements.txt` for either setting up processses or containerization (if required) which is crucial for each project.
    - To automate setting up python virtual environment, use git bash on windows, Mac's terminal, or Linux CLI
        ```bash
        make venv

        source pyenv/Scripts/activate
        # for mac: source pyenv/script/bin/activate

        make install
        ```
    - To manually set python virtual environemnt for each project (avoid dependencies conflict)
        ```bash
        python -m venv pyenv
        # or python3, depends on your python installation in local machine

        source pyenv/Scripts/activate
        # for mac: source pyenv/script/bin/activate

        # (pyenv) TODO: replace with path to specific project
        pip install -r <project-directory/requirements.txt>
        ```
    - To reset python environment, please run this command:
        ```bash
        # delete 'pyenv' file
        make clean
        ```
2. Cloud Infrastructure Setting up
    
    Some sub-projects are required to set up cloud resources. We will utilize ***Terraform*** as much as possible to reduce manual configuration and enhance reproducibility. If the project is required, the Terraform folder will be located in it, intended to manage it as a resource group for each project.

## 2. Projects and Development
1. [MBTI-IPIP: Discover Your MBTI in 12 Questions with an ML Model Deployed via Streamlit on Azure Cloud Using Docker and Terraform CI/CD Pipelines](./mbti_ipip/README.md)
    - This sub-project emphasizes not only MLOps but also data science methodology. It covers initiating a problem, applying ML to address it, and wrangling and labeling data to meet the requirements. While MLOps practices, particularly ML model deployment, remain essential for delivering a functional web service, this is achieved using Docker containers, Streamlit, and Azure Web App Service.
    - In this sub-project, we achieved the following:
        - **Leveraged semi-supervised learning** to utilize simple Machine Learning algorithms effectively.
        - **Developed a containerized ML application** using Streamlit and Docker.
        - **Provisioned Azure cloud resources** for ML deployment with a Terraform remote backend.
        - **Deployed the ML application on Azure** using Azure Web App Service, Azure CLI, and CI/CD pipelines with Terraform.
    ![mbti_ipip_kmlops_overview](./mbti_ipip/docs/kmlops_overview.png)
    ![mbti_product1](./mbti_ipip/docs/mbti_product1.png)
    ![mbti_product2](./mbti_ipip/docs/mbti_product2.png)
2. *In progress. . .*

## 3. Conclusion
I expected this project to be my POC workspace or sandbox for MLOps practices, how AI/ML/DL can be deployed on production in either machine learning pipelines or model serving patterns aspects. Hopefully, this somehow could benefit anyone who shares the same learning path.

## 4. References
- [MLOps: Continuous delivery and automation pipelines in machine learning - Google Cloud](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning#top_of_page)
- [Machine Learning Operations - ml-ops.org](https://ml-ops.org/)