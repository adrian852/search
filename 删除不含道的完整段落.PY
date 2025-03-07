# -*- coding: utf-8 -*-
import re

# 指定來源檔案與輸出檔案路徑
input_filename = "cleaned_text.txt"      # 原始文字檔
output_filename = "filtered_道.txt"  # 輸出只含有目標段落的文字檔

# 指定要搜尋的目標中文字
target_character = "道"

# 讀取來源檔案內容
with open(input_filename, "r", encoding="utf-8") as infile:
    content = infile.read()

# 根據空白行分割段落
# 若你的段落是以其他方式區分，請修改下行
paragraphs = content.split("\n\n")

# 過濾段落：只保留含有目標中文字的段落
filtered_paragraphs = []
for paragraph in paragraphs:
    if target_character in paragraph:
        filtered_paragraphs.append(paragraph)

# 將剩餘的段落依原有的分隔符號合併後寫入新的檔案中
with open(output_filename, "w", encoding="utf-8") as outfile:
    outfile.write("\n\n".join(filtered_paragraphs))

print(f"已處理完畢，僅留下含有 '{target_character}' 的段落，結果存入 {output_filename}")