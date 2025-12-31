import gradio as gr
import requests

# URL of your backend. 
# LOCAL TESTING: "http://127.0.0.1:8000/predict"
# DEPLOYMENT: Replace with your Hugging Face Space URL, e.g., "https://username-space.hf.space/predict"
API_URL = "https://riva1205-midterm.hf.space/predict"

def analyze_sentiment(text):
    if not text:
        return "Please enter text."
    
    try:
        response = requests.post(API_URL, json={"text": text})
        if response.status_code == 200:
            data = response.json()
            return f"Sentiment: {data['label']}\nConfidence: {data['confidence']}"
        else:
            return f"Error: API returned status {response.status_code}"
    except Exception as e:
        return f"Connection Error: {str(e)}"

# Create GUI
iface = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(lines=5, placeholder="Type a movie review here..."),
    outputs="text",
    title="SentimentScope",
    description="A Machine Learning tool to detect positive or negative sentiment in reviews."
)

if __name__ == "__main__":
    iface.launch()