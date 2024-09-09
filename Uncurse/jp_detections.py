import os
import jaconv
import pykakasi

# Initialize pykakasi for romaji conversion
kakasi = pykakasi.kakasi()


# Remove exceptions and process Japanese text to detect inappropriate words
def detect_inappropriate_japanese(text):
    japanese_dir = os.path.join(os.path.dirname(__file__), 'japanese')

    basic_words = load_file(os.path.join(japanese_dir, 'basic.txt'))
    advanced_words = load_file(os.path.join(japanese_dir, 'advanced.txt'))
    exceptions = load_file(os.path.join(japanese_dir, 'exceptions.txt'))  # Load Japanese exceptions

    # Directly remove exceptions from the text
    text = remove_exceptions(text, exceptions)

    # Check original Japanese text against basic words
    for word in basic_words:
        if word in text:
            return True

    # Convert Japanese text to romaji for advanced detection
    romaji_text = convert_to_romaji(text)
    print(romaji_text) # Debug

    # Check romaji text against advanced words
    for word in advanced_words:
        if word in romaji_text:
            return True

    return False  # Clean Japanese text


# Convert Japanese text to romaji using pykakasi
def convert_to_romaji(text):
    result = kakasi.convert(text)
    romaji = ''.join([item['hepburn'] for item in result])
    return jaconv.kana2alphabet(romaji)  # Ensure kana is fully romanized


# Helper to load basic, advanced, and exceptions word lists
def load_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file.readlines()]
    return []


# Helper to remove exceptions from text
def remove_exceptions(text, exceptions):
    for exception in exceptions:
        if exception in text:
            text = text.replace(exception, "")
    return text
