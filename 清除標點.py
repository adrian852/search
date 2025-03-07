import re

# 指定來源檔案路徑與輸出檔案路徑
input_filename = "道德經.txt"
output_filename = "cleaned_text.txt"

# 定義正規表達式：
# 本模式會移除所有非中文字（範圍：\u4e00-\u9fff）、非英數字、非底線與非空白字元，
# 這樣能移除大部分的標點符號。
punctuation_pattern = re.compile(r'[^\u4e00-\u9fff\w\s]', re.UNICODE)

# 讀取來源檔案內容
with open(input_filename, "r", encoding="utf-8") as infile:
    content = infile.read()

# 移除標點符號
cleaned_content = punctuation_pattern.sub('', content)

# 將清除標點後的內容存入新的檔案中
with open(output_filename, "w", encoding="utf-8") as outfile:
    outfile.write(cleaned_content)

print(f"已完成標點符號移除，清除結果存入：{output_filename}")