## Title
Medical Cost Prediction Using Machine Learning

### Problem Statement
Many people in the world don't take into account their health. They live their life anyhow they won't without thinking of what may happen to them or their loved ones. Will all these people be able to afford their medical costs in case something worse or bad happens to them in order to save their lives? the `AIM` of this project is to build a predictive model to help individuals predict their medical cost in case something bad happen to them. By doing so, individuals will start to advise themselves on how to live their lives.

### Objectives
* To collect dataset.
* Train model to predict medical charges.

### Functional Requirements
* Allow Access To Model API
* Predict and return medical charges

### Software Requirements
* Python3.10 packages

| Packages Names | Version Number |
| ---------------|--------------- |
| Pandas         | 0.23.4         |
| Numpy          | 1.15.1         |
| Matplotlib     | 2.2.3          |
| Seaborn        | 0.9.0          |
| Notebook       | 0.19.2         |
| Scikit Learn   | 5.6.0          |

* Vscode
* Docker / Dockerhub
* Azure CLI

### Hardware Requirements
* Ubuntu 22.04
* 16 Gig Ram
* 1 Terabyte HDD

### Machine Learning Algorithms Experimented With
* Linear Regression
* Random Forest Regressor
* Decision Tree
* SVM
* LightGBM
* xGBoost
* Ridge Regression
* Lasso Regression
* KNN

### Evaluation Metrics Used
* R Squared
* Mean Absolute Percentage Error
* Mean Squared Error

### Hyperpparameter Tuning Technique Used
* GridSearchCV
* RandomSearchCV

### Cloud Platform Used
* Microsoft Azure
* Azure DevOps

The model was deployed on `Microsoft Azure`. The diagram bellow is the cloud architecture on azure resources used to run the model.
![Cloud architecture diagram](./images/detailed.drawio.png)

### Azure Resources Used
* Resource Group
* Container App Environment
* Containerapp
* Log Analytics Workspace
* Storage Account
* Managed Identity

### Azure DevOps Resources Used
Yaml Pipeline
Repos
Board

The model was deployed to `Azure` using `Azure DevOps` CICD Yaml pipeline by building, testing and deploying. The diagram bellow represent how the model was released onto microsoft azure through azure devops yaml pipeline.
![Deploy model to azure](./images/deployment.png)

### Training Steps:
1. Retrieved Dataset.
2. Performed Exploratory Data Analysis.
3. Preprocess Dataset.
4. Build Base Model.
5. Evaluated Base Model
6. Perform Hyper-parameter Tuning.
7. Selected Best Model
8. Saved Model

The diagram bellow is a visual representation of how the entire model was built.
![How model was built](./images/model-lifecycle.png)

### Cost Involved
Since serverless technologies were used for the entire project life cycle, it cost **$ 0.00.**
| Azure Resource Name       | Price |
| --------------------------| ------|
| Container App             | $ 0.0 |
| Storage Account           | $ 0.0 |
| Log Analytics             | $ 0.0 |
| Resource Group            | $ 0.0 |
| Container App Environment | $ 0.0 |
| Total                     | $ 0.0 |
