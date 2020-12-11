from fuzzywuzzy import fuzz

ratio = fuzz.ratio("P.F. Chang's", "PF Changs")
print(ratio)
ratio = fuzz.partial_ratio("P.F. Chang's", "PF Changs")
print(ratio)
ratio = fuzz.token_set_ratio("P.F. Chang's", "PF Changs")
print(ratio)
ratio = fuzz.token_sort_ratio("P.F. Chang's", "PF Changs")
print(ratio)
ratio = fuzz.token_sort_ratio("Chick Fil A", "Chick-Fil-A")
print(ratio)
ratio = fuzz.partial_ratio("Bob Evans", "Bob Evans Restaurant")
print(ratio)
