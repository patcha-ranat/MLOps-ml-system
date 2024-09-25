# MLOps Note & Research
*Patcharanat P.*

## Table of Contents
1. [Three Levels of ML Software](#1-three-levels-of-ml-software)
    1. [Data: Data Engineering Pipelines](#1-data-data-engineering-pipelines)
    2. [Model: Machine Learning Pipelines](#2-model-machine-learning-pipelines)
    3. [Code: Deployment Pipelines](#3-code-deployment-pipelines)
2. Model Performance Monitoring
3. Automate pipeline Re-training Model
4. CI/CD/CT (Continuous Training)
5. ML Deployment Strategies

## 1. Three Levels of ML Software
*https://ml-ops.org/content/three-levels-of-ml-software*

### 1. Data: Data Engineering Pipelines
- Data Ingestion
    - Data Sources
    - Metadata Catalog
- Exploration and Validation (EDA)
    - Use RAD tools: Using Jupyter notebooks is a good way to keep records of data exploration and experimentation.
    - Attribute Profiling:
        - Number of Records
        - Schema & Data Types
        - Numerical attr. profiling (min, max, avg, median)
        - Amount of missing values
        - Distribution
    - Label Attribute Identification
    - Data Visualization
    - Attributes Correlation
- Data Wrangling (Cleaning)
    - Transformations (Feature Engineering related)
    - Outliers
    - Missing Values
    - Not relevant Data: Drop the attributes that provide no useful information
- Data Splitting
    - Rule of thumb: 80% train set

### 2. Model: Machine Learning Pipelines
- Model Training
    - Feature Engineering
        - Discretize continuous features
        - Decompose features
        - Add transformations of features (e.g., log(x), sqrt(x), x2, etc.)
        - Aggregate features into promising new features
        - Feature Scaling
    - Model Engineering
        - ML model specification (code that creates an ML model) should be versioned
        - Train many ML models from different categories using standard parameters.
        - Measure and compare their performance. For each model, use N-fold cross-validation and compute the mean and standard deviation of the performance measure on the N folds.
        - Error Analysis: analyze the types of errors the ML models make.
        - Feature Selection
        - Identify the top three to five most promising models, preferring models that make different types of errors.
        - Hyperparameters tuning by using cross-validation. Random search for hyperparameters is preferred over grid search.
        - Consider Ensemble methods such as majority vote, bagging, boosting, or stacking, should produce better performance than running them individually.
- Model Evaluation
    - ensure it meets original business objectives before serving the ML model in production to the end-user.
- Model Testing
    - Model performance needs to be measured by using the hold-back test dataset to estimate the generalization error by performing the final “Model Acceptance Test”.
- Model Packaging
    - The process of exporting the final ML model into a specific format, *ML Model serialization formats*.
        - ML Model serialization formats
            - In order to achieve a distributable format, the ML model should be present and should be executable as an independent asset.
            - This means that the ML models should work outside of the model-training environment.
            - Language-agnostic exchange formats
                - Amalgamation
                - PMML
                - PFA
                - etc. [Source: Open Standard Models](https://github.com/adbreind/open-standard-models-2019)
            - Vendor-specific exchange formats
                - scikit-learn: `.pkl` as a pickle file
                - SparkML: MLeap file format (JAR for Java Runtime)
                - Tensorflow: `.pb` (protocol buffer)
                - PyTorch: `.pt`
                - Keras: `.h5`
                - etc. [ML Models training file formats](https://towardsdatascience.com/guide-to-file-formats-for-machine-learning-columnar-training-inferencing-and-the-feature-store-2e0c3d18d4f9)
- **Different forms of ML workflows**
    1. **ML Model Training**
        - **Offline Learning** *(aka batch / static learning)*
            - The model is trained on a set of already collected data.
            - After deploying to the production environment, the ML model remains constant until it re-trained because the model will see a lot of real-live data and becomes stale, this called "model decay".
        - **Online Learning** *(aka dynamic learning)*
            - The model is regularly being re-trained as new data arrives, e.g. as data streams.
    2. **ML Model Prediction**
        - **Batch Predictions**
            - The deployed ML model makes a set of predictions based on historical input data. This is often sufficient for data that is not time-dependent, or when it is not critical to obtain real-time predictions as output.
        - **Real-time Predictions** (aka on-demand predictions)
            - Predictions are generated in real-time using the input data that is available at the time of the request.
        - **Model Serving Pattern & Model Prediction Comparison**
            ![model-prediction-serving-pattern](https://ml-ops.org/img/model%20serving%20patterns.jpg)
            - **Offline Learning + Batch Prediction**
                - Forecast
                    - This type of machine learning workflow is widely spread in academic research or data science education.
                    - Usually, we take an available dataset, train the ML model, then run this model on another (mostly historical) data, and the ML model makes predictions.
                    - This ML workflow is not very useful and, therefore, not common in an industry setting for production systems
            - **Offline Learning + Real-time Prediction**
                - Microservices (Web-service) + REST API
                    - The web service takes input data and outputs a prediction for the input data points.
                    - The model is trained offline on historical data, but it uses real-live data to make predictions.
            - **Online Learning + Real-time Prediction**
                - Real-time streaming analytic
                    - The most dynamic way to embed machine learning into a production system is to implement online learning, which is also known as real-time streaming analytics.
                    - *Please note that online learning can be a confusing name because the core learning or ML model training is usually not performed on the live system. We should call it incremental learning; however, the term online learning is already established within the ML community.*
                    - In this type of ML workflow, the ML learning algorithm is continuously receiving a data stream, either as single data points or in small groups called mini-batches. The system learns about new data on the fly as it arrives, so the ML model is incrementally being re-trained with new data. This continually re-trained model is instantly available as a web service.
                    - Technically, this type of ML system works well with the lambda architecture in big data systems. Usually, the input data is a stream of events, and the ML model takes the data as it enters the system, provides predictions and re-learns on these new data. The model would typically run as a service on a Kubernetes cluster or similar.
                    - A big difficulty with the online learning system in production is that if bad data is entering the system, the ML model, as well as the whole system performance, will increasingly decline.
            - **Online Learning + Batch Prediction**
                - Automated ML
                    - An even more sophisticated version of online learning is automated machine learning or AutoML.
                    - AutoML promises training ML models with minimal effort and without machine learning expertise.
                    - The user needs to provide data, and the AutoML system automatically selects an ML algorithm, such as neural network architecture, and configures the selected algorithm.
                    - Instead of updating the model, we execute an entire ML model training pipeline in production that results in new models on the fly. ***For now, this is a very experimental way to implement ML workflows.***
    3. ML Model Type
        - type of machine learning algorithm such as supervised, unsupervised, semi-supervised, and Reinforcement Learning.

### 3. Code: Deployment Pipelines
1. **Model Serving** - The process of deploying the ML model in a production environment.
2. **Model Performance Monitoring** - The process of observing the ML model performance based on live and previously unseen data. In particular, we are interested in ML-specific signals, such as prediction deviation from previous model performance. These signals might be used as triggers for model re-training.
3. **Model Performance Logging** - Every inference request results in a log-record.

In the following, we discuss Model Serving Patterns and Model Deployment Strategies.
- Model Serving Patterns
    - Model serving is a way to integrate the ML model in a software system. Three components should be considered when we serve an ML model in a production environment. The *inference* is the process of getting data to be ingested by a model to *compute* predictions. This process requires ***a model***, ***an interpreter*** for the execution, and ***input data***.
    - Deploying an ML system to a production environment includes two aspects, first deploying the pipeline for automated retraining and ML model deployment. Second, providing the API for prediction on unseen data.
    - **Model-as-Service**
        - Model-as-Service is a common pattern for wrapping an ML model and the interpreter as an independent web service that applications can request through a REST API or consume as a gRPC service.
        ![model-as-service](https://ml-ops.org/img/model-as-service.jpg)
    - **Model-as-Dependency**
        - Model-as-Dependency is probably the most straightforward way to package an ML model. A packaged ML model is considered as a dependency within the software application.
        - For example, the application consumes the ML model like a conventional jar dependency by invoking the prediction method and passing the values.
        - The Model-as-Dependency approach is mostly used for implementing the Forecast pattern.
        ![model-as-dependency](https://ml-ops.org/img/model-as-dependency.jpg)
    - **Precompute Serving Pattern**
        - This type of ML model serving is tightly related to the Forecast ML workflow.
        - With the Precompute serving pattern, we use an already trained ML model and precompute the predictions for the incoming batch of data. The resulting predictions are persisted in the database.
        - We query the database to get the prediction result.
        ![precompute-serving-pattern](https://ml-ops.org/img/precompute-serving-pattern.jpg)
    - **Model-on-Demand**
        - The Model-on-Demand pattern also treats the ML model as a dependency that is available at runtime. This ML model, unlike the Model-as-Dependency, has its own release cycle and is published independently.
        - The message-broker architecture is typically used for such on-demand model serving.
        - We can imagine such architecture containing input- and output-queues. A message broker allows one process to write prediction-requests in an input queue. The event processor contains the model serving runtime and the ML model. This process connects to the broker, reads these requests in batch from the queue and sends them to the model to make the predictions. The model serving process runs the prediction generation on the input data and writes the resulted predictions to the output queue. Afterwards, the queued prediction results are pushed to the prediction service that initiated the prediction request.
        ![model-on-demand](https://ml-ops.org/img/model-on-demand.jpg)
    - **Hybrid-Serving (Federated Learning)**
        - It is unique in the way it does, there is not only one model that predicts the outcome, but there are also lots of it. Exactly spoken there are as many models as users exist.
        -  Let us start with the unique model, the one on the server. The model on the server-side is trained only once with the real-world data. It sets the initial model for each user. Also, it is a relatively general trained model so it fits for the majority of users.
        - On the other side, there are the user-side models, which are the real unique models. The devices will train their own highly specialized model for their own user. Once in a while, the devices send their already trained model data (not the personal data) to the server. There the server model will be adjusted, so the actual trends of the whole user community will be covered by the model. This model is set to be the new initial model that all devices are using.
        - The big benefit of this is that the data used for training and testing, which is highly personal, never leaves the devices while still capturing all data that is available. This way it is possible to train highly accurate models while not having to store tons of (probably personal) data in the cloud.
        - But there is no such thing as a free lunch, normal machine learning algorithms are built with homogeneously and large datasets on powerful hardware which is always available for training. With Federated Learning there are other circumstances, the mobile devices are less powerful, the training data is distributed across millions of devices and these are not always available for training.
        ![federated-learning](https://ml-ops.org/img/federated-learning.jpg)
- Deployment Strategies
    
    In the following, we discuss common ways for wrapping trained models as deployable services, namely deploying ML models as Docker Containers to Cloud Instances and as Serverless Functions.
    - Deploying ML Models as Docker Containers
        - As of now, there is no standard, open solution to ML model deployment. As ML model inference being considered stateless, lightweight, and idempotent, containerization becomes the de-facto standard for delivery.
        - One ubiquitous way is to package the whole ML tech stack (dependencies) and the code for ML model prediction into a Docker container. Then Kubernetes or an alternative (e.g. AWS Fargate) does the orchestration. The ML model functionality, such as prediction, is then available through a REST API (e.g. implemented as Flask application)
        ![infra-cloud](https://ml-ops.org/img/infra-cloud.jpg)
    - Deploying ML Models as Serverless Functions
        - Various cloud vendors already provide machine-learning platforms, and you can deploy your model with their services as serverless functions.
        - In order to deploy an ML model as a serverless function, the application code and dependencies are packaged into .zip files, with a single entry point function. This function then could be managed by major cloud providers such as Azure Functions, AWS Lambda, or Google Cloud Functions.
        - However, attention should be paid to possible constraints of the deployed artifacts such as the size of the artifact.
        ![infra-lambda](https://ml-ops.org/img/infra-lambda.jpg)

## 2. Model Performance Monitoring
*In progress*

## 3. Automate pipeline Re-training Model
*In progress*

## 4. CI/CD/CT (Continuous Training)
*In progress*

## 5. ML Deployment Strategies
*In progress*
- Blue/Green
- Shadow/Challenger
- Canary
- A/B
- Multi-Armed Bandits