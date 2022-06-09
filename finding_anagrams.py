def find_anagram(word, anagram):

    if sorted(word) == sorted (anagram): 
        return True
    else:
        return False

print(find_anagram('yam', 'may'))