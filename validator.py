
def is_text_valid(text):
    keywords = ["room", "rate", "season", "check-in", "child"]
    return all(keyword in text.lower() for keyword in keywords)
