import re

# 指定來源檔案與輸出檔案路徑
input_filename = "道德經.txt"             # 請替換成你的文言文檔案名稱
output_filename = "filtered_道德經_虛詞.txt"    # 輸出過濾後結果的檔案

# 定義常見的文言文虛詞（停用詞）清單，依需求可增刪
wenyan_stopwords = [
    "之", "乎", "者", "也", "矣", "焉", "哉", "耳",
    "以", "而", "乃", "則", "所", "其", "斯", "然"
]

# 讀取來源檔案內容
with open(input_filename, "r", encoding="utf-8") as infile:
    text = infile.read()

# 建構正規表達式模式，將所有虛詞以 OR 串接，若需要完整單詞匹配可加入邊界(\b)
# 注意：對文言文而言，因為字和詞之間沒有明顯的空白，通常逐一字移除即可
pattern = re.compile("|".join(map(re.escape, wenyan_stopwords)))

# 利用正規表達式替換所有虛詞為空字串
filtered_text = pattern.sub("", text)

# 將過濾後的結果寫入新的輸出檔案
with open(output_filename, "w", encoding="utf-8") as outfile:
    outfile.write(filtered_text)

print(f"文言文虛詞過濾完成，結果存入：{output_filename}")