import nltk
from nltk.tree import Tree


class processor:
    text = ''
    text_tokens = []
    name_entities = []
    other_words = []

    def process(self, text):
        self.text = text
        self.other_words = []
        self.__create_tokens()
        self.__get_name_entities()

    def __create_tokens(self):
        self.text_tokens = nltk.word_tokenize(self.text)

    def __get_name_entities(self):
        tagged_sentence = nltk.pos_tag(self.text_tokens)
        pos_chunks = nltk.ne_chunk(tagged_sentence)
        continuous_chunk = []
        current_chunk = []
        temp = []

        for i in pos_chunks:
            if type(i) == Tree:
                current_chunk.append(" ".join([token for token, pos in i.leaves()]))
            elif current_chunk:
                named_entity = " ".join(current_chunk)
                if named_entity not in continuous_chunk:
                    continuous_chunk.append(named_entity)
                    current_chunk = []
            else:
                if i[1] == 'NNP':
                    temp.append(i[0])
                else:
                    # Collecting other important words
                    if ['J', 'N', 'R'].count(i[1][0]):
                        self.other_words.append(i[0])
                    if len(temp) == 1:
                        temp = []
                continue

        one_more = " ".join(temp)
        if continuous_chunk or current_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity)

        if len(temp) > 1:
            continuous_chunk.append(one_more)

        self.name_entities = continuous_chunk
