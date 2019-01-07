import nltk

training_data = open("data/train.tsv", encoding="latin-1").read()
print(len(training_data.splitlines()))

for sentence in training_data.splitlines():
    tokens = nltk.word_tokenize(sentence)
    print(nltk.pos_tag(tokens))
