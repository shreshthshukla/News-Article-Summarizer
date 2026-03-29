# 📰 News Article Summarizer

A simple Python-based desktop application that extracts and summarizes news articles from a given URL using Natural Language Processing (NLP).

---

## 🚀 Features

* 🔗 Extracts article content from any valid news URL
* 🧠 Generates a short summary using NLP techniques
* 📰 Displays article title and summarized content
* 🖥️ User-friendly GUI built with Tkinter
* 🔄 Clear button to reset inputs

---

## 🛠️ Technologies Used

* Python
* Tkinter (GUI)
* Newspaper3k (Article extraction)
* NLTK (Text processing)

---

## 📦 Installation

Follow these steps to run the project on your system:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/news-summarizer.git
cd news-summarizer
```

### 2. Install required libraries

```bash
pip install newspaper3k nltk
```

### 3. Run the application

```bash
python main.py
```

---

## ▶️ How to Use

1. Run the application

2. Paste a valid news article URL into the input box

3. Click **"Summarize"**

4. View:

   * 📰 Article Title
   * ✂️ Short Summary

5. Click **"Clear"** to reset

---

## 📂 Project Structure

```
news-summarizer/
│
├── main.py          # Main GUI application
├── README.md        # Project documentation
```

---

## 🧠 How It Works

* The app uses **Newspaper3k** to extract article text
* Text is split into sentences using **NLTK**
* Word frequency is calculated
* Sentences are ranked based on importance
* Top sentences are selected as the summary

---

## ⚠️ Notes

* Make sure you have an active internet connection
* Some websites may block scraping
* Works best with standard news article URLs

---

## 🔮 Future Improvements

* Add support for multiple languages
* Improve summary using advanced ML models (like transformers)
* Add file export (PDF/Text)
* Enhance UI design

---

## 🙌 Contributing

Feel free to fork this repository and improve the project!

---

## 📄 License

This project is open-source and free to use.

---

## 💡 Author: Shreshth Shukla

Developed as a BYOP (Bring Your Own Project) for learning Python and NLP.

