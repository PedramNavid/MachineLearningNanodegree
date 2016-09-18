import re
from collections import OrderedDict
def count_words(s, n):
    split =  re.split("\W+", s)
    cnt = [split.count(word) for word in split]
    word_cnt = zip(split, cnt)
    cnt_no_dupes = list(OrderedDict.fromkeys(word_cnt))
    cnt_sort_alpha = sorted(cnt_no_dupes)
    return sorted(cnt_sort_alpha, key=lambda x: x[1], reverse = True)[0:n]
    
    
print count_words("betty bought a bit of butter but the butter was bitter",3)
