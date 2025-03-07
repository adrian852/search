import re

# 設定搜尋目標中文字與前後要取得的字數
target_character = "道"
context_len = 5

# 指定先前清理過標點符號的文字檔
filename = "cleaned_text_道德經.txt"

# 讀取清理後檔案內容
with open(filename, "r", encoding="utf-8") as file:
    content = file.read()

# 利用 re.finditer 來尋找所有出現目標中文字的位置
matches = list(re.finditer(re.escape(target_character), content))

if not matches:
    print(f"在檔案中找不到目標中文字「{target_character}」。")
else:
    for match in matches:
        start_index = match.start()
        end_index = match.end()
        # 取得目標字前方 context_len 個字（不足則取剩餘部分）
        before = content[max(0, start_index - context_len) : start_index]
        # 取得目標字後方 context_len 個字（不足則取剩餘部分）
        after = content[end_index : min(len(content), end_index + context_len)]
        snippet = before + target_character + after
        print(f"目標字出現於位置 {start_index}，片段：{snippet}")
    
    # 印出搜尋到的目標字總數
    print(f"\n搜尋到 {len(matches)} 個目標文字「{target_character}」。")