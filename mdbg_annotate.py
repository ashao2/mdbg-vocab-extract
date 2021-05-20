import sys
import requests
from bs4 import BeautifulSoup

assert len(sys.argv) == 2

URL = sys.argv[1]

assert "www.mdbg.net" in URL

#URL = "https://www.mdbg.net/chinese/dictionary?page=worddict&wdrst=0&wdqb=%E4%B8%96%E7%95%8C+%E6%B8%A9%E6%9A%96+%E7%83%AD%E7%88%B1+%E9%81%BF%E5%85%8D+%E6%8B%89%E5%BC%80"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

char_py_list = list()
def_list = list()

# <div> will class = "head"
results = soup.find_all(class_="head")
for head in results:
    #char = head.find_all(class_="hanzi")

    # <div> with class = "hanzi"
    hanzi = head.select(".hanzi")
    for zi in hanzi:
        # <span> with class "mpt*"
        characters = zi.select(".mpt1, .mpt2, .mpt3, .mpt4, .mpt, .mpt5")
        #chars = char.select(".mpt1", ".mpt2", ".mpt3", ".mpt4", ".mpt", ".mpt5")
        #print(characters, end='\n'*2)
        word = ""
        for each_char in characters:
            word = word + each_char.text
        #print(word)

    pinyin = head.select(".pinyin")
    for py in pinyin:
        syllables = py.select(".mpt1, .mpt2, .mpt3, .mpt4, .mpt, .mpt5")

        full = ""
        for each_syll in syllables:
            full = full + each_syll.text

        char_py_joint = word + " " + full
        char_py_list.append(char_py_joint)
        #print(char_py_joint)

res2 = soup.find_all(class_="details")
for details in res2:
    definition = details.select(".defs")

    for meaning in definition:
        def_list.append(meaning.text)

with open('results.txt', 'w') as res_doc:
    for int in range(len(def_list)):
        final = char_py_list[int] + " - " + def_list[int] + "\n"
        res_doc.write(final)
