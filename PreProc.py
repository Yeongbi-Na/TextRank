import kss
import pandas as pd
def divided_by_sentence(text): #문장나누기 str형
    result=kss.split_sentences(text)
    return result
    
def PreProcess(text): #str형
    temp=divided_by_sentence(text) # 문장 나누기
    data=""
    for s in temp:
        data+=s
    return data #문자열 형태


    
def PreProc_apply(title_file,n):#제목 파일명, 데이터 개수

    data=pd.read_csv(title_file, sep=",")
    content=list(data['Content'])

    title=list(data['Title'])
    content=[PreProcess(str(c)) for c in content]

    return title,content #전처리된 데이터를 list로 반환 ['data1내용','data2내용']
    
def remove_stopwords(keywords_list): #keywords 모인 리스트
    #stopwords 제거하기 
    st_file_name = "stopwords_total.txt"
    with open(st_file_name,'rt',encoding="utf8") as f:
        stopwords=f.read()
        stopwords=stopwords.split("\n")


    keywords_list=[x for x in keywords_list if x not in stopwords]
    
    return keywords_list #list형으로 반환
    
    