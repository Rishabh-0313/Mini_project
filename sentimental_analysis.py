import string

def sentiment_analysis(text):
    positive_words = ["good", "happy", "love", "excellent", "great", "amazing", "awesome", "fantastic", "wonderful", "joyful", "positive", "brilliant", "delightful", "favorable"]
    negative_words = ["bad", "sad", "hate", "terrible", "poor", "awful", "horrible", "disastrous", "depressing", "negative", "unpleasant", "disappointing", "miserable", "tragic", "unfortunate"]
    neutral_words = ["okay", "fine", "average", "decent", "mediocre", "neutral", "fair", "ordinary", "regular"]
    intensifiers = ["very", "extremely", "totally", "completely", "absolutely", "incredibly", "highly", "utterly", "particularly"]

    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = text.split()

    pos_count = 0
    neg_count = 0
    neutral_count = 0

    negation_words = ["not", "no", "never", "none"]

    for i, word in enumerate(words):
        if word in negation_words and i < len(words) - 1:
            next_word = words[i + 1]
            if next_word in positive_words:
                neg_count += 1
            elif next_word in negative_words:
                pos_count += 1
        elif word in intensifiers and i < len(words) - 1:
            next_word = words[i + 1]
            if next_word in positive_words:
                pos_count += 2
            elif next_word in negative_words:
                neg_count += 2
        elif word in positive_words:
            pos_count += 1
        elif word in negative_words:
            neg_count += 1
        elif word in neutral_words:
            neutral_count += 1

    if pos_count > neg_count:
        if neutral_count > 0:
            return "Mostly Positive with Neutral Elements"
        else:
            return "Positive"
    elif neg_count > pos_count:
        if neutral_count > 0:
            return "Mostly Negative with Neutral Elements"
        else:
            return "Negative"
    else:
        return "Neutral"

text = input("Enter a sentence: ")
print("Sentiment:", sentiment_analysis(text))