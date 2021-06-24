# TextRank
TexRank extracts important words using co-occurence between words in a sentence. It is based on words frequency.
This code extracts important keywords using TextRank Algorithm. The code is based on Korean data(Youtube Description data)

I referenced this site :https://lovit.github.io/nlp/2019/04/30/textrank/

Data: Description data of Youtube video (Beauty field like review of production, make-up)

<h2>Input type, output type of functions </h2>

<h3>main_.py</h3>
<h4>textrank(file name of title, the number of data)</h4>
<h4>    return) dataframe type of result, list of textrank keywords, list of brand</h4>
<br>
<h4>ExtranctKeywords(str type)</h4>
<h4>return) list of keywords, list of brand</h4>

<br>

<h3>PreProc.py
<h4>divided_by_sentence(str type)</h4>
<h4>return) sentences splited by kss</h4>
<br> 
<h4>PreProcess(str type)</h4>
<h4>return) str type</h4>
<br>
<h4>PreProc_apply(file name of title, the number of data)</h4>
<h4>return) list of title, list of data</h4>
<h4>*example list of data : ['content of data1' , 'content of data2']</h4>
    <br>
<h4>remove_stopwords(list of keywords)</h4>
<h4>return) list of keywords</h4>

<br>
<h3>textrank.py</h3>
<h4>tokenize(str type) #using kkma</h4>
<h4>return) list of noun</h4>
    <br>
<h2>brand, stopwords text file</h2>
brand_dic.txt: cowling brand name from the site: powder room. If you want to use this file to extract brand name using kkma, you have to extra this file on noun dictionary of kkma. <br>
stopwords_total: to remove not meaningful keywords
  
  
