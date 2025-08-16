# sentiment_app.py
from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze sentiment of given text.
    Returns Positive, Negative or Neutral with emoji.
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # range: -1 (negative) → +1 (positive)

    if polarity > 0.1:
       sentiment = "Positive 😀"
    elif polarity < -0.1:
       sentiment = "Negative 😞"
    else:
       sentiment = "Neutral 😐"


if __name__ == "__main__":
    print("🔹 Sentiment Analysis Tool 🔹")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("Enter a sentence: ")
        if user_input.lower() == "quit":
            print("Exiting... Goodbye 👋")
            break

        result = analyze_sentiment(user_input)
        print(f"Sentiment: {result}\n")
