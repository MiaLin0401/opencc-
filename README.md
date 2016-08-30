# opencc- 中文轉換
steps：
1. https://github.com/yichen0831/opencc-python
2. 下載解壓縮後，python setup.py install
3. 將解壓縮後的資料夾中的opencc資料夾移到C:\Python27\Lib\site-packages
4. opencc.py
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

5. Conversions include 轉換包含:

'hk2s': Traditional Chinese (Hong Kong standard) to Simplified Chinese
's2hk': Simplified Chinese to Traditional Chinese (Hong Kong standard)

's2t': Simplified Chinese to Traditional Chinese
's2tw': Simplified Chinese to Traditional Chinese (Taiwan standard)
's2twp': Simplified Chinese to Traditional Chinese (Taiwan standard, with phrases)

't2hk': Traditional Chinese to Traditional Chinese (Hong Kong standard)
't2s': Traditional Chinese to Simplified Chinese
't2tw': Traditional Chinese to Traditional Chinese (Taiwan standard)

'tw2s': Traditional Chinese (Taiwan standard) to Simplified Chinese
'tw2sp': Traditional Chinese (Taiwan standard) to Simplified Chinese (with phrases)
