def is_anagram(str1,str2):
    sortedstr1 = sorted(str1)
    sortedstr2 = sorted(str2)
    if sortedstr1 == sortedstr2:
        return True
    else:
        return False
    
a = is_anagram("listen","lusten")
print(a)
