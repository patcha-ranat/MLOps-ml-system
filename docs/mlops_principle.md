# MLOps Note & Research
*Patcharanat P.*

## Table of Contents
1. [Three Levels of ML Software](#1-three-levels-of-ml-software)
2. [ML Workflows / Model Serving Pattern](#2-ml-workflows--model-serving-pattern)
3. Model Performance Monitoring
4. Automate pipeline Re-training Model
5. CI/CD/CT (Continuous Training)
6. ML Deployment Strategies

## 1. Three Levels of ML Software
*https://ml-ops.org/content/three-levels-of-ml-software*
- Data: Data Engineering Pipelines
    - Data Ingestion
    - Exploration and Validation
    - Data Wrangling (Cleaning)
    - Data Splitting
- Model: Machine Learning Pipelines
    - Model Training
    - Model Evaluation
    - Model Testing
    - Model Packaging
    - Different forms of ML workflows
        - ML Model Training
        - ML Model Prediction
    - ML Model serialization formats
        - Language-agnostic exchange formats
        - Vendor-specific exchange formats
- Code: Deployment Pipelines
    - Model Serving Patterns
        - Model-as-Service
        - Model-as-Dependency
        - Precompute Serving Pattern
        - Model-on-Demand
        - Hybrid-Serving (Federated Learning)
    - Deployment Strategies
        - Deploying ML Models as Docker Containers
        - Deploying ML Models as Serverless Functions



## 2. ML Workflows / Model Serving Pattern
| Model Learning   | Static Learning (Offline)           | Dynamic Learning (Online)                     |
|------------------|-------------------------------------|-----------------------------------------------|
| **Model Prediction** | | |
| **Real-time Data (On-demand)**   | - Microservices                     | - Real-time Streaming Analysis                |
|                  | - REST API                          | - Online Learning                             |
| **Historical Data (Batch)** | - Forecast                          | - Automated ML Pipeline                       |
|                  | - Batch Prediction                  |                                               |

*Remark: More on [MLOps.org (Three Levels of ML Software)](https://ml-ops.org/content/three-levels-of-ml-software)*

- Static Learning - On-demand Prediction
    - Microservices
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