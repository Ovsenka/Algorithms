# s_num is number for searching
# Base: len(list_) == 1: return lst[0]
# recursive: return lst[0:lst.index(half)] if half >= s_num else lst[lst.index(half):lst[-1]]