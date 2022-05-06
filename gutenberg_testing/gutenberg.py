import gutenbergpy.textget

ids = [208,
2833,
1093,
1190,
432,
178,
2870,
2834,
2715,
211,
4264,
177,
7118,
645,
29452,
642,
39316,
19717,
1032,
38776,
6354,
33727,
1144,
179,
898,
30059,
176,
2425,
54136,
58471,
2327]

for id in ids:
    raw_book = gutenbergpy.textget.get_text_by_id(id)
    clean_book = gutenbergpy.textget.strip_headers(raw_book)
    clean_book = clean_book.decode('UTF-8')
    with open(f'{id}.txt', 'w') as f:
        f.write(clean_book)
    
    

#raw_book = gutenbergpy.textget.get_text_by_id(208)
#clean_book = gutenbergpy.textget.strip_headers(raw_book)
