from wikipedia import wikipedia
from processor import Processor
import wikiparser as wp
from ttl_generator import TtlGenerator


def check(entities):
    """
        Really naive approach which first search WikiPage for the Subject
        and then try to search Object in that page and if found return
        positive confidence otherwise negative
    """
    weight = -1
    try:
        search_result = wp.search(entities[0])
        content = search_result.content
    except wikipedia.exceptions.DisambiguationError:
        # Exception can be raise if search term (Subject) returns
        return -1

    for entity in entities[1:]:
        if entity.strip():
            if content.find(entity) > -1:
                weight = 1
    return weight


if __name__ == "__main__":
    training_data = open("data/train.tsv", encoding="latin-1").read()
    processor = Processor()
    ttl_writer = TtlGenerator("result_train")

    for line in training_data.splitlines()[1:]:
        split = line.split("\t")

        if len(split) < 2:
            continue

        factID = split[0]
        sentence = split[1]

        processor.process(sentence)
        result = check(processor.name_entities)
        ttl_writer.addfact(factID, str(result))

    ttl_writer.closefile()
