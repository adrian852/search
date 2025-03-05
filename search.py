import re

target_character = "道"
# 檔案名稱，請依需求修改

filename = "道德經.txt"

# 使用 re.escape 來處理特殊字元（雖然中文通常不用，但可保險起見）
punctuation_pattern = re.compile(r'[^\w\s]', re.UNICODE)

# 2. 用來搜尋目標中文字，先用 re.escape 處理特殊字元（中文通常無需，但較保險）
target_pattern = re.compile(re.escape(target_character))

print(f"包含特定中文字 '{target_character}' 的行（去除標點後）：")
with open(filename, "r", encoding="utf-8") as file:
    for line_num, line in enumerate(file, start=1):
        # 去除行中的標點符號
        line_clean = punctuation_pattern.sub('', line)
        # 若該行含有目標中文字，則列印行號與內容
        if target_pattern.search(line_clean):
            print(f"第 {line_num} 行 : {line_clean.strip()}")

print("\n-----\n")

# --- 方式二：統計整個檔案中目標中文字的出現次數（去除標點後） ---
with open(filename, "r", encoding="utf-8") as file:
    text = file.read()

# 清除整個文字檔的標點符號
text_clean = punctuation_pattern.sub('', text)
# 使用 findall 尋找所有目標中文字匹配項
occurrences = target_pattern.findall(text_clean)
print(f"在整個去除標點後的檔案中，'{target_character}' 出現的次數為：{len(occurrences)}")