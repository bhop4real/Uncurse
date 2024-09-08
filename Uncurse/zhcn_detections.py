import os
from pypinyin import lazy_pinyin


# Remove exceptions and process pinyin for Chinese detection
def detect_inappropriate_chinese(text):
    chinese_dir = os.path.join(os.path.dirname(__file__), 'chinese')

    basic_words = load_file(os.path.join(chinese_dir, 'basic.txt'))
    advanced_words = load_file(os.path.join(chinese_dir, 'advanced.txt'))
    exceptions = load_file(os.path.join(chinese_dir, 'exceptions.txt'))  # Load Chinese exceptions

    # Directly remove exceptions from the text
    text = remove_exceptions(text, exceptions)

    # Convert Chinese text to pinyin
    pinyin_list = lazy_pinyin(text)
    pinyin_text = ''.join(pinyin_list)  # Concatenate full pinyin

    # Check if full pinyin contains inappropriate words
    for word in basic_words:
        if word in pinyin_text:
            return True

    # If not found, check first letters of pinyin
    first_letters = ''.join([p[0] for p in pinyin_list])
    for word in advanced_words:
        if word in first_letters:
            return True

    return False  # Clean Chinese text


# Helper to load basic, advanced, and exceptions word lists
def load_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:  # Ensure UTF-8 encoding
            return [line.strip() for line in file.readlines()]
    return []


# Improved helper to remove exceptions from text
def remove_exceptions(text, exceptions):
    for exception in exceptions:
        if exception in text:
            text = text.replace(exception, "")  # Ensure complete match
    return text
