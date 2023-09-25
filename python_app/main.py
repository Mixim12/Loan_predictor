from flask import Flask, request, jsonify, render_template, session
import torch
import numpy as np
import pandas as pd
import json

app = Flask(__name__, template_folder="templates")

scaled_columns = [
    "income_annum",
    "loan_amount",
    "residential_assets_value",
    "commercial_assets_value",
    "luxury_assets_value",
    "bank_asset_value",
    "loan_term",
    "cibil_score",
]

with open("python_app/scaling_factors.json", "r") as file:
    scaling_factors = json.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST", "GET"])
def predict():
    # declare a variable to store the prediction
    prediction = 0.0
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    if request.method == "POST":
        if request.is_json:
            # Handle POST request with JSON data
            data_json = request.json['data']
            print("Incoming JSON data:", data_json)
            data_df = pd.DataFrame(data_json, index=[0])

            for column in scaled_columns:
                data_df[column] = data_df[column] / scaling_factors[column]

            input_tensor = torch.tensor(data_df.values.astype(np.float32)).to(device)

            torch_model = torch.jit.load('python_app/scripted_model.pt').to(device)
            torch_model.eval()

            with torch.no_grad():
                output_tensor = torch_model(input_tensor)

            prediction = output_tensor.item()
        else:
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            # Handle POST request with form data
            data = {
            'no_of_dependents': float(request.form['no_of_dependents']),
            'education': float(request.form['education']),
            'self_employed': float(request.form['self_employed']),
            'income_annum': float(request.form['income_annum']),
            'loan_amount': float(request.form['loan_amount']),
            'loan_term': float(request.form['loan_term']),
            'cibil_score': float(request.form['cibil_score']),
            'residential_assets_value': float(request.form['residential_assets_value']),
            'commercial_assets_value': float(request.form['commercial_assets_value']),
            'luxury_assets_value': float(request.form['luxury_assets_value']),
            'bank_asset_value': float(request.form['bank_asset_value'])
            }
            
            
            data_json = data
            print("Incoming JSON data:", data_json)
            data_df = pd.DataFrame(data_json, index=[0])
            
            loan_amount = int(data_df['loan_amount'].values[0])
            loan_term = int(data_df['loan_term'].values[0])
            
            for column in scaled_columns:
                data_df[column] = data_df[column] / scaling_factors[column]
                
            print(data_df)
            
            input_tensor = torch.tensor(data_df.values, dtype=torch.float32).to(device)

            torch_model = torch.jit.load('python_app/scripted_model.pt').to(device)
            
            torch_model.eval()
            with torch.no_grad():
                 output_tensor = torch_model(input_tensor)

            prediction = output_tensor.item()
            
            print(prediction)
            
            if prediction > 0.5:
                return render_template('approved_loan.html', loan_amount=loan_amount, loan_term=loan_term)
            else:
                return render_template('rejected_loan.html', loan_amount=loan_amount)
        
    
if __name__ == "__main__":
    app.run(debug=True)
