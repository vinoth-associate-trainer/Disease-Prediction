from flask import Flask, render_template, request

app = Flask(__name__)

# Function to predict disease based on input features
def predict_disease(height, weight, age, junk_food, occupation):
    # Replace this with your actual prediction code using a trained ML model
    # For demonstration, simply returning a fixed result
    # Assume that the prediction is based on whether the person is overweight or not
    if age > 40 and weight > 80:
        return "You are predicted to have a disease, You may be at risk for heart disease."

    if junk_food == "high":
        return " You may be at risk for digestive problems."

    if occupation == "working":
        return " You may be at risk for stress-related issues."
    else:
        return "You didn't have a diabetes issue."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user inputs from the form
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    age = int(request.form['age'])
    junk_food = request.form['junk_food']
    occupation = request.form['occupation']

    # Call the predict_disease function with user inputs
    prediction = predict_disease(height, weight, age, junk_food, occupation)

    # Render result template with prediction
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
