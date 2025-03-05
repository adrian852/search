import re

target_character = "道"
# 檔案名稱，請依需求修改

filename = "道德經.txt"

# 使用 re.escape 來處理特殊字元（雖然中文通常不用，但可保險起見）
pattern = re.compile(re.escape(target_character))

print(f"包含特定中文字 '{target_character}' 的行：")
with open(filename, "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        if pattern.search(line):
            print(f"第 {line_number} 行 : {line.strip()}")

with open(filename, "r", encoding="utf-8") as file:
    content = file.read()

occurrences = pattern.findall(content)
print(f"\n在整個檔案中，'{target_character}' 出現的次數為：{len(occurrences)}")