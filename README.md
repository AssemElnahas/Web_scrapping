# Web Scraping & Data Classification Tool

## 📌 Overview
This is a **Web Scraping Tool** built with **Streamlit** that extracts articles from a given website, classifies them into categories based on their content, and allows users to download the data as a CSV file.

## 🚀 Features
- **Extracts article titles, summaries, and links** from websites.
- **Automatically classifies articles** into predefined categories:
  - 📊 **Business & Finance**
  - 🤖 **Technology**
  - 🏥 **Health**
  - 🌎 **General News**
- **Displays extracted data in a Streamlit interface**.
- **Allows users to download classified data as a CSV file**.

## 🛠 Installation
Before running the tool, install the required Python libraries:
```bash
pip install requests beautifulsoup4 pandas streamlit
```

## ▶️ How to Run
1. **Save the Python script** (e.g., `scraper.py`).
2. **Run the Streamlit app** using the command:
```bash
streamlit run scraper.py
```
3. **Enter the website URL** in the input box.
4. **Click on the "Start Scraping 🚀" button**.
5. The extracted and classified data will be displayed in a table.
6. **Download the data as a CSV file** using the provided button.

## 📝 How Classification Works
The tool uses **keyword-based classification**:
- If the article title contains **keywords** like `market, finance, stock`, it is categorized as **Business & Finance**.
- If the title includes words like `AI, tech, robotics`, it is categorized as **Technology**.
- Articles with words like `health, medicine, covid` are classified under **Health**.
- All other articles are categorized as **General News**.

## 📌 Example Output
| Title                        | Link            | Summary            | Category          |
|------------------------------|----------------|--------------------|------------------|
| AI is Transforming the World | example.com/ai  | A brief on AI      | 🤖 Technology    |
| Stock Market Hits New Highs  | example.com/stock | Market update     | 📊 Business & Finance |
| New COVID-19 Treatment Found | example.com/health | Medical news      | 🏥 Health        |

## 🏆 Future Improvements
- Use **Natural Language Processing (NLP)** for better classification.
- Extract data from **multiple page links**.
- Add **visualizations** for data analysis.

## ⚠️ Disclaimer
This tool is for **educational and research purposes only**. Ensure that you follow the website’s `robots.txt` and terms of service before scraping data.

---
🚀 **Developed by:** Asem Elnahas | AI Developer & Data Analyst

