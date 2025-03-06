import re

# 設定目標中文字，請按需求修改
target_character = "道"

# 指定文字檔檔名或路徑
filename = "道德經.txt"

# 定義前後需要取得的字數
context_len = 5

# 讀取檔案內容
with open(filename, "r", encoding="utf-8") as file:
    content = file.read()

# 利用 re.finditer 搜尋所有目標中文字的位置
matches = list(re.finditer(re.escape(target_character), content))

if not matches:
    print(f"在檔案中找不到目標中文字「{target_character}」。")
else:
    for match in matches:
        start_index = match.start()  # 目標中文字的起始位置
        # 取出目標中文字前後的片段
        before = content[max(0, start_index - context_len) : start_index]
        after = content[start_index + len(target_character) : start_index + len(target_character) + context_len]
        snippet = before + target_character + after
        print(f"位於位置 {start_index} 的片段：{snippet}")