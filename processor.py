import nltk
from nltk.tree import Tree


class Processor:
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
        print(pos_chunks)
        entities = []
        continuous_chunk = []
        other_entities = []
        word = ""

        for i in pos_chunks:
            if type(i) == Tree:
                # Because if two or more NNP appears before NE they can be a part of entity
                if other_entities:
                    word = " ".join(other_entities)
                    other_entities = []

                word += " " + " ".join([token for token, pos in i.leaves()])
                continuous_chunk.append(word)
                word = ""
            else:
                if continuous_chunk:
                    if i[1] == 'NNP':
                        continuous_chunk.append(i[0])
                        continue

                    entity = " ".join(continuous_chunk).strip()
                    if entity:
                        entities.append(entity)
                    continuous_chunk = []

                # Because if two or more NNP appears together they can be a entity
                if i[1] == 'NNP':
                    other_entities.append(i[0])
                else:
                    # Collecting other important words
                    if ['J', 'N', 'R'].count(i[1][0]):
                        self.other_words.append(i[0])
                    if len(other_entities) == 1:
                        other_entities = []

        other_entity = " ".join(other_entities)

        if other_entity:
            entities.append(other_entity)
        self.name_entities = entities
