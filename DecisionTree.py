
class DecisionTree:

    def __init__(self):
        pass



    def runTraining(self, url, label):
        for feature in self.features:
            result = feature(url, label)

            #print("result" + str(result))

    def runUserInput(self, features):

        for feature in features:
            if feature == "Phishing":
                return "phishing"
        return "benign"


