# AdSmart
CTR-based Ad Recommendation System using ML models for personalized ad targeting.
# 📊 AdSmart: Personalized Ad Recommendation System

AdSmart is a simple web-based ad recommendation system that uses user interaction data to recommend top-performing ads based on Click-Through Rate (CTR). Built using Python and Streamlit, this app allows marketers to analyze ads and make data-driven decisions.

---

## 🚀 Features

- Upload your own ad interaction data in `.csv` format  
- Automatically calculate CTR for each ad  
- Get top N recommended ads with highest CTR  
- Clean, interactive, and user-friendly interface  

---

## 🛠️ Tech Stack

- Python  
- Pandas  
- Streamlit  

---

## 📁 Folder Structure


<img width="542" height="209" alt="image" src="https://github.com/user-attachments/assets/a299d710-dfa0-43a4-b66f-0d88e106c8c6" />

<img width="542" height="209" alt="Screenshot 2025-07-29 062954" src="https://github.com/user-attachments/assets/346a9aa8-9e21-4b76-a1f7-686ff6db8e46" />

---

## 📦 Installation

### 1. Clone the Repository

```bash

git clone https://github.com/your-username/AdSmart.git
cd AdSmart

2. Create Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt


If requirements.txt doesn't exist yet, install manually:
pip install streamlit pandas

▶️ How to Run
streamlit run app.py

Once launched, it will open in your browser at:
📍 http://localhost:8501

Sample CSV Format
Make sure your CSV includes the following required columns:

ad_id,impressions,clicks,clicked,CTR
101,1000,200,1,0.2
102,800,80,0,0.1
...

Future Improvements
Add user segmentation

Implement ML-based personalized recommendations

Integrate real-time dashboards and analytics


Let me know if you'd like to customize:
- **GitHub username**
- **Your name**
- **Email**
- **Profile links**  
I can fill them in for you.
-----------------------------------------------------------------------
 Step 2: Check Git Status
To see what changes you've made:
git status

