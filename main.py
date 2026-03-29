import tkinter as tk
from tkinter import messagebox
from newspaper import Article
import nltk
from nltk.tokenize import sent_tokenize
from collections import Counter
import re

nltk.download('punkt', quiet=True)

def summarize_text(text, n=3):
    sentences = sent_tokenize(text)

    words = re.findall(r'\w+', text.lower())
    freq = Counter(words)

    sentence_scores = {}

    for sentence in sentences:
        for word in re.findall(r'\w+', sentence.lower()):
            if word in freq:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + freq[word]

    # Get top N sentences
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:n]

    return " ".join(summary_sentences)


def summarize_news():
    url = entry.get()

    if url == "":
        messagebox.showwarning("Warning", "Enter URL")
        return

    try:
        article = Article(url)
        article.download()
        article.parse()

        text = article.text

        # ✅ Better summary
        summary = summarize_text(text, 3)

        title_text.delete("1.0", tk.END)
        title_text.insert(tk.END, article.title)

        summary_text.delete("1.0", tk.END)
        summary_text.insert(tk.END, summary)

    except Exception as e:
        messagebox.showerror("Error", str(e))



def clear_all():
    entry.delete(0, tk.END)
    title_text.delete("1.0", tk.END)
    summary_text.delete("1.0", tk.END)

root = tk.Tk()
root.title("News Summarizer")
root.geometry("700x520")

tk.Label(root,
         text="📰 NEWS ARTICLE SUMMARIZER",
         font=("Arial", 20, "bold"),
         fg="#1f4e79").pack(pady=15)

entry = tk.Entry(root, width=80)
entry.pack(pady=10)
entry.insert(0, "Enter the URL here...")
entry.config(fg="grey")

def on_click(event):
    if entry.get() == "Enter the URL here...":
        entry.delete(0, tk.END)
        entry.config(fg="black")

def on_leave(event):
    if entry.get() == "":
        entry.insert(0, "Enter the URL here...")
        entry.config(fg="grey")

entry.bind("<FocusIn>", on_click)
entry.bind("<FocusOut>", on_leave)



btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Summarize", command=summarize_news, bg="blue", fg="Black").pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Clear", command=clear_all, bg="red", fg="Black").pack(side=tk.LEFT, padx=5)


title_text = tk.Text(root, height=2, wrap="word")
title_text.pack(pady=5)

frame = tk.Frame(root)
frame.pack()

scroll = tk.Scrollbar(frame)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

summary_text = tk.Text(frame, height=15, width=80, wrap="word", yscrollcommand=scroll.set)
summary_text.pack()

scroll.config(command=summary_text.yview)

root.mainloop()