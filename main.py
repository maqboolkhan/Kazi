# Builtin
import sys

# 3rd parties
import wikiparser as wp

from ttl_generator import TtlGenerator
from processor import Processor


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
    except:
        # Exception can be raise if search term (Subject) returns
        # multiple search result
        return -1

    for entity in entities[1:]:
        if entity.strip():
            if content.find(entity) > -1:
                weight = 1
    return weight


if __name__ == "__main__":
    """
        Script only takes one argument which should be 
        either train or test and all extra arguments
        would be ignore
    """
    if len(sys.argv) > 1 and ['train', 'test'].index(sys.argv[1]) != -1:
        option = sys.argv[1]
        training_data = open("data/" + option + ".tsv", encoding="latin-1").read()
        processor = Processor()
        ttl_writer = TtlGenerator("result_" + option)

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
    else:
        print("No or Invalid arguments provided! \ntry: \n\tpython3 main.py train \nor\n\tpython3 main.py test")
