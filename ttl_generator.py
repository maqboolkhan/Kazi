class ttlGenerator:
    'Class for generating ttl file'

    def __init__(self, filename):
        self.filename = filename
        f = open(filename + '.ttl', "w")
        f.close()

    def addFact(self, factID, truthValue, confidence):
        f = open(self.filename + '.ttl', "a")
        f.write('<http://swc2017.aksw.org/task2/dataset/'+str(factID)+'> ' + '<http://swc2017.aksw.org/has'+truthValue+'> ' + '"'+str(confidence)+'"' + '^^<http://www.w3.org/2001/XMLSchema#double> .\n')
        f.close()



