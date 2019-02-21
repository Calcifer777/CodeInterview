# Given a string with multiple words and spaces represented as a character array. 
# Write an in-place algorithm to reverse the order of words in the string. 
# Example: convert ['p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'm', 'a', 'k', 'e', 's', 
# ' ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e'] 
# to ['p', 'r', 'a', 'c', 't', 'i', 'c', 'e', ' ', 'm', 'a', 'k', 'e', 's', ' ', 
# 'p', 'e', 'r', 'f', 'e', 'c', 't']

def reverseTheWords(l): 
  if len(l) <= 1: 
    return l 
  i = 0 
  while i < len(l) and l[i] != ' ': 
    i += 1 
    return reverseTheWords(l[i:])+l[:i]
    
