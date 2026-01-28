import re
import random

# Toggle this to True to show detected emotions (for demo)
DEBUG = True

# Predefined intents and responses
responses = {
    "greetings": [
        "Hello! How can I assist you today?",
        "Hi there! Ready to chat?",
        "Hey! What’s up?",
        "Greetings! How’s your day going?"
    ],
    "help": [
        "I can respond to greetings, small talk, jokes, and emotions.",
        "Try typing: hello, how are you, joke, or exit.",
        "I'm here to chat whenever you need."
    ],
    "happy_help": [
        "I see you are in a good mood and want help — let's make it fun! 😄",
        "Happy to assist! Ask away and let's keep the energy positive!",
        "Your positivity is great! How can I help you today?"
    ],
    "bot_identity": [
        "I’m a rule-based chatbot, not a human.",
        "I’m a bot created to chat, not a real person.",
        "I don’t have feelings, but I can respond intelligently."
    ],
    "joke": [
        "Why did the computer show up late? It had a hard drive!",
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the developer go broke? He used up all his cache!"
    ],
    "small_talk": [
        "I'm doing great for a bunch of code!",
        "Just chatting and processing words 😄",
        "All systems running smoothly!",
        "Life is good in binary."
    ],
    "happy": [
        "That’s awesome to hear! 😊",
        "Your good mood is contagious!",
        "Love that energy!"
    ],
    "sad": [
        "I’m here if you want to talk.",
        "That sounds tough. You’re not alone.",
        "Sending some positive vibes your way 💛"
    ],
    "angry": [
        "Take a breath. Things will settle.",
        "I get that frustration happens.",
        "Let’s slow things down for a moment."
    ],
    "default": [
        "Interesting… tell me more.",
        "I didn’t fully get that. Can you rephrase?",
        "I’m listening."
    ],
    "fallback": [
        "I may not be trained for that topic.",
        "That seems outside my current knowledge.",
        "I’m still learning. Try asking something simpler."
    ],
    "personal_refusal": [
        "I’m not supposed to answer personal questions.",
        "I can’t discuss personal or private topics.",
        "I’m a chatbot, so I avoid personal questions."
    ],
    "exit": [
        "Goodbye! Take care.",
        "See you next time!",
        "Chat ended. Have a great day!"
    ]
}

# Detect emotion from keywords
def detect_emotion(text):
    if any(word in text for word in ["happy", "great", "awesome", "good"]):
        return "happy"
    if any(word in text for word in ["sad", "down", "bad", "lonely"]):
        return "sad"
    if any(word in text for word in ["angry", "mad", "frustrated"]):
        return "angry"
    return None

# Determine chatbot response
def chatbot_response(user_input):
    text = user_input.lower()

    # Exit
    if re.search(r"\b(exit|quit|bye)\b", text):
        return random.choice(responses["exit"]), True

    # Greetings
    if re.search(r"\b(hi|hello|hey)\b", text):
        return random.choice(responses["greetings"]), False

    # Help (check if user is happy → happy_help)
    happy_words = ["happy", "great", "awesome", "good"]
    if re.search(r"\b(help|support)\b", text):
        if any(word in text for word in happy_words):
            return random.choice(responses["happy_help"]), False
        return random.choice(responses["help"]), False

    # How are you → bot identity
    if re.search(r"\b(how are you|how r u|what's up|how is it going)\b", text):
        return random.choice(responses["bot_identity"]), False

    # Personal questions
    if re.search(r"\b(age|address|phone|number|married|salary|location|where do you live)\b", text):
        return random.choice(responses["personal_refusal"]), False

    # Emotion detection
    emotion = detect_emotion(text)
    if emotion:
        response = f"I noticed you seem {emotion}. I hope things improve."
        if DEBUG:
            response = f"[Detected emotion: {emotion}] {response}"
        return response, False

    # Unknown input
    return random.choice(responses["fallback"]), False

# Main loop
def main():
    print("🤖 Advanced Rule-Based Chatbot Started (type 'exit' to quit)\n")

    while True:
        try:
            user_input = input("You: ")
            reply, should_exit = chatbot_response(user_input)
            print("Bot:", reply)

            if should_exit:
                break

        except KeyboardInterrupt:
            print("\nBot: Chat interrupted. Goodbye!")
            break
        except Exception:
            print("Bot: Something went wrong.")

if __name__ == "__main__":
    main()
