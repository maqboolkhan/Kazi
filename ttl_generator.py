class TtlGenerator:
    # Class for generating ttl file

    def __init__(self, filename):
        self.filename = filename
        self.f = open(filename + '.ttl', "w")

    def addFact(self, factID, truthValue, confidence):
        self.f.write('<http://swc2017.aksw.org/task2/dataset/'+str(factID)+'> ' + '<http://swc2017.aksw.org/has'+truthValue+'> ' + '"'+str(confidence)+'"' + '^^<http://www.w3.org/2001/XMLSchema#double> .\n')

    def closeFile(self):
        self.f.close()
