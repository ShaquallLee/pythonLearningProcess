from fuzzywuzzy import fuzz, process


def getMaxSimilarityByFuzzy(text, lists):
    '''
    从lists中使用fuzzywuzzy库（编辑距离）来计算得到最大相似度
    :param text:
    :param lists:
    :return:
    '''
    sim = process.extractOne(text, lists)
    print(sim[1]/100)


def getSimilarityByFuzzy(text1, text2):
    '''
    使用fuzzywuzzy封装好的编辑距离来计算文本相似度
    :param text1:
    :param text2:
    :return:
    '''
    return float(fuzz.ratio(text1, text2))/100


if __name__ == '__main__':
    getMaxSimilarityByFuzzy('12347', ['1234567','123512356', 'laidhsfof0989'])
