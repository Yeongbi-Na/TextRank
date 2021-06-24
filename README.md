# TextRank
Extracting important keywords using TextRank Algorithm. The code is based on Korean data(Youtube Description data)

I referenced this site :https://lovit.github.io/nlp/2019/04/30/textrank/

Data: Description data of Youtube video (Beauty field like review of production, make-up)

<h2>input type, output type of functions </h2>
<main.py>
textrank(file name of title, the number of data)
> dataframe type of result, list of textrank keywords, list of brand

ExtranctKeywords(str type)
> list of keywords, list of brand

<PreProc.py>
divided_by_sentence(str type)
> sentences splited by kss

PreProcess(str type)
>> str type

PreProc_apply(file name of title, the number of data)
>> list of title, list of data
*example list of data : ['content of data1' , 'content of data2']

remove_stopwords(list of keywords)
>> list of keywords

<textrank.py>
tokenize(str type) #using kkma
>> list of noun
