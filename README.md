# Uncurse

**Uncurse** is a highly customizable inappropriate text detection tool that supports multiple languages with modular character mappings, exception handling, and advanced detection techniques.

## Beta branch

This branch is v2-beta/Socrates, may have gliches/bugs/flaws.

## Features

- **Multi-language support**: Detects inappropriate text in (in theory) any languages.
- **Character Mapping**: Supports multiple mappings, replacing complex character variants (e.g., "1" to "i", "𝑏" to "b").
- **Exception Handling**: Removes specified exceptions before detection to avoid false positives.
- **Highly Configurable**: Uses `.txt` files for word lists (e.g., `badwords.txt`, `exceptions.txt`), `.json` for character mappings, and `.values` for configurable settings. *(Currently, .vaules files is unused.)*

## Directory Structure

```
Uncurse/
│
├── english/
│   ├── badwords.txt         # List of inappropriate words for English detection
│   ├── exceptions.txt       # List of exception words for English
│   ├── maps/                # Folder containing character mapping tables
│   │   ├── 1.json
│   │   └── 2.json
│   └── ...
│
├── chinese/
│   ├── basic.txt            # Basic pinyin word list
│   ├── advanced.txt         # Advanced pinyin word list (first letter detection)
│   ├── exceptions.txt       # List of exception words for Chinese
│   └── ...
│
└── __init__.py              # Main script for initializing Uncurse
└── zhcn_detections.py       # Chinese-specific detection logic
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/Uncurse.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Make sure to install the `pypinyin` library for Chinese pinyin processing:
   ```bash
   pip install pypinyin
   ```

## Usage

### Example: English Detection

```python
import Uncurse

text_to_check = "Your sample text here"
is_inappropriate_english = Uncurse.detect(text_to_check, language="english")

print("Contains inappropriate content:", is_inappropriate_english)
```

### Example: Chinese Detection

```python
import Uncurse

text_to_check = "你的示例文本"
is_inappropriate_chinese = Uncurse.detect(text_to_check, language="chinese")

print("Contains inappropriate content:", is_inappropriate_chinese)
```

## How It Works

### English Detection

1. **Remove Exceptions**: Exceptions listed in `exceptions.txt` are removed from the input text.
2. **Apply Character Mappings**: Multiple character mapping tables from the `maps/` folder are applied sequentially.
3. **Lowercase Conversion**: Text is converted to lowercase to normalize for case-sensitive matches.
4. **Bad Word Matching**: The text is checked against the `badwords.txt` list, and it returns whether inappropriate content is found.

### Chinese Detection

1. **Remove Exceptions**: Exceptions listed in `exceptions.txt` are removed before processing.
2. **Pinyin Conversion**: The text is converted to **pinyin** using the `pypinyin` library.
3. **Basic Matching**: The full pinyin is concatenated and checked against the `basic.txt` word list.
4. **Advanced Matching**: If no match is found, the first letter of each pinyin syllable is concatenated and checked against `advanced.txt`.

## Customization

You can easily customize Uncurse for your needs by updating the following files:

- **`badwords.txt`**: Add or remove words to match inappropriate content for a specific language.
- **`exceptions.txt`**: Add words to be excluded from detection to avoid false positives.
- **Character Mapping**: Add custom mappings in `.json` format under the `maps/` folder.

## Future Plans

- Add support for additional languages.
- Extend the character mapping functionality for other non-Latin scripts.
- Optimize the detection process for large-scale applications.

## Contributing

Feel free to fork the repository and submit pull requests for improvements or bug fixes. We welcome contributions that expand language support or enhance performance.
