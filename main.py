import streamlit as st
from nltk.chat.util import Chat, reflections

pairs = [
   
[
        r"work experience",
        [
            "Koyilbek has a diverse range of work experiences:",
            "1. AI Researcher & AI Engineer at Woosong University Capstone Project (Sep 2023 - Dec 2023): Optimizing trash bag collection using YOLOv8.",
            "2. AI Research & Computer Vision Intern at Sequus PTY LTD (Jun 2023 - Oct 2023): Annotating construction plan drawings and automating annotation process.",
            "3. Computer Vision & IoT Intern at The Sparks Foundation (May 2023 - Jun 2023): Developing a real-time face mask detection system."
        ]
    ],

    [
        
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi!"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you.", "I'm fine, thanks for asking!"]
    ],
    [
        r"what is your name ?",
        ["You can call me ChatBot.", "I'm ChatBot!"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye!", "Bye! Take care."]
    ],
    [
        r"(.*) your name (.*)",
        ["My name is ChatBot."]
    ],
    [
        r"(.*) (age|old) ?",
        ["Koyilbek is 21 years old"]
    ],
    [
        r"(.*) (created|made) ?",
        ["I was created using Python programming language."]
    ],
    [
        r"(.*) (portfolio) ?",
        ["You can check out Koyilbek's portfolio at their website: https://valiev-koyiljon.github.io/Web/"]
    ],
      [
        r"hi|hello|hey",
        ["Hello! I'm Koyilbek's chatbot. How can I assist you?", "Hey there! How can I help you today?"]
    ],
    [
        r"who are you|what are you",
        ["I'm a chatbot designed to provide information about Koyilbek. What do you want to know?", "I'm Koyilbek's virtual assistant. How can I assist you?"]
    ],
    [
        r"(.*) name ?",
        ["My name is Koyilbek.", "I am Koyilbek from Uzbekistan."]
    ],
    [
        r"how old are you|age",
        ["Koyilbek is 21 years old."]
    ],
    [
        r"email",
        ["Koyilbek's email is valievkoyiljon112@gmail.com."]
    ],
    [
        r"phone number|contact number",
        ["Koyilbek's phone number is +82-010-2253-3010."]
    ],
    [
        r"current location|where do you live",
        ["Koyilbek currently resides in Daejeon, South Korea."]
    ],
    [
        r"where are you from|nationality",
        ["Koyilbek is from Uzbekistan."]
    ],
    [
        r"skills|expertise|proficiency",
        ["Koyilbek has expertise in Python, OpenCV, Git, PyTorch, Streamlit, Scikit-Learn, TensorFlow, YOLO, Matplotlib, Seaborn, Pandas, NumPy, FastAPI, Scipy, Transformer, Selenium, and Django."]
    ],
    [
        r"work experience",
        [
            "Koyilbek worked as an AI Researcher & AI Engineer at Woosong University Capstone Project from Sep 2023 to Dec 2023, focusing on optimizing trash bag collection using YOLOv8.",
            "Koyilbek also worked as an AI Research & Computer Vision Intern at Sequus PTY LTD from June 2023 to October 2023, annotating construction plan drawings and automating the annotation process.",
            "Furthermore, Koyilbek served as a Computer Vision & IoT Intern at The Sparks Foundation from May 2023 to June 2023, developing a real-time face mask detection system."
        ]
    ],
    [
        r"education",
        [
            "Koyilbek is pursuing a Bachelor's in Artificial Intelligence from Woosong University (2021-2025).",
            "Previously, Koyilbek studied Mathematics and Physics from High School #13 in the Ferghana Region (2020-2021)."
        ]
    ],
    [
        r"achievements|accomplishments",
        [
            "Koyilbek has several achievements including winning chess and language competitions, earning recognition in the Machine Learning class Learning Concert Competition, and securing multiple awards in various contests at Woosong University."
        ]
    ],
    [
        r"activities|Woosong Activities|extracurricular",
        [
            "At Woosong University, Koyilbek volunteered as a Sol-Green Police Volunteer, taking care of the university environment, and was also a Python Programming Club Instructor."
        ]
    ],
    [
        r"capstone project|major project",
        [
            "Koyilbek contributed to securing 1st Place in Woosong University's major capstone project contest, implementing an AI-based solution to optimize garbage collection in South Korea."
        ]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "My pleasure to assist you!"]
    ],
    [
        r"goodbye|bye",
        ["Goodbye! Have a great day!", "Bye! Take care."]
    ],
    [
        r"Trash Bag Segmentation|Optimizing trash bag collection",
        ["Koyilbek's team developed an AI project for NetVision Company using YOLOv8 for trash bag optimization in real-time video streams. The project won the Woosong University President's Award."]
    ],
    [
        r"Real Time Face Mask Detection|Face mask identification",
        ["This project used PyTorch, OpenCV, and MTCNN for face mask identification in real-time video feeds."]
    ],
       [
        r"Tell me about Koyilbek",
        ["Koyilbek is an AI and Machine Learning Engineer from Uzbekistan. He specializes in Python, deep learning, computer vision, and has experience in developing and deploying ML models."]
    ],
    [
        r"What skills does Koyilbek have",
        ["Koyilbek has skills in Python, OpenCV, Git, PyTorch, TensorFlow, Scikit-Learn, YOLO, Matplotlib, Pandas, NumPy, FastAPI, Scipy, Streamlit, Django, and more."]
    ],
    [
        r"What work experience does Koyilbek have",
        ["Koyilbek worked as an AI Researcher & Engineer, Computer Vision & IoT Intern, and contributed to various projects focusing on trash bag optimization, face mask detection, weather classification, IoT systems, healthcare, and more."]
    ],
    [
        r"What is Koyilbek's educational background",
        ["Koyilbek is pursuing a Bachelor's in Artificial Intelligence from Woosong University and completed Mathematics and Physics in high school."]
    ],
    [
        r"What awards has Koyilbek won",
        ["Koyilbek has won awards in chess competitions, language competitions, machine learning competitions, and university capstone contests."]
    ],
    [
        r"What projects have Koyilbek completed",
        ["Koyilbek completed projects on trash bag optimization, face mask detection, weather classification, exploratory data analysis, IoT-based systems, kidney illness detection, banking, insurance, and house price prediction."]
    ],
    [
        r"How can I contact Koyilbek",
        ["You can contact Koyilbek via email at valievkoyiljon112@gmail.com or through his LinkedIn profile: [LinkedIn Profile Link]"]
    ],
    [
        r"Tell me about Koyilbek's portfolio",
        ["You can access Koyilbek's portfolio here: https://valiev-koyiljon.github.io/Web/"]
    ],
    # .
    # Additional variations of questions and responses can be added here
]



