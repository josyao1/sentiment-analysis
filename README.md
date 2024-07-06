### Project Title: Sentiment Analysis Web Application

#### Description
This project is a web application that allows users to input a sentence and receive a sentiment analysis score in return. The sentiment score ranges from 0 to 1, indicating how positive the sentence is. The application uses a pre-trained model to predict the sentiment and is built using Flask for the backend and HTML/CSS for the frontend.

#### Features
- User-friendly web interface for inputting sentences.
- Real-time sentiment analysis based on user input.
- Model trained on a dataset with 5000 most frequent words.
- Sentiment score formatted to six decimal places for clarity.

#### Project Structure
```
sentiment_analysis/
│
├── app.py
├── model.h5
├── static/
│   └── (optional static files like CSS, JS, favicon, etc.)
├── templates/
│   └── index.html
├── all_data.csv
├── tokenizer.pickle (optional, if saved)
└── README.md
```

#### Requirements
- Python 3.x
- Flask
- TensorFlow
- pandas

#### Setup Instructions
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/sentiment_analysis.git
   cd sentiment_analysis
   ```

2. **Install the Required Libraries**
   ```bash
   pip install -r requirements.txt
   ```
   Ensure your `requirements.txt` includes:
   ```
   Flask
   tensorflow
   pandas
   ```

3. **Place the Model and Data Files**
   - Ensure `model.h5` is in the project directory.
   - Ensure `all_data.csv` is in the project directory.

4. **Run the Flask Application**
   ```bash
   python app.py
   ```

5. **Access the Application**
   Open your web browser and navigate to `http://127.0.0.1:5000/`.

#### How It Works
- **Data Loading and Tokenizer Fitting**: The application loads the training data from `all_data.csv` and fits the tokenizer on the text data. This ensures that the input text for prediction is processed in the same way as during model training.
- **Model Loading**: The pre-trained model is loaded from `model.h5`.
- **Prediction Function**: The `predict_sentiment` function processes the input sentence, converts it to sequences, pads it, and uses the model to predict the sentiment score.
- **Web Interface**: Users can input a sentence on the web page and receive a sentiment score after clicking the "Analyze Sentiment" button.

#### Example Usage
1. Open the web application in your browser.
2. Enter a sentence in the text area, e.g., "I am having a great day".
3. Click "Analyze Sentiment".
4. The sentiment score will be displayed below the button.

#### Troubleshooting
- **Model Not Loading**: Ensure the `model.h5` file is correctly placed in the project directory.
- **Tokenizer Issues**: Make sure the tokenizer is fitted on the same training data used during model training.
- **Server Errors**: Check the terminal for error logs and ensure all dependencies are installed.

#### Future Enhancements
- Add more sophisticated error handling and user feedback.
- Implement additional preprocessing steps for input text.
- Improve the model by training on a larger and more diverse dataset.
