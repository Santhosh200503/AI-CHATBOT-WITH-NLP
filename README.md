#AI-CHATBOT-WITH-NLP

COMPANY: CODTECH IT SOLUTIONS

NAME: santhosh Kumar B

INTERN ID: CT04WG10

DOMAIN: PYTHON PROGRAMMINNG

DURATION: 4 WEEKS

MENTOR: NEELA SANTHOSH AI-CHATBOT-WITH-NLP
#This AI chatbot project is a comprehensive implementation of a rule-based natural language processing system developed in Python using the NLTK (Natural Language Toolkit) library. It is designed to simulate human-like conversations by analyzing user input and providing contextually appropriate responses. The core mechanism of the chatbot relies on a collection of predefined patterns and responses, where each user message is matched against a list of regular expression (regex) patterns. These patterns are mapped to specific sets of responses that the bot randomly selects from when a match is found, creating variation and a sense of spontaneity in its replies. For instance, when a user greets the bot with “hello” or “hi,” the regex pattern hi|hello|hey is triggered, prompting the chatbot to respond with friendly phrases like “Hello!” or “Hey there!”. The use of regex provides flexibility in recognizing various ways users may phrase their questions, making the chatbot more versatile in its understanding. Beyond simple greetings, the chatbot is also capable of handling conversational topics like asking about its identity (“What is your name?”), its purpose (“What can you do?”), or even its origins (“Who created you?”). These personalized responses help establish a sense of character and engagement with the user.

In addition to basic conversations, the chatbot integrates a basic form of computational intelligence by evaluating mathematical expressions. When a user inputs a phrase such as “calculate 8 * 5” or “calculate 12 / 4 + 3”, the bot uses Python’s eval() function to compute the result in a controlled environment. This is done securely by disabling access to built-in functions to prevent unsafe code execution. This feature transforms the chatbot from a simple responder to a functional assistant that can perform useful tasks. Furthermore, the chatbot has been enhanced to respond to questions about the current time and date using Python’s datetime module, allowing it to provide real-time responses like “The current date and time is…” when such queries are detected in user input. All user interactions are stored in a memory list, which could later be expanded to maintain context over a conversation, implement sentiment tracking, or even personalize interactions based on past inputs. The program runs in a continuous loop, allowing real-time back-and-forth conversation with the user, and only terminates when the keyword “quit” is entered. If the bot cannot understand a user's message—perhaps because it doesn't match any defined pattern—it gracefully responds with a fallback message that encourages the user to clarify or ask something different, thereby maintaining the flow of conversation and preventing dead ends.

Another key feature is the integration of NLTK’s reflections, a utility that reverses common pronouns and verbs to give replies that sound more natural—for example, converting “I am” to “you are.” This helps simulate more human-like dialogue. While this chatbot is rule-based, meaning it doesn't "learn" from interactions, it forms a strong foundation for exploring more complex AI systems. It introduces developers to important NLP concepts like tokenization, pattern matching, input parsing, and response generation. In future upgrades, this chatbot could be extended with machine learning libraries such as spaCy, Hugging Face Transformers, or integrated into web apps using frameworks like Flask, Django, or React. Voice recognition and speech synthesis could also be included to turn this into a voice assistant. In short, this project is an excellent demonstration of how traditional NLP techniques can be used to create interactive applications, and it offers countless opportunities for expansion, innovation, and deeper exploration into artificial intelligence.

#output
![Image](https://github.com/user-attachments/assets/84ea54a8-ccc0-4b90-b5da-9eab79a08e25)
