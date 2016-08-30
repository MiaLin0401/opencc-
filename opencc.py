#encoding=utf-8
from opencc import OpenCC
import io

results = []
openCC = OpenCC('s2t')  # 簡體中文轉繁體中文
with io.open("wiki.zh.txt", 'r', encoding="utf-8") as inputfile:
    data = inputfile.read()

with io.open("wiki.tw.txt", 'w', encoding="utf-8") as outputfile:
    for word in data:
        outputfile.write(openCC.convert(word))

print 'ok'
