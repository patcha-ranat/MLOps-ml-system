# MLOps - ML System
*patcharanat p.*

## Introduction
Starting an MLOps project is essential for organizations aiming to operationalize or productionize machine learning models to their own business. MLOps bridges the gap between data science and IT operations, ensuring that machine learning models are efficiently deployed, monitored, and maintained in a scalable production environment.

This project aims to introduce the detailed in implementation of machine learning life cycle management and deployment processes bringing AI to real-world applications over AI development techniques and AI research.

## Table of Contents
1. [Installation and Development](#1-installation-and-development)
2. [ML Workflows / Model Serving Pattern](#2-ml-workflows--model-serving-pattern)
3. Model Performance Monitoring
4. Automate pipeline Re-training Model
5. CI/CD/CT (Continuous Training)
6. ML Deployment Strategies
7. [Conclusion](#7-conclusion)
8. [References](#8-references)

<!-- 3. [Model Performance Monitoring](#3-model-performance-monitoring) -->
<!-- 4. [Automate pipeline Re-training Model](#4-automate-pipeline-re-training-model) -->
<!-- 5. [CI/CD/CT (Continuous Training)](#5-cicdct-continuous-training) -->
<!-- 6. [ML Deployment Strategies](#6-ml-deployment-strategies) -->

## 1. Installation and Development
1. Testing Environment
    - In root working directory, there's an [requirements.txt](requirements.txt) for development environment which will not be used in deployment. But in each sub-directory will have a seperated `requirements.txt` for packaging app to a docker container (if required) which is crucial for each application.
    - To use testing virtual environemnt, use git bash on windows, Mac's terminal, Linux
    ```bash
    python -m venv pyenv
    # or python3, depends on your python installation in local machine

    source pyenv/Scripts/activate
    # for mac: source pyenv/script/bin/activate

    # (pyenv)
    pip install -r requirements.txt
    ```
2. Cloud Setting up
    - TBC


## 2. ML Workflows / Model Serving Pattern
| Model Learning   | Static Learning (Offline)           | Dynamic Learning (Online)                     |
|------------------|-------------------------------------|-----------------------------------------------|
| **Model Prediction** | | |
| **Real-time Data (On-demand)**   | - Microservices                     | - Real-time Streaming Analysis                |
|                  | - REST API                          | - Online Learning                             |
| **Historical Data (Batch)** | - Forecast                          | - Automated ML Pipeline                       |
|                  | - Batch Prediction                  |                                               |

*Remark: More on [MLOps.org (Three Levels of ML Software)](https://ml-ops.org/content/three-levels-of-ml-software)*

### Relevant Projects
- Static Learning - On-demand Prediction
    - Microservices:
        - [mbti_ipip - Know your MBTI within 12 questions through ML model deployed with streamlit on Azure cloud](./mbti_ipip/README.md)
    - REST API
- Static Learning - Batch Prediction
    - Forecast
    - Batch Prediction
- Dynamic Learning - On-demand Prediction
    - Real-time Streaming Analysis
- Dynamic Learning - Batch Prediction
    - Automated ML Pipeline


## 3. Model Performance Monitoring
*In progress*

## 4. Automate pipeline Re-training Model
*In progress*

## 5. CI/CD/CT (Continuous Training)
*In progress*

## 6. ML Deployment Strategies
*In progress*
- Blue/Green
- Shadow/Challenger
- Canary
- A/B
- Multi-Armed Bandits

## 7. Conclusion
I expected this project to introduce MLOps practices of how AI/ML/DL can be deployed on production with automation either training pipelines or model serving services with different approaches. Hopefully, this somehow could give a sense to anyone who shares the same interest.

Me, who's deeply interested in this area of knowledge but might not be as expert as anyone who's been working on this area, hoping my inspiration and ambition contributed to this as an open source project could return me a learning curve and encourage any organization that finds AI important to them find this topic is also.

## 8. References
- [MLOps: Continuous delivery and automation pipelines in machine learning - Google Cloud](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning#top_of_page)
- [Machine Learning Operations - ml-ops.org](https://ml-ops.org/)