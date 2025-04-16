
class DecisionTree:

    def __init__(self, extractor):
        self.extractor = extractor

        self.features = [self.extractor.containsWWW,
                         self.extractor.containsHTTPS,
                         self.extractor.containsAtSymbol]



    def runTraining(self, url, label):
        for feature in self.features:
            result = feature(url, label)
            print(feature)
            #print("result" + str(result))

    def runUserInput(self, url):
        for feature in self.features:
            result = feature(url)