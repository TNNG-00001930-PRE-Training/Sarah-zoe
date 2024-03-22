input_str = input("Enter a sequence of words: ")
words_list = input_str.split(',')
sorted_words = sorted(words_list)
print(','.join(sorted_words))
