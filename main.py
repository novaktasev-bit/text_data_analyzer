text = "python is powerful and python is easy to learn and very useful"

words = text.split()
long_words = []
count = 0
total_length = 0
average_length = 0
longest_word = ""
freq = {}
most_used_word = ""

for w in words:
    if len(w) > 5:
        long_words.append(w)
        count = count + 1
        total_length = total_length + len(w)
    
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1


average_length = total_length/count      
longest_word = max(long_words, key=len)
most_used_word = max(freq, key = freq.get)

print ("\n === TEXT ANALYSIS REPORT === \n")

print ("Long words: ", long_words)
print ("Number of long words: ", count)
print ("Total length: ", total_length)    
print ("Average length: ", average_length)
print("Longest word: ", longest_word)

print("Most used word: ",most_used_word)
print ("Occurrences:", freq)
