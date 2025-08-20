# ✈️ Airline Booking Market Demand – Insights Dashboard

An interactive **Streamlit dashboard** that visualizes airline booking demand using **Google Trends** as a demand proxy and optionally integrates flight traffic data sources (e.g., OpenSky).  
The app also provides **AI-powered insights** (via Gemini) or a **rule-based summary fallback**.

---

## 🚀 Features
- 📊 **Interactive charts** for flight routes demand trends  
- 📌 **Filters** by city, date range, and geography  
- 🔍 **KPIs**: Top routes, date span, tracked routes  
- 🤖 **AI summary** of demand insights (Gemini) with fallback to rule-based  
- 📷 **Latest snapshot** table for the most recent data  

---

## 📂 Project Structure
----
      Airline-Market-Demand-Insights-Dashboard/
      ├── myenv/
      ├── app.py
      ├── .env
      ├── .streamlit/
      │   └── secrets.toml
      ├── utils/
      │   ├── init.py
      │   ├── constants.py
      │   ├── data_loader.py
      │   ├── summarizer.py
      │   └── charts.py
      ├── requirements.txt
      └── README.md
-----

----

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Airline-Market-Demand-Insights-Dashboard.git
cd Airline-Market-Demand-Insights-Dashboard
```

----

2. Create & Activate Virtual Environment

   # Windows (PowerShell)
   ```
    python -m venv myenv
    myenv\Scripts\activate
    ```
    # Mac/Linux
   ```
    python3 -m venv myenv
    source myenv/bin/activate
    ```

----
3. Install Requirements

   ```
     pip install -r requirements.txt
   ```
----
4. Add API Keys

Create a .env file in the root directory:
```
  GEMINI_API_KEY=your_google_gemini_key_here

```
Or, if deploying on Streamlit Cloud, add it inside .streamlit/secrets.toml:
```
  GEMINI_API_KEY="your_google_gemini_key_here"
```
----
5. Run the App
   ```
     streamlit run app.py

   ```
----
6. ## 🖼️ UI Preview

Here’s how the dashboard looks in action 👇  

<p align="center">
  <img src="assets/airline 1.png" alt="Dashboard UI" width="700"/>
  <img src="assets/airline 2.png" alt="Dashboard UI" width="700"/>
  <img src="assets/airline 3.png" alt="Dashboard UI" width="700"/>
</p>

---

## 🤖 AI Integration

- Uses **Google Gemini** (`gemini-2.5-flash`) for AI summaries  
- If no API key is available, falls back to a **rule-based summary**  

---

## 📝 Roadmap

- [ ] Add OpenSky flight traffic integration  
- [ ] Support multi-country comparisons  
- [ ] Deploy on Streamlit Cloud  

---

## ⚡ Tech Stack

- **Frontend/UI**: [Streamlit](https://streamlit.io/)  
- **Data**: [Google Trends via PyTrends](https://github.com/GeneralMills/pytrends)  
- **Charts**: [Plotly Express](https://plotly.com/python/plotly-express/)  
- **AI**: [Google Generative AI (Gemini)](https://ai.google.dev/)  

---

## 📜 License

This project is licensed under the **MIT License**.  
You are free to use and modify it for personal and commercial purposes.  

---

## 👨‍💻 Author

Built with ❤️ by **Saswata Maitra**  

