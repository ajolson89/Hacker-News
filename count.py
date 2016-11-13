import pandas as pd
import numpy as np
import read
from collections import Counter
import operator

if __name__ == "__main__":
    df = read.load_data()
    emp_str = ""
    for row in df['headline']:
        emp_str = emp_str + ' ' + str(row)
    words = emp_str.lower().split()
    dic_words = Counter(words).most_common(100)
    #sorted_dic = sorted(dic_words.items(), key=operator.itemgetter(1))
    common_word = [x[0] for x in dic_words]
    print (common_word)