"""
Author : M.Madhusudhanan
Reg no : 3122225002067
"""

import re
from collections import Counter

class TextEditor:
    def __init__(self):
        self.text = ""
    
    def load_text(self, input_text):
        self.text = input_text

    def get_basic_stats(self):
        char_count = len(self.text)
        word_count = len(self.text.split())
        sentence_count = len(re.split(r'[.!?]', self.text))
        return char_count, word_count, sentence_count

    def count_word_frequencies(self, top_n):
        words = re.findall(r'\w+', self.text.lower())
        word_freq = Counter(words)
        return word_freq.most_common(top_n)

    def append_text(self, new_text):
        self.text += new_text

    def insert_text(self, position, new_text):
        self.text = self.text[:position] + new_text + self.text[position:]

    def search_and_replace(self, search_text, replace_text):
        self.text = self.text.replace(search_text, replace_text)

    def delete_text(self, start, end):
        self.text = self.text[:start] + self.text[end:]

    def categorize_text(self):
        categories = {
            "numbers": len(re.findall(r'\d+', self.text)),
            "alphabets": len(re.findall(r'[a-zA-Z]+', self.text)),
            "urls": len(re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', self.text)),
            "links": len(re.findall(r'www\.[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', self.text)),
        }
        categories["others"] = len(self.text.split()) - sum(categories.values())
        return categories

if __name__ == "__main__":
    editor = TextEditor()
    input_text = """Unfortunately, the Department hasn't bothered to keep any of the old links,
    or provide cross-links into the new database-driven website in www.apple.com"""

    editor.load_text(input_text)

    char_count, word_count, sentence_count = editor.get_basic_stats()
    print(f"Character Count: {char_count}")
    print(f"Word Count: {word_count}")
    print(f"Sentence Count: {sentence_count}")

    top_words = editor.count_word_frequencies(5)
    print("Top 5 words and their frequencies:")
    for word, freq in top_words:
        print(f"{word}: {freq}")

    # Example usage of other functions:
    # editor.append_text(" More text to append.")
    # editor.insert_text(10, " Inserted ")
    # editor.search_and_replace("input", "text")
    # editor.delete_text(5, 15)

    categories = editor.categorize_text()
    print("Categorized Text:")
    for category, count in categories.items():
        print(f"{category.capitalize()}: {count}")

    # Ensure total word count matches categorized count
    total_word_count = sum(categories.values())
    print(f"Total Word Count: {total_word_count}")

