# 🛍️ Product Review Generator using GPT & Streamlit

A simple **AI-powered product review generator** built with **Streamlit** and **OpenAI GPT API**.  
Users can input product details and instantly get a **personalized, human-like product review**.

---

## 🚀 Features
- 📄 Generate realistic product reviews using GPT
- 🎛 Adjustable tone and length (optional)
- ⚡ Instant output in a clean Streamlit UI
- ☁️ Deployable on Streamlit Cloud / Hugging Face Spaces

---

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set your OpenAI API key**
```bash
export OPENAI_API_KEY="your_api_key_here"
```
*(On Windows PowerShell use: `setx OPENAI_API_KEY "your_api_key_here"`)*
  
4. **Run the app**
```bash
streamlit run app.py
```

---

## 🛠 Deployment
### **Streamlit Cloud**
1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://share.streamlit.io/)
3. Connect your GitHub repo
4. Set the **OPENAI_API_KEY** in Secrets Manager

---

## 📂 Project Structure
```
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
```

---

## 📜 License
This project is licensed under the MIT License.
