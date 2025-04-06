import nltk
import random
import string
from nltk.chat.util import Chat, reflections
import re

# Expanded set of patterns and responses
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hey there!", "Hi! How can I help you today?"]],
    [r"how are you ?", ["I'm good, how about you?", "I'm doing well, and you?", "I'm great, thanks for asking!"]],
    [r"(.*) your name ?", ["I'm an AI chatbot!", "Call me ChatBot, how can I assist you?"]],
    [r"what can you do ?", ["I can chat with you, answer basic questions, do simple calculations, and assist with tasks. Try asking me something!"]],
    [r"tell me a joke", [
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ]],
    [r"(.*) weather (.*)", ["I can't check real-time weather, but you can try looking it up online!"]],
    [r"(.*) your age ?", ["I'm just a few lines of code old!", "Age is just a number, and I don't have one!"]],
    [r"who created you ?", ["I was created by a programmer who loves AI!", "I'm a chatbot made with Python and NLTK!"]],
    [r"(.*) help (.*)", ["Sure! What do you need help with?", "I'm here to assist! Please ask your question."]],
    [r"what are you doing", ["I'm chatting with you! How can I assist you?", "Just here, ready to answer your questions!"]],
    [r"i want (.*) food", ["You can order food online or visit a nearby restaurant!", "Are you craving something specific? I can suggest some dishes!"]],
    [r"calculate (.*)", ["Let me calculate that for you!"]],
    [r"(.*) (time|date) ?", ["I'm not equipped to tell the time or date, but you can check on your device!"]],
    [r"who are you", ["I'm an AI chatbot designed to chat with you!", "I am ChatBot, your virtual assistant!"]],
    [r"(.*)", [
        "That's interesting! Tell me more.",
        "I see! Could you elaborate?",
        "I'm here to listen. What else can I do for you?",
        "Can you explain that a bit more?",
        "I didn't quite get that. Could you rephrase it?",
        "Hmm, that sounds intriguing! What else can you tell me?"
    ]],
    [r"quit", ["Bye! Have a great day!", "Goodbye, take care!"]]
]

# Initialize chatbot
chatbot = Chat(pairs, reflections)

# Memory for context
memory = []

def evaluate_math(expression):
    try:
        return str(eval(expression, {"__builtins__": {}}))
    except Exception:
        return "Sorry, I can't compute that."

def chatbot_response():
    print("ChatBot: Hello! Type 'quit' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'quit':
            print("ChatBot: Goodbye!")
            break
        memory.append(user_input)

        # Check for calculation requests
        match = re.search(r'calculate (.*)', user_input)
        if match:
            expression = match.group(1)
            print(f"ChatBot: {evaluate_math(expression)}")
            continue

        response = chatbot.respond(user_input)
        if response:
            print(f"ChatBot: {response}")
        else:
            print(random.choice([
                "I'm not sure how to respond to that. Try rephrasing!",
                "That’s an interesting question! Could you clarify?",
                "I might not know the answer, but I’d love to learn!",
                "Hmm... I’m not sure about that. Want to ask something else?"
            ]))

if __name__ == "__main__":
    chatbot_response()
