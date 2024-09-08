import Uncurse

# Detect English text
text_to_check = "10ser"
is_inappropriate_english = Uncurse.detect(text_to_check, language="english")

if is_inappropriate_english:
    print("Inappropriate English text detected.")
else:
    print("English text is clean.")

# Detect Chinese text
chinese_text_to_check = "生病"
is_inappropriate_chinese = Uncurse.detect(chinese_text_to_check, language="chinese")

if is_inappropriate_chinese:
    print("Inappropriate Chinese text detected.")
else:
    print("Chinese text is clean.")
