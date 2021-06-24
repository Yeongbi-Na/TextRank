# TextRank
TexRank extracts important words using co-occurence between words in a sentence. It is based on words frequency.
This code extracts important keywords using TextRank Algorithm. The code is based on Korean data(Youtube Description data)

I referenced this site :https://lovit.github.io/nlp/2019/04/30/textrank/

Data: Description data of Youtube video (Beauty field like review of production, make-up)

<h2>Input type, output type of functions </h2>
<main.py>
<h1>textrank(file name of title, the number of data)</h1>


return) dataframe type of result, list of textrank keywords, list of brand



ExtranctKeywords(str type)

return) list of keywords, list of brand

<h4><PreProc.py></h4>
divided_by_sentence(str type)


return) sentences splited by kss

PreProcess(str type)


return) str type

PreProc_apply(file name of title, the number of data)


return) list of title, list of data


*example list of data : ['content of data1' , 'content of data2']

remove_stopwords(list of keywords)


return) list of keywords

<h1><textrank.py></h1>
tokenize(str type) #using kkma
return) list of noun