questions = [
    # Greeting
    "Hi, hello, hey",
    "How are you ?",

    # Personal Information
    "What is your name ?",
    "What is Koyilbek's name ?",
    "What is your age ?",
    "How old are you ?",
    "Who are you? / What are you?",

    # Contact Information
    "Email",
    "Phone number / Contact number",
    "How can I contact Koyilbek?",

    # Location
    "Current location / Where do you live?",
    "Where are you from / Nationality?",

    # Skills
    "Skills / Expertise / Proficiency",

    # Work Experience
    "Work experience",
    "What work experience does Koyilbek have?",

    # Education
    "Education",
    "What is Koyilbek's educational background?",

    # Achievements
    "Achievements / Accomplishments",
    "What awards has Koyilbek won?",

    # Activities
    "Activities / Woosong Activities / Extracurricular",

    # Projects
    "Capstone project / Major project",
    "What projects have Koyilbek completed?",

    # General Information
    "Tell me about Koyilbek",
    "What skills does Koyilbek have?",

    # Specific Projects
    "Trash Bag Segmentation / Optimizing trash bag collection",
    "Real Time Face Mask Detection / Face mask identification",

    # Closure
    "Thank you / Thanks",
    "Goodbye / Bye"
]


# # Create a chatbot
# chatbot = Chat(pairs, reflections)

# # List to store conversation history
# conversation_history = []

def chat(message):
    response = chatbot.respond(message)
    return response if response else "I'm sorry, I do not have an answer for this question."

# # Streamlit app
# def main():
#     st.title("Simple ChatBot")
#     st.title("List of Questions")

#     st.write("Here is a list of questions:")
#     for index, question in enumerate(questions, start=1):
#         st.write(f"{index}. {question}")
#     st.markdown(
#         """
#         <style>
#         .stApp {
#             background-color: #f0f0f0;
#         }
#         .stTextInput > div > div > input {
#             border: 2px solid #0080ff;
#             border-radius: 5px;
#             padding: 8px 10px;
#             ::placeholder {
#                 color: #aaa;
#                 opacity: 0.5;
#             }
#         }
#         .stButton button {
#             background-color: #0080ff;
#             color: white;
#             border-radius: 5px;
#             padding: 8px 15px;
#         }
#         .stMarkdown {
#             font-weight: bold;
#             color: #0080ff;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

#     st.write("Hi! I'm a simple ChatBot. You can ask about Koyilbek Valiev.")

#     user_input = st.text_input("Enter your message here:", value='', help='Type here...')

#     if st.button("Send"):
#         if user_input:
#             bot_response = chat(user_input)
#             conversation_history.append({"user": user_input, "bot": bot_response})

#             for conv in conversation_history:
#                 st.markdown(
#                     f"<div style='padding: 5px;'>You: {conv['user']}</div>"
#                     f"<div style='padding: 5px;'>Bot: {conv['bot']}</div>",
#                     unsafe_allow_html=True
#                 )
            
#             st.markdown("<hr>", unsafe_allow_html=True)  # Add a horizontal line to separate conversations
#         else:
#             st.warning("Please enter a message!")

# if __name__ == "__main__":
#     main()


# Create a chatbot
chatbot = Chat(pairs, reflections)

# Streamlit app
def main():
    st.title("Simple ChatBot")
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #f0f0f0;
        }
        .stTextInput > div > div > input {
            border: 2px solid #0080ff;
            border-radius: 5px;
            padding: 8px 10px;
            ::placeholder {
                color: #aaa;
                opacity: 0.5;
            }
        }
        .stButton button {
            background-color: #0080ff;
            color: white;
            border-radius: 5px;
            padding: 8px 15px;
        }
        .stMarkdown {
            font-weight: bold;
            color: #0080ff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.write("Hi! I'm a simple ChatBot. You can ask about Koyilbek Valiev.")

    user_input = st.text_input("Enter your message here:", value='', help='Type here...')

    if st.button("Send"):
        if user_input:
            bot_response = chat(user_input)
            st.markdown(
                f"<div style='padding: 5px;'>You: {user_input}</div>"
                f"<div style='padding: 5px; text-align: right;'>Bot: {bot_response}</div>",
                unsafe_allow_html=True
            )
            st.markdown("<hr>", unsafe_allow_html=True)  # Add a horizontal line to separate conversations
        else:
            st.warning("Please enter a message!")

    st.sidebar.title("List of Example Questions")
    for index, question in enumerate(questions, start=1):
        st.sidebar.write(f"{index}. {question}")

if __name__ == "__main__":
    main()
