import gutenbergpy.textget


raw_book = gutenbergpy.textget.get_text_by_id(208)
clean_book = gutenbergpy.textget.strip_headers(raw_book)
print(clean_book[:100])
