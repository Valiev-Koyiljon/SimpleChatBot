import streamlit as st
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello! I'm Koyilbek's chatbot. How can I assist you?", "Hey there! How can I help you today?"]
    ],
    [
        r"who are you|what are you",
        ["I'm a chatbot designed to provide information about Koyilbek, an AI engineer from Uzbekistan. How can I assist you?", "I'm Koyilbek's virtual assistant. I can tell you about his experience, skills, and achievements."]
    ],
    [
        r"(.*) name ?",
        ["My name is Koyilbek.", "I am Koyilbek from Uzbekistan, a passionate AI engineer dedicated to building intelligent systems."]
    ],
    [
        r"how old are you|age",
        ["Koyilbek was born in 2003."]
    ],
    [
        r"email",
        ["Koyilbek's email is valievkoyiljon112@gmail.com"]
    ],
    [
        r"phone number|contact number",
        ["Koyilbek's phone number is +82-010-2253-3010"]
    ],
    [
        r"current location|where do you live",
        ["Koyilbek currently resides in Daejeon, South Korea"]
    ],
    [
        r"where are you from|nationality",
        ["Koyilbek is from Uzbekistan"]
    ],
    [
        r"skills|expertise|proficiency",
        ["Koyilbek has expertise in:\n1. Programming: Python\n2. ML/DL Frameworks: PyTorch, TensorFlow, Transformers, PEFT, StableBaselines3\n3. Data Science: NumPy, Pandas, SciPy, Matplotlib, Seaborn\n4. LLMs: LLAMA, Ollama, GPT\n5. DevOps: Git, GitHub, Docker, FastAPI\n6. Optimization: Optuna, Accelerate\n7. NLP: NLTK\n8. RL: OpenAI Gym"]
    ],
    [
        r"work experience|job history",
        [
            "Koyilbek's work experience includes:\n\n1. AI Engineer & Team Lead at Recs Innovation Ltd (Feb 2024 - Present):\n- Started as AI Intern (Feb-Mar 2024)\n- Promoted to AI Team Lead (Mar-Jul 2024)\n- Currently working as AI Engineer (Jul 2024-Present)\n\nAs Team Lead:\n- Led anomaly detection system development for photovoltaic sensors\n- Built automated data pipeline processing 1.3M+ daily sensor readings\n- Managed AI team and coordinated with international stakeholders\n\n2. AI Researcher at Woosong University (Sep 2023 - Dec 2023):\n- Led trash bag collection optimization project using YOLOv8\n\n3. AI Research & Computer Vision Intern at Sequus PTY LTD (Jun 2023 - Aug 2023)\n\n4. Computer Vision & IoT Intern at The Sparks Foundation (May 2023 - Jun 2023)"
        ]
    ],
    [
        r"leadership experience|team lead",
        [
            "Koyilbek served as AI Team Lead at Recs Innovation Ltd (March 2024 - July 2024) where he:\n- Led the development of an anomaly detection system for photovoltaic sensors\n- Managed data pipeline processing 1.3M+ sensor readings daily\n- Established MLflow experimentation framework\n- Led an AI team and coordinated with executives and international stakeholders"
        ]
    ],
    [
        r"current role|recent work",
        [
            "Koyilbek has progressed through several roles at Recs Innovation Ltd:\n1. Currently: AI Engineer (July 2024 - Present)\n- Developing bidding optimization systems\n- Creating solar power forecasting frameworks\n2. Previously: AI Team Lead (March 2024 - July 2024)\n- Led anomaly detection system development\n- Managed AI team and data pipeline\n3. Initially: AI Intern (Feb 2024 - March 2024)\n- Implemented Autoencoder models for sensor data"
        ]
    ],
    [
        r"career progression|promotions",
        [
            "At Recs Innovation Ltd, Koyilbek showed rapid career growth:\n1. Started as AI Intern (Feb 2024)\n2. Promoted to AI Team Lead (March 2024)\n3. Transitioned to AI Engineer role (July 2024)\nEach role involved increasing responsibilities in AI development and team management."
        ]
    ],
    [
        r"education",
        [
            "Koyilbek's education:\n1. Bachelor's in Artificial Intelligence from Woosong University (2021-2025)\n2. Mathematics and Physics from High School #13 in Ferghana Region (2020-2021)"
        ]
    ],
    [
        r"achievements|accomplishments",
        [
            "Koyilbek's notable achievements include:\n1. 1st Place in Woosong University Capstone Contest (2023)\n2. 2nd Place in Machine Learning Learning Concert Competition (2023)\n3. 1st Place in IoT Learning Concert Competition (2023)\n4. 1st Place in School Chess Competition (2013)\n5. 2nd Place in Ferghana District Chess Competition (2013)\n6. 1st Place in School Russian Language Competition (2015)\n7. 2nd Place in Ferghana District English Language Competition (2019)"
        ]
    ],
    [
        r"activities|Woosong Activities|extracurricular",
        [
            "At Woosong University, Koyilbek:\n1. Served as Sol-Green Police Volunteer (Jul 2023 - Oct 2023)\n2. Worked as Python Programming Club Instructor (Oct 2021 - Dec 2021)"
        ]
    ],
    [
        r"capstone project|major project",
        [
            "Koyilbek's team won 1st Place in Woosong University's capstone project contest, competing against 200+ teams from 29 departments. They developed an AI-based solution for optimizing garbage collection in South Korea using YOLOv8 technology."
        ]
    ],
    [
        r"solar power|energy management",
        [
            "At Recs Innovation Ltd, Koyilbek developed solar power forecasting systems using hybrid LSTM-CNN models and reinforcement learning. He achieved a 0.7% error rate in bidding optimization and integrated predictions into Sun-Q EMS."
        ]
    ],
    [
        r"How can I contact Koyilbek",
        ["You can contact Koyilbek via email at valievkoyiljon112@gmail.com or through his LinkedIn profile: https://www.linkedin.com/in/koyiljonvaliev2003/"]
    ],
    [
        r"(.*) (portfolio|website) ?",
        ["You can check out Koyilbek's portfolio at: https://valiev-koyiljon.github.io/Web/"]
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
        r"thank you|thanks",
        ["You're welcome!", "Happy to help!"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! Have a great day!", "Bye! Take care."]
    ]
]

questions = [
    # Basic Information
    "How old is Koyilbek?",
    "Where is Koyilbek from?",
    "Where does Koyilbek currently live?",

    # Contact Information
    "What is Koyilbek's email?",
    "What is Koyilbek's phone number?",
    "How can I contact Koyilbek?",
    "What is Koyilbek's portfolio website?",

    # Professional Background
    "What is Koyilbek's current role?",
    "What is Koyilbek's leadership experience?",
    "Tell me about Koyilbek's work at Recs Innovation",
    "What was Koyilbek's role as Team Lead?",

    # Skills and Expertise
    "What are Koyilbek's technical skills?",
    "What is Koyilbek's AI and ML expertise?",
    "What is Koyilbek's experience with energy management systems?",

    # Education
    "What is Koyilbek's educational background?",
    "What university does Koyilbek attend?",

    # Projects
    "What major projects has Koyilbek completed?",
    "Tell me about Koyilbek's solar power forecasting system",
    "What was Koyilbek's capstone project?",

    # Achievements
    "What awards has Koyilbek won?",
    "What are Koyilbek's notable achievements?"
]

# # Create a chatbot
# chatbot = Chat(pairs, reflections)

# # List to store conversation history
# conversation_history = []

def chat(message):
    response = chatbot.respond(message)
    return response if response else "I'm sorry, I do not have an answer for this question."


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
