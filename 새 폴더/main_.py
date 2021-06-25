import PreProc as pp
import textrank as tr
from pandas import DataFrame as df

def ExtranctKeywords(text): #str형
    text_list=text.split('.')
    keywords, brand=tr.textrank_keyword(text_list, tr.tokenize, 1, window=1, min_cooccurrence=0, df=0.85, max_iter=30, topk=100) 
    result=[keywords[i][0] for i in range(len(keywords))]
    return result,brand #keywords를 list로 반환



def textrank(title,n): #제목파일명, 데이터개수
    #전처리
    title, data=pp.PreProc_apply(title,n)


    #키워드 추출 & 불용어 제거 & & 브랜드명 추출 & textrank 적용
    tr_keywords_list=[]
    brand=[]
    for i in range(n):
        k_temp, b_temp=ExtranctKeywords(data[i])
        tr_keywords_list.append(k_temp)
        brand.append(b_temp)

    result=df(data={'title':title, 'hashtag_30':tr_keywords_list, 'brand': brand})
    return result, tr_keywords_list, brand #dataframe/ keywords/brand keywords 반환





#textrank("최종데이터파일명.csv",데이터개수)
#output총3개 >>>>> result: 최종결과물 dataframe/tr_keywrods_list:textrank결과 키워드/brand_keywords: 브랜드명 키워드
result, tr_keywords_list, brand_keywords=textrank("data.csv",50)
result.to_csv('textrank_original_0605.csv', index=False, encoding='utf-8')