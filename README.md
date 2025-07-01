# 🧠 Multi-Modal Memory Chatbot

A powerful **Multi-Modal Memory Chatbot** that can process text and images, maintaining contextual memory across conversations. Built with Python and Streamlit, integrating AI models for a seamless user experience.

---

## 🚀 Features

✅ Multi-Modal input (Text + Image)  
✅ Memory-based conversation context  
✅ Streamlit Web UI  
✅ Easy to set up and deploy  
✅ Extensible for future LLM or Vision API integrations

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (for interactive UI)
- **OpenAI API** (for LLM integration)
- **Docker** (for containerized deployment)

---

## 📂 Project Structure
multi_modal_memory_chatbot/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
└── .gitignore



### 1. **Clone the repository**

```bash
git clone https://github.com/<your-username>/multi_modal_memory_chatbot.git
cd multi_modal_memory_chatbot
```

2. Create a virtual environment
   python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


3. Install dependencies
   pip install -r requirements.txt

4. Set up environment variables
   OPENAI_API_KEY=your_api_key_here

5. Run the application
   streamlit run app.py

