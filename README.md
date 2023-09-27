# Loan Predictor

## The Loan Approval Predictor

The Loan Approval Predictor is a web-based application that simulates a loan verification process. It provides a user-friendly interface where users can input relevant data, and the system returns a verdict, either "Approved" or "Not Approved," indicating whether their loan application is likely to be accepted or rejected.

- **Dataset Source**: The dataset used in this project is sourced from [Kaggle](https://www.kaggle.com/datasets/architsharma01/loan-approval-prediction-dataset). It provides valuable data for loan approval prediction.

- **Data Profiling**: For a comprehensive understanding of the dataset, we have conducted web-based data profiling using [ydata-profiling](https://rawgit.com/Mixim12/Loan_predictor/main/data_profiling.html). This profiling offers insights into the dataset's characteristics and helps in preprocessing and analysis.

<a href="https://youtu.be/m85qxmrJwn4">
  <img src="python_app/templates/youtube_social_icon_red.png" alt="YouTube Logo" width="50" height="31" align="left">
  <h2 style="margin-left: 55px;"> Loan Approval Predictor Video</h3>
</a>

## Features

- **Web-Based Interface**: The loan predictor comes with a user-friendly web interface powered by Flask, making it accessible through any modern web browser.

- **Pretrained Model**: The model can be used as a pretrained model, ensuring accurate and efficient loan predictions without requiring users to train the model themselves.

- **Upgradable Model**: The PyTorch model is saved using the JIT (Just-In-Time) compilation feature. This means that you can easily upgrade the model without needing access to the main codebase. This flexibility allows for future improvements and enhancements to the prediction capabilities.

- **Docker Support**: The loan predictor is Docker-ready, allowing you to containerize and deploy it effortlessly. Docker ensures consistent and isolated environments, making it easy to run the predictor on various platforms.

These features make this loan predictor unique, user-friendly, and adaptable for continuous improvements and model upgrades.  

### Technologies Used

- Python
- PyTorch
- Flask
- Docker

## Table of Contents

- [Loan Predictor](#loan-predictor)
  - [The Loan Approval Predictor](#the-loan-approval-predictor)
  - [Features](#features)
    - [Technologies Used](#technologies-used)
  - [Table of Contents](#table-of-contents)
  - [Data](#data)
    - [Data features](#data-features)
    - [Data label](#data-label)
    - [Data preparation](#data-preparation)
  - [Getting Started](#getting-started)
    - [**Using it from the terminal**](#using-it-from-the-terminal)
    - [**Using it with docker**](#using-it-with-docker)
  - [Usage](#usage)
  - [Model Training](#model-training)
    - [Neural Network Summary](#neural-network-summary)
    - [Learning Rate Range Test](#learning-rate-range-test)
  - [Contribution](#contribution)
  - [License](#license)

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

### **Using it from the terminal**

```shell
git clone https://github.com/Mixim12/Loan_predictor
cd Loan_predictor
pip install -r requirements.txt
python3 python_app/main.py
```

### **Using it with docker**

```shell
docker build --platform linux/amd64 -t mixim12/loan_predictor:latest .
docker run -dp 0.0.0.0:3000:3000 mixim12/loan_predictor:latest
```

## Usage

The program is running at <http://127.0.0.1:3000> or <http://192.168.1.145:3000>, connect using a browser or use POSTMAN with POST method at <http://127.0.0.1:3000/predict>.

## Model Training

### Neural Network Summary

The neural network is designed for binary classification tasks and consists of the following components:

- **Input Layer**: Accepts input data of 11.

- **Hidden Layers**:
  - First Hidden Layer: 128 units with ReLU activation.
  - Second Hidden Layer: 32 units with ReLU activation.

- **Output Layer**: A single unit with a sigmoid activation function, producing output in the [0, 1] range.

- **Activation Functions**:
  - ReLU Activation: Applied in the first and second hidden layers to capture complex patterns in the data.
  - Sigmoid Activation: Used in the output layer for binary classification, providing probability-like outputs.

- **Loss Function**: Binary Cross-Entropy Loss (BCELoss) is used to compute the error between predicted and actual values, which is minimized during training.

- **Optimizer**: Adam optimizer is employed to update the network's weights and biases, optimizing the loss function during the training process.

- **Learning Rate Scheduler**: The OneCycleLR learning rate scheduler is utilized to dynamically adjust the learning rate during training. This technique helps in faster convergence and improved model performance.
  
### Learning Rate Range Test

- **Purpose**: Find the optimal learning rate for model training.
- **Benefits**: Improved model performance, resource efficiency, and training stability.
- **How It Works**: Define a range of learning rates, train the model, monitor losses, and visualize results.
- **Key Decision**: Choose the learning rate resulting in the steepest loss decrease.

## Contribution

Contributions to this project are welcome! Feel free to fork the repository, make improvements, and submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
