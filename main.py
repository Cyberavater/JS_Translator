import re
import deepl

input_filepath = input("")  # "Remove web limits(modified).user.js"

output_file = "[Translated].".join(input_filepath.split(".", 1))

with open(input_filepath, "r", encoding="utf8") as in_file:
    context = in_file.read()

chinese_texts = re.findall(r'[\u4e00-\u9fff]+', context)
translated_texts = {}

for chinese_text in chinese_texts:
    translated_texts[chinese_text] = deepl.translate(source_language="ZH", target_language="EN", text=chinese_text, formality_tone="informal")

for chinese_text, translated_text in dict.items(translated_texts):
    print(chinese_text, translated_text)
    context = context.replace(chinese_text, translated_text)

with open(output_file, "w", encoding="utf8") as out_file:
    context = in_file.write(context)
