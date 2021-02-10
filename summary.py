import jieba.analyse
import wordcloud
import time

with open('record/history.txt', 'r') as f:
    original = ''.join(f.readlines())
    text = original.replace('\n', ' ')

key = jieba.analyse.extract_tags(text, topK=8)
wc = wordcloud.WordCloud().generate(text)
wc.to_image().show()
filename = time.strftime("%Y%m%d_%H%M%S", time.localtime())
file = open('results/' + filename + '.txt', 'w')
file.write('KEYWORDS:\n' + ' '.join(key) + '\n\n')
file.write('CLASS RECORD:\n')
file.writelines(original)
file.close()
f.close()
print(key)
