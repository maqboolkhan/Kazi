class TtlGenerator:
    # Class for generating ttl file

    def __init__(self, filename):
        self.filename = filename
        self.f = open(filename + '.ttl', "w")

    def addfact(self, factid, confidence):
        self.f.write('<http://swc2017.aksw.org/task2/dataset/' + factid + '> '
                     + '<http://swc2017.aksw.org/hasTruthValue> '
                     + '"' + confidence + '"' + '^^<http://www.w3.org/2001/XMLSchema#double> .\n')

    def closefile(self):
        self.f.close()
