from konlpy.tag import Okt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer


def showForKeyBERT(doc):

    #1. 형태소 분석기를 통한 명사 추출 문서
    okt = Okt()
    tokenized_doc = okt.pos(doc)
    tokenized_nouns = ' '.join([word[0] for word in tokenized_doc if word[1] == 'Noun'])
    #print('명사 추출 :', tokenized_nouns)

    # 2. 사이킷런의 CountVectorizer를 사용해 단어를 추출.
    n_gram_range = (1, 1)
    count = CountVectorizer(ngram_range=n_gram_range).fit([tokenized_nouns])
    candidates = count.get_feature_names_out()
    #print('trigram 개수 :', len(candidates))
    #print('trigram 다섯개만 출력 :', candidates[:5])

    # 3. 문서와 문서로부터 추출한 키워드들을 SBERT를 통해 수치화함. 한국어 포함 다국어 SBERT 로드
    model = SentenceTransformer('sentence-transformers/xlm-r-100langs-bert-base-nli-stsb-mean-tokens')
    doc_embedding = model.encode([doc])
    candidate_embeddings = model.encode(candidates)

    #4. 문서와 가장 유사한 키워드 추출.
    top_n = 10
    distances = cosine_similarity(doc_embedding, candidate_embeddings)
    keywords = [candidates[index] for index in distances.argsort()[0][-top_n:]]
    #print(keywords)    #배열형식으로 나옴
    htag_string = " "
    for htag in keywords:
        htag_string = htag_string + " " + htag
    print("텍스트에서 키워드 추출")
    print(htag_string)

    return htag_string 
