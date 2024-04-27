## Language Detector
Language Detector is a tool developed with FastAPI to accurately detect the language of text input. It utilizes the Multinomial Naive Bayes (MultinomialNB) algorithm for classification.

## Install Dependencies
pip install -r requirements.txt

## Run the FastAPI Server
uvicorn main:app --port 8000

## Access the API Endpoint
Open your web browser and navigate to http://localhost:8000/detect. Send a POST request to this endpoint with the input text as a string in the request body.Input Schema:\
{
    "text": "Your text input here"
}

