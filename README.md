# TextRank
TexRank extracts important words using co-occurence between words in a sentence. It is based on words frequency.
This code extracts important keywords using TextRank Algorithm. The code is based on Korean data(Youtube Description data)

I referenced this site :https://lovit.github.io/nlp/2019/04/30/textrank/

Data: Description data of Youtube video (Beauty field like review of production, make-up)

<h2>Input type, output type of functions </h2>

<h3>main_.py
<h4>textrank(file name of title, the number of data)</h4>
return) dataframe type of result, list of textrank keywords, list of brand
<h4>ExtranctKeywords(str type)</h4>
return) list of keywords, list of brand



>PreProc.py
<h4>divided_by_sentence(str type)</h4>
return) sentences splited by kss

<h4>PreProcess(str type)</h4>
return) str type
<h4>PreProc_apply(file name of title, the number of data)</h4>
return) list of title, list of data
*example list of data : ['content of data1' , 'content of data2']
<h4>remove_stopwords(list of keywords)</h4>
return) list of keywords

>textrank.py
<h4>tokenize(str type) #using kkma</h4>
return) list of noun
