# MBTI - IPIP
*Know your MBTI within 12 questions through ML model deployed with streamlit on Azure cloud*

*patcharanat p.*

***Non-commercial Project***

## Introduction

Taking nearly 100 questions to know your MBTI could take a lot of time. How about knowing your MBTI within 12 questions? predicted by Machine Learning deployed with Streamlit on Azure Cloud.

## Table of Contents

1. [Getting Started](#1-getting-started)
2. [Model Development](#2-model-development)
3. [Authentication](#3-authentication)
4. [Deployment](#4-deployment)
5. [Appendix](#5-appendix)
    - [About Dataset](#about-dataset)
    - [Mapping Personalities IPIP to MBTI](#mapping-personalities-ipip-to-mbti)
    - [MBTI Contents](#mbti-contents)

## Prerequisites

- Python
- Microsoft Azure with available subscription
- Azure CLI SDK (`az`)
- Docker Hub Account
- Terraform (+Set to `$PATH`)
- Add the following file:
    - `./mbti_ipip/terraform/terraform.tfvars`
        ```shell
        subscription_id = "XXX-XXX-XXX-XXX-XXX"
        client_id = "XXX-XXX-XXX-XXX-XXX"
        client_secret = "XXXXXXXXXX"
        tenant_id = "XXX-XXX-XXX-XXX-XXX"

        location = "XXXX XXX"
        ```
        - Please refer to [3. Authentication](#3-authentication) for more details.

## 1. Getting Started

This sub-project is quite focused on data science methodology, including initiating a problem, how we use ML to solve the problem, and how we wrangle and label the data to meet the requirement. Even though MLOps practices, especially ML model deployment, still play a crucial role to deliver developed ML as an usable product as a web service with docker container, streamlit, and Azure cloud Web App service.

- Core component for the project consist of:
    - [Dockerfile](Dockerfile)
        - containerize ML application.
    - streamlit/[requirements.txt](./streamlit/requirements.txt)
        - dependency of the application required in the container.
    - streamlit/[main_app.py](./streamlit/main_app.py)
        - Streamlit App (Web-based UI)
    - streamlit/models/*
        - Contained ML model, Encoder/Decoder, and list of input questions used in Streamlit App
    - streamlit/mbti_info/*
        - Contained application's text contents
    - streamlit/picture/*
        - Contained application's picture contents
    - terrform/*
        - Code for deployment on cloud
- To run application locally for development, demo or testing, please enable `pyenv` in root working directory before and then run this:
    ```bash
    # workdir .
    streamlit run mbti_ipip/streamlit/main_app.py
    ```

## 2. Model Development
- Overall Process
![mbti_overall_process](./docs/mbti_overall_process.png)
- Overview Architecture
![mbti_architecture_overview](./docs/mbti_architecture_overview.png)
- Development Notebook
    - [ML-Sandbax - mbti_ipip - GitHub patcha-ranat](https://github.com/patcha-ranat/ML-Sandbox/blob/main/mbti_ipip/model_dev.ipynb)
- Output
![mbti_product1](./docs/mbti_product1.png)
![mbti_product2](./docs/mbti_product2.png)

## 3. Authentication

In Azure Cloud, there are multiple authentication methods that you can choose to match your specific needs such as Service Principal, Managed Identity, and etc. However, I will use Service Principal with Client Secret which is the most easiest to implement, but still being in the overall common practices. 

***Service Principal*** (SP) is similar to *Service Account* in GCP. It's intended to have least permissions to interact with a resource according to security purpose. We will enable SP for provisioning cloud resources through either Terraform or CLI. To create SP, you can achieve it through Azure Portal (Web UI) or through Azure CLI (`az`).

### 1. Creating Service Principal with Azure CLI
- first we'll need to login through `az`

    ```bash
    az login

    az account set --subscription "subscription_id"

    # check result -- attribute `id` is your subscription_id for owner account
    az account list
    ```

    *Please, note that you may encounter difficulty in authenticating Azure with Git Bash. Switching terminal type to powershell, Ubuntu, etc. for authentication first, and then switching back to Git Bash is worked for me (output from `az login` is shared within host machine regardless of terminal type or session)*

    ```bash
    az ad sp create-for-rbac \
        --display-name kmlops-sp \
        --role Contributor \
        --scopes subscriptions/<subscription_id>(/<optional>)
    ```
- Please, note that you can specify more of `--scopes` after subscription to make SP having lesser permission specific to resources which is a better practice.
- It will give output as:
    ```json
    {
        "appId": "REDACTED", // client id
        "displayName": "sp-display-name",
        "password": "REDACTED", // client secret
        "tenant": "REDACTED" // tenant id
    }
    ```
- We will futher use this output either in Terraform or CLI for account impersonation

### 2. Creating Service Principal with Azure Portal
- Creating SP
    - `Microsoft Entra ID (formerly Azure Active Directory (Azure AD))` >> `App registrations` >> *create SP*
    - `App registrations` >> newly created SP >> `Certificates & secrets`
        - You can get `client ID`, `tenant ID` in SP page within `App registrations`.
        - In `Certificates & secrets` >> `New client secret` >> *get Secret **Value** for client secret*.
- Grant Role
    - `Bill access control (IAM)` >> `Access control (IAM)` >> *Add, choose Contributor Role and search your SP with display-name*

As GCP-familiar data engineer, I find this part frustrating by non beginner-friendly documentation and inconsistent cloud service names which make it much more harder to explore and search for information. Please refer to this [thread](https://stackoverflow.com/a/72483319) for more detail on App registrations and Service Principle.

References:
- [Demystifying Service Principals – Managed Identities - Dev Blogs Microsoft](https://devblogs.microsoft.com/devops/demystifying-service-principals-managed-identities/)
- [What is Azure Service Principal? - Stack Overflow](https://stackoverflow.com/a/48105935)
- [Creating SP via Azure Portal - Microsoft Official Documentation](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal)
- [Azure Provider: Authenticating using a Service Principal with a Client Secret - Terraform Official Documentation](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/service_principal_client_secret.html)
- [Create an Azure service principal with Azure CLI - Microsoft Official Documentation](https://learn.microsoft.com/en-us/cli/azure/azure-cli-sp-tutorial-1?tabs=bash)
- [az ad sp create for rbac - Microsoft Official Documentation](https://learn.microsoft.com/en-us/cli/azure/ad/sp?view=azure-cli-latest#az-ad-sp-create-for-rbac)

## 4. Deployment

I included 2 approaches of deployment in this sub-project:
1. Azure CLI and CI/CD Pipeline
2. Terraform and CI/CD Pipeline

### 4.1 Azure CLI and CI/CD Pipeline

We have to create docker hub repo first via Docker Hub Web UI before proceeding to the next step. You might also need to change some variables to match your case.

#### 4.1.1 Recheck Image Result

Before we push the image to public/private registry, we should always check content contained in the image if it's not sensitive, safe to be deployed or not, and also check if the image works properly as expected. 

```bash
# workdir: .

# docker build -t <image-name>:<tag> <dockerfile-location-relative-to-current-workdir>
docker build -t <image-name>:<tag> mbti_ipip/.

# test running on local
docker run -p 8501:8501 <image-name>:<tag>

# check http://localhost:8501

# check files inside the container while running
docker exec -it <container-id> bash

# check for sensitive content contained in the container by overriding image entrypoint
docker run -it --entrypoint bash <image-name>:<tag>

docker stop <container-id>
```

#### 4.1.2 Build

You may need to authenticate first for Docker Hub

```bash
docker login
```
```bash
# workdir: .

# docker build -t <image-name>:<tag> <dockerfile-location-relative-to-current-workdir>
docker build -t <image-name>:<tag> mbti_ipip/.

# Rename image
docker tag <image-name>:<tag> <dockerhub-username>/<repo-name>:<tag>

# Push to Docker Hub
docker push <dockerhub-username>/<repo-name>:<tag>
```

- In before revised version, I configure Azure app service in Azure cloud manually. please refer to references below to deploy on cloud as online application through Azure Web UI (Azure Portal).
- To prepare Streamlit app for production, you can find more details at [Official Documentation from Streamlit](https://docs.streamlit.io/deploy/tutorials/docker)

References:
- [Pushing Docker Image to Docker Hub - Youtube - Shaw Talebi](https://youtu.be/pJ_nCklQ65w?si=C0T-OnEd_BbAvsdV&t=1035)
- [How to deploy and test docker container websites using Azure app service - Youtube - LetMeTechYou](https://youtu.be/Fl9AIKj8UAY?si=hnUq7S4ut8v7-zEj&t=228)

#### 4.1.3 Deploy

- First We'll need to login with newly created SP:
    ```bash
    az login \
        --service-principal \
        -u <client-id> \
        -p <client-secret> \
        --tenant <tenant-id>

    # you should see servicePrincipal type
    az account list
    ```
- resource group
    ```bash
    az group create \
        --name <resource-group-name> \
        --location <location>
    # az group delete --name <resource-group-name>
    ```
- app service plan
    ```bash
    az appservice plan create \
        -g <resource-group-name> \
        -n <app-service-plan-name> \
        --is-linux \
        --sku F1 \ # cluster type
        --location <location>
    # az appservice plan delete --name <app-service-plan-name> --resource-group <resource-group-name>
    ```
- webapp
    ```bash
    # for docker hub public repo
    az webapp create \
        --name <web-app-name-or-url-domain> \
        --resource-group <resource-group-name> \
        --plan <app-service-plan-name> \
        -i <namespace>/<repo-name>:<tag>

    # for docker hub private repo
    az webapp create \
        --name <web-app-name-or-url-domain> \
        --resource-group <resource-group-name> \
        --plan <app-service-plan-name> \
        -i <namespace>/<repo-name>:<tag> \
        --container-registry-user <docker-email> \
        --container-registry-password <docker-password>
    
    # az webapp delete --name <web-app-name-or-url-domain> --resource-group <resource-group-name>
    ```

Now you can access your ML App through `<web-app-name>.azurewebsites.net` URL

Note
- For Azure, you can find list of available region/location here:
    - https://learn.microsoft.com/th-th/industry/sustainability/sustainability-data-solutions-fabric/deploy-availability
    - https://www.azurespeed.com/Information/AzureRegions

References:
- [Manage Azure Resource Groups by using Azure CLI - Microsoft Official Documentation](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-cli)
- [Azure CLI az appservice plan - Microsoft Official Documentation](https://learn.microsoft.com/en-us/cli/azure/appservice/plan?view=azure-cli-latest)
- [Azure CLI az webapp create - Microsoft Official Documentation](https://learn.microsoft.com/en-us/cli/azure/webapp?view=azure-cli-latest#az-webapp-create)

#### 4.1.4 CLI and CI/CD Pipeline

For CI/CD Pipeline, there is an only file related to this topic:
- [ipip-mbti-build-deploy.yml](../.github/workflows/ipip-mbti-build-deploy.yml)

The file operated with the same steps as manual execution in the previous topic, but with GitHub Action Runner:
1. Build
    1. Login to Docker Hub
    2. Build image from the GitHub repo with specified Dockerfile path
    3. Push built image to specified repo (public/private)
4. Deploy
    1. Login to Azure
    2. Deploy Web App with specified image version
    3. Echo result such as App URL, image repo, image version
    4. Azure logout

Anyway, there're some point worth noting:
- We have to manually deploy Web App first time before deploying through CI/CD Pipeline because it requires some resources to be pre-exist which are resource group, App Service Plan, and Web App first version.
- To authenticate with *Azure Login action*, we need to specify GitHub Action secret: `AZURE_CREDENTIALS` manually with these attributes:
    ```json
    {
        "clientSecret": "REDACTED", // client secret
        "subscriptionId": "REDACTED", // subscription id
        "tenantId": "REDACTED", // tenant id
        "clientId": "REDACTED" // client id
    }
    ```
    - Please note that `--sdk-auth` is deprecated and `--json-auth` is not worked as expected for me. So, manual creating this json is required.
- Everytime we deploy a newer image version, it will change existing web app resource with the same specified app name to use the newer version.
- ***Managed Identity*** in Azure Cloud use `client-id`, `tenant-id`, `subscription-id`, and additional setup to avoid storing long-lived credentials (so, no `client secret`) for authentication. Please, refer to references below for more details *(Azure Login Action)*.

References:
- [Deploy a custom container to App Service using GitHub Actions - Microsoft Official Documentation](https://learn.microsoft.com/en-us/azure/app-service/deploy-container-github-action?tabs=service-principal)
- [Docker Build GitHub Actions - dockerdocs](https://docs.docker.com/build/ci/github-actions/)
- [Azure Login Action - Azure GitHub](https://github.com/Azure/login?tab=readme-ov-file#azure-login-action)

Although using CI/CD Pipeline with CLI commands for deployment is simple and easy to setup, there're some drawback in this approach such as:
1. It required some resources to be manually provisioned before automated deployment.
2. Cloud resources can't be versioning lead to unable to track changes and it's more harder to monitor cloud resources properties without representing in code.

For enterprise-scale projects or projects that intensively operate on the cloud, I think it's more appropriate to adopt *Terraform* in architecture dedicated to more mature deployment, even it have the same level of rollback capability.

### 4.2 Azure Terraform and CI/CD Pipeline

In this section I will utlize **Terraform** to automate (or manual) Azure web service deployment.

#### 4.2.1 Build

#### 4.2.2 Deploy

#### 4.2.3 Terraform and CI/CD Pipeline

#### References:
- [Terraform Azure Authentication (CLI) - Official Terraform Docs](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/azure_cli)
- [Linux Web App Terraform - Official Terraform Docs](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/linux_web_app#example-usage)
- [Terraform create app service for linux container - Stack Overflow](https://stackoverflow.com/a/75997774)
- [Create App Service app using a Terraform template - Microsoft Official Documentation](https://learn.microsoft.com/en-us/azure/app-service/provision-resource-terraform)

## 5. Appendix
### About Dataset
- [Big Five Personality Test - Kaggle](https://www.kaggle.com/datasets/tunguz/big-five-personality-test)
- [Local Data Dict](./data/codebook.txt)
- [International Personality Item Pool](https://ipip.ori.org/)
- [Converting IPIP Item Responses to Scale Scores](https://ipip.ori.org/newScoringInstructions.htm)
- [Big-Five Factor Markers - Questions Classification](https://ipip.ori.org/newBigFive5broadKey.htm)
- [Interpreting Individual IPIP Scale Scores](https://ipip.ori.org/InterpretingIndividualIPIPScaleScores.htm)
- [MBTI - Letters personalities explain](https://www.16personalities.com/articles/our-theory)

### Mapping Personalities IPIP to MBTI
- Factor I (EXT questions)
    - Surgency or Extraversion = Introversion or Extroversion (I/E)
- Factor II (AGR questions)
    - Agreeableness = Thinking or Feeling (T/F)
- Factor III (CSN questions)
    - Conscientiousness = Judging and Perception (J/P)
- Factor IV (EST questions)
    - Emotional Stability = Turbulance or Assertive (T/A)
- Factor V (OPN questions)
    - Intellect or Imagination = Sensors or Intuitives (S/N)

---
