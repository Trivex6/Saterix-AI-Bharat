# 🛡️ Saterix AI: Cognitive Firewall for Rural Bharat

**Team Loop Lords | AI for Bharat Competition 2026**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge.svg)](https://saterix-ai-bharat.streamlit.app/)
![Security Hardened](https://img.shields.io/badge/Security-L3_Hardened-red?style=for-the-badge&logo=shield)
![Latency](https://img.shields.io/badge/Latency-~280ms-green?style=for-the-badge&logo=lightning)
![AI Model](https://img.shields.io/badge/Model-Llama_3.3_70B-blue?style=for-the-badge&logo=meta)

Saterix is a multi-layered security engine designed to protect vernacular users from social engineering scams (WBSEDCL utility fraud, banking phishing, and KYC scams). By leveraging ultra-fast LPU inference and behavioral analysis, Saterix intercepts threats in real-time before users can be manipulated.

---

## ⚙️ The Saterix Defense-in-Depth

Instead of a single check, Saterix runs every message through a 3-layer security tunnel to ensure maximum protection for rural users.

### **Layer 1: Local Heuristics (Instant Block)**
* **Regex Scanning**: Detects suspicious URL shorteners (bit.ly, t.me, wa.me).
* **Domain Watch**: Blocks impersonated utility domains (e.g., `wbsedcl-pay-bills.com`).
* **Response**: Instant flagging with **LOCAL_HEURISTICS** engine.

### **Layer 2: Instruction Isolation (Hardened)**
* **XML Encapsulation**: Wraps user input in `<UNTRUSTED_DATA>` tags to prevent Prompt Injection.
* **System Guard**: Prevents the LLM from following malicious instructions like "Ignore all previous commands."

### **Layer 3: Cognitive Intent Engine (LPU Powered)**
* **Groq LPU™**: Leverages **Llama 3.3 (70B)** with a **~280ms response time**.
* **Social Engineering Detection**: Identifies psychological triggers like artificial urgency and fear in **Bengali, Hindi, and Hinglish**.

---

## 🚀 Key Features

* **⚡ LPU-Powered Inference:** Extreme speed (~280ms) ensures the user is warned before they click.
* **🎙️ Bimodal Accessibility:** Native **Speech-to-Text (STT)** integration for users with low digital literacy.
* **🇮🇳 Vernacular Intelligence:** Optimized for the unique threat landscape of rural West Bengal and India.

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Frontend** | Streamlit |
| **LLM Engine** | Llama 3.3 70B (**Groq LPU**) |
| **Database** | Amazon DynamoDB |
| **Voice Engine** | Streamlit Mic Recorder (STT) |
| **Security Layer** | XML Delimiter Hardening |

---

## 🚀 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yoyobabaji009/Saterix-AI-Bharat

Install dependencies
pip install -r requirements.txt

3. Configure Secrets
Create a folder named .streamlit and a file inside it called secrets.toml:

GROQ_API_KEY = "your_groq_key_here"
AWS_ACCESS_KEY_ID = "your_aws_key_here"
AWS_SECRET_ACCESS_KEY = "your_aws_secret_here"

4. Run Saterix
streamlit run app.py

