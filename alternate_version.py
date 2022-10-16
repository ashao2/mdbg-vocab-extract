import sys
import requests
import re
from bs4 import BeautifulSoup

# Example: python3 alternate_version.py "一切都是最好的安排"

assert len(sys.argv) == 2

vocab = sys.argv[1]

URL = "https://www.mdbg.net/chinese/dictionary?page=worddict&wdrst=0&wdqb=" + vocab
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
    characters = zi.find_all("span", class_=re.compile("mpt[0-9]*"))
    word = ""
    for each_char in characters:
      word = word + each_char.text

  pinyin = head.select(".pinyin")
  for py in pinyin:
    syllables = py.find_all("span", class_=re.compile("mpt[0-9]*"))

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
    def_list.append(meaning.text.replace('  ', ' '))

# Write to file
#with open('results.txt', 'w') as res_doc:
#    for int in range(len(def_list)):
#        final = char_py_list[int] + " - " + def_list[int] + "\n"
#        res_doc.write(final)

# Print results
for int in range(len(def_list)):
  final = char_py_list[int] + " - " + def_list[int] #+ "\n"
  print(final)
