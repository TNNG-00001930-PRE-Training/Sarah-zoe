first_sequence = input("Enter a sequence of whitespace-separated words: ")


unique_words = set(first_sequence.split())

sorted_words = sorted(unique_words)


sorted_sequence = ' '.join(sorted_words)
print(sorted_sequence)
