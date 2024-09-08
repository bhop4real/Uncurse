import os
import json
from .find_root import find_root_directory
from .zhcn_detections import detect_inappropriate_chinese

# Locate the root directory
root_dir = find_root_directory(os.path.dirname(__file__))
if not root_dir:
    raise FileNotFoundError("'.root' file not found. Please ensure you're in the correct directory.")


# Load English-specific files
def load_english_files():
    # Path for English resources
    english_dir = os.path.join(root_dir, 'english')

    # Load bad words and exceptions for English
    bad_words = load_file(os.path.join(english_dir, 'badwords.txt'))
    exceptions = load_file(os.path.join(english_dir, 'exceptions.txt'))

    # Load character mappings for English
    mappings = load_mappings(os.path.join(english_dir, 'maps'))

    return bad_words, exceptions, mappings


# Helper to load text files
def load_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    return []


# Load character mappings from the `maps/` folder
def load_mappings(maps_dir):
    mappings = {}
    for filename in os.listdir(maps_dir):
        if filename.endswith(".json"):
            with open(os.path.join(maps_dir, filename), 'r', encoding='utf-8') as file:
                mappings.update(json.load(file))
    return mappings


# Remove exceptions from text
def remove_exceptions(text, exceptions):
    for exception in exceptions:
        text = text.replace(exception, "")
    return text


# Apply character mappings to text
def apply_mappings(text, mappings):
    for original, replacements in mappings.items():
        if isinstance(replacements, list):
            # Iterate over the replacement list
            for replacement in replacements:
                text = text.replace(replacement, original)  # Replace each variant with the original
        else:
            text = text.replace(replacements, original)  # Single replacement case
    return text



# Detect inappropriate English text
def detect_inappropriate_english(text):
    bad_words, exceptions, mappings = load_english_files()

    # Remove exceptions and apply character mappings
    text = remove_exceptions(text, exceptions)
    text = apply_mappings(text, mappings)

    # Convert text to lowercase and check for bad words
    text = text.lower()

    for bad_word in bad_words:
        if bad_word in text:
            return True  # Inappropriate text detected
    return False  # Clean text


# Main detection function that handles both English and Chinese
def detect(text, language="english"):
    if language == "chinese":
        return detect_inappropriate_chinese(text)
    return detect_inappropriate_english(text)
