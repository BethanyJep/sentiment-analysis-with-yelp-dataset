# use the model in a flask app
import pickle

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# load the model
model = pickle.load(open('local models/model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def predict():
    # predict the rating based on the review
    if request.method == 'POST':
        text = request.form['text']
        my_prediction = model.predict([text])
        prediction = f'This is a {my_prediction} star review.'
    
        return render_template('result.html', prediction=prediction, text=text)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


