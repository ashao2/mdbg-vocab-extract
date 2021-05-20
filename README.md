# mdbg-vocab-extract
mdbg_annotate.py is a Python script that extracts characters, pinyin, and definitions from MDBG using beautifulsoup. The results will be returned in results.py after being reformatted.

To use the script, run python3 mdbg_annotate.py &lt;"mdbg url"&gt;.
  
The URL can be obtained by pasting words into the MDBG dictionary and then copying the URL generated for the query. Ensure that you put quotation marks around the URL or else it will not parse correctly. Below is an example:
  
"https://www.mdbg.net/chinese/dictionary?page=worddict&wdrst=0&wdqb=%E8%B8%8F%E5%AE%9E+%E5%8F%8B%E5%A5%BD+%E6%9E%81%E4%B8%BA+%E6%88%91%E7%9A%84+%E4%BF%A1%E7%94%A8%E5%8D%A1+%E6%89%80"
