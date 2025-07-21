"""
Author : M.Madhusudhanan
Reg no : 3122225002067
"""

class TextEditor:
    def __init__(self):
        # Initialize an empty text when an instance of TextEditor is created.
        self.text = ""
    
    def load_text(self, text):
        # Load the provided text into the text editor.
        self.text = text

    def get_statistics(self):
        # Calculate and return statistics about the text.
        char_count = len(self.text)  # Count characters
        word_count = len(self.text.split())  # Count words
        sentence_count = self.text.count('.') + self.text.count(
            '!') + self.text.count('?')  # Count sentences
        return char_count, word_count, sentence_count

    def count_word_frequencies(self, top_n):
        # Count and return the top N most frequent words in the text.
        words = self.text.split()
        word_freq = {}
        for word in words:
            word = word.strip('.,!?()[]{}":;')  # Remove punctuation
            word = word.lower()  # Convert to lowercase
            if word:
                word_freq[word] = word_freq.get(word, 0) + 1
        sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)  # Sort by frequency
        return sorted_word_freq[:top_n]

    def append_text(self, text_to_append):
        # Append the provided text to the end of the current text.
        self.text += text_to_append

    def insert_text(self, position, text_to_insert):
        # Insert the provided text at the specified position in the text.
        self.text = self.text[:position] + text_to_insert + self.text[position:]

    def search_and_replace(self, search_text, replace_text):
        # Search for a specific text and replace it with another text in the entire document.
        self.text = self.text.replace(search_text, replace_text)

    def delete_text(self, start, end):
        # Delete a portion of the text, specified by the start and end positions.
        self.text = self.text[:start] + self.text[end:]

    def categorize_text(self):
        # Categorize the text based on a specific logic, but this part is left as an exercise.
        # It's recommended to use external libraries for accurate categorization if needed.
        categorized_text = {}  # Store categorized text and their counts
        return categorized_text

# Example usage:
editor = TextEditor()
editor.load_text(" Vicky waited for the train. The train was late. Mary and Samantha took the bus.")
char_count, word_count, sentence_count = editor.get_statistics()
print(f"Character Count: {char_count}")
print(f"Word Count: {word_count}")
print(f"Sentence Count: {sentence_count}")
top_words = editor.count_word_frequencies(3)
print(f"Top Words: {top_words}")
editor.append_text(" Appended Text.")
print("After Append:", editor.text)
editor.insert_text(10, "Inserted")
print("After Insert:", editor.text)
editor.search_and_replace("sample", "modified")
print("After Replace:", editor.text)
editor.delete_text(5, 14)
print("After Delete:", editor.text)
categorized_text = editor.categorize_text()  # Categorization logic needs to be implemented.
print("Categorized Text:", categorized_text)
