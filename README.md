# Loan Predictor

## About

- **Dataset Source**: The dataset used in this project is sourced from [Kaggle](https://www.kaggle.com/datasets/architsharma01/loan-approval-prediction-dataset). It provides valuable data for loan approval prediction.

- **Data Profiling**: For a comprehensive understanding of the dataset, we have conducted web-based data profiling using [ydata-profiling](https://rawgit.com/Mixim12/Loan_predictor/main/data_profiling.html). This profiling offers insights into the dataset's characteristics and helps in preprocessing and analysis.

## Features

- **Web-Based Interface**: The loan predictor comes with a user-friendly web interface powered by Flask, making it accessible through any modern web browser.

- **Pretrained Model**: The model utilized by the loan predictor is pretrained, ensuring accurate and efficient loan predictions without requiring users to train the model themselves.

- **Upgradable Model**: The PyTorch model is saved using the JIT (Just-In-Time) compilation feature. This means that you can easily upgrade the model without needing access to the main codebase. This flexibility allows for future improvements and enhancements to the prediction capabilities.

- **Docker Support**: The loan predictor is Docker-ready, allowing you to containerize and deploy it effortlessly. Docker ensures consistent and isolated environments, making it easy to run the predictor on various platforms.

These features make this loan predictor unique, user-friendly, and adaptable for continuous improvements and model upgrades.

## Table of Contents

- [Loan Predictor](#loan-predictor)
  - [About](#about)
  - [Features](#features)
  - [Table of Contents](#table-of-contents)
  - [Data](#data)
    - [Data features](#data-features)
    - [Data label](#data-label)
    - [Data preparation](#data-preparation)
  - [Getting Started](#getting-started)
    - [**Using it fromm the terminal**](#using-it-fromm-the-terminal)
    - [**Using it with docker**](#using-it-with-docker)
  - [Usage](#usage)
  - [Model Training](#model-training)
  - [Contributing](#contributing)
  - [Acknowledgments](#acknowledgments)

## Data

### Data features

- **loan_id**: A unique identifier for each loan application. (Categorical)
- **no_of_dependents**: The number of dependents of the loan applicant. (Numeric - Discrete)
- **education**: The education level of the loan applicant (e.g., "Graduate," "Not Graduate"). (Categorical)
- **self_employed**: Indicates whether the loan applicant is self-employed (e.g., "Yes," "No"). (Categorical)
- **income_annum**: The annual income of the loan applicant. (Numeric - Continuous)
- **loan_amount**: The requested loan amount. (Numeric - Continuous)
- **loan_term**: The duration of the loan in months. (Numeric - Discrete)
- **cibil_score**: The credit score of the loan applicant. (Numeric - Discrete)
- **residential_assets_value**: The value of residential assets owned by the loan applicant. (Numeric - Continuous)
- **commercial_assets_value**: The value of commercial assets owned by the loan applicant. (Numeric - Continuous)
- **luxury_assets_value**: The value of luxury assets owned by the loan applicant. (Numeric - Continuous)
- **bank_asset_value**: The total value of assets with the bank or financial institution. (Numeric - Continuous)

### Data label

- **loan_status**: The status of the loan application (e.g., "Approved," "Rejected"). This is the target variable you want to predict. (Categorical)

### Data preparation

The dataset presented an unusual issue where leading blank spaces were present in every string. To resolve this, I conducted a preprocessing step to remove these leading spaces.

Additionally, the loan_id column was removed from the dataset as it was deemed unnecessary for the analysis.

Next, I performed feature scaling on all the numeric features, scaling them to an interval of [0, 1]. I utilized a JSON file to store the maximum values of the dataset, which would later be used to scale input data from users effectively.

Finally, I saved the newly normalized dataset into a fresh CSV file for future use and analysis.

## Getting Started

### **Using it fromm the terminal**

```shell
git clone https://github.com/Mixim12/Loan_predictor
cd Loan_predictor
pip install -r requirements.txt
python3 python_app/main.py
```

### **Using it with docker**

## Usage

The program is running at <http://127.0.0.1:3000> or <http://192.168.1.145:3000>, connect using a browser or use POSTMAN with POST method at <http://127.0.0.1:3000/predict>.

## Model Training

## Contributing

## Acknowledgments
