from processor import processor

training_data = open("data/train.tsv", encoding="latin-1").read()

proc = processor()

for line in training_data.splitlines()[1:]:
    split = line.split("\t")

    if len(split) < 3:
        continue

    factID = split[0]
    sentence = split[1]
    confidence = split[2]

    proc.process(sentence)
    print(proc.text)
    print(proc.text_tokens)
    print(proc.name_entities)
    print(proc.other_words)
    print("-----")
