import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st


# تصنيف المقال بناءً على العنوان
def classify_article(title):
    title = title.lower()
    categories = {
        "📊 الاقتصاد & الأعمال": ["market", "business", "finance", "stock"],
        "🤖 التكنولوجيا": ["AI", "tech", "software", "robotics"],
        "🏥 الصحة": ["health", "medicine", "wellness", "covid"],
    }
    for category, keywords in categories.items():
        if any(keyword in title for keyword in keywords):
            return category
    return "🌎 الأخبار العامة"


# عنوان التطبيق
st.title("🔍 Web Scraping & Data Classification")

# إدخال الرابط
url = st.text_input("🔗 أدخل رابط الموقع:")

if st.button("ابدأ التحليل 🚀"):
    if not url:
        st.error("❌ الرجاء إدخال رابط الموقع!")
    else:
        headers = {"User-Agent": "Mozilla/5.0"}
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            # استخراج المقالات
            articles = soup.find_all("article")

            if not articles:
                st.warning("⚠️ لم يتم العثور على أي بيانات، جرّب رابطًا آخر.")
            else:
                data = []
                for article in articles:
                    title = (
                        article.find("h2").text
                        if article.find("h2")
                        else "No Title"
                    )
                    link = (
                        article.find("a")["href"]
                        if article.find("a")
                        else "No Link"
                    )
                    summary = (
                        article.find("p").text
                        if article.find("p")
                        else "No Summary"
                    )
                    category = classify_article(title)

                    data.append({"Title": title, "Link": link,
                                 "Summary": summary, "Category": category})

                # حفظ البيانات في ملف CSV
                df = pd.DataFrame(data)
                filename = "classified_scraped_data.csv"
                df.to_csv(filename, index=False, encoding="utf-8")

                # عرض البيانات مع التصنيف
                st.success(f"✅ تم استخراج {len(data)} مقال وتصنيفه!")
                st.dataframe(df)

                # زر لتحميل الملف
                st.download_button(
                    label="📥 تحميل البيانات المصنفة كـ CSV",
                    data=df.to_csv(index=False).encode("utf-8"),
                    file_name="classified_scraped_data.csv",
                    mime="text/csv",
                )

        except requests.exceptions.RequestException as e:
            st.error(f"❌ حدث خطأ أثناء جلب البيانات:\n{e}")
