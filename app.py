from flask import Flask, request, render_template, jsonify
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pandas as pd

# Load your training data
data = pd.read_csv('all_data.csv')  
texts = data['text']  

# Fit the tokenizer on the training data
tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(texts)

# Load your pre-trained model
model_path = 'model.h5'  # Ensure this is the correct path to your model
model = tf.keras.models.load_model(model_path)

app = Flask(__name__)

def predict_sentiment(sentence):
    sequence = tokenizer.texts_to_sequences([sentence])
    padded_sequence = pad_sequences(sequence, maxlen=100)
    prediction = model.predict(padded_sequence)
    return float(prediction[0][0])  # Convert to standard float

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        sentence = data['message']
        sentiment_score = predict_sentiment(sentence)
        return jsonify({'prediction': f"{sentiment_score:.6f}"})  # Format the output to six decimal places
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
