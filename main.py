from DecisionTree import DecisionTree
from FeatureExtraction import FeatureExtraction


class Main:

    def __init__(self):
        url_label = self.openDataSet()
        self.callModel(url_label)

    def openDataSet(self):
        with open('URL_train_data.txt', 'r') as URLtraindata:
            for line in URLtraindata:
                url_label = line.strip().rsplit(",", 1)
                return url_label

    def callModel(self, url_label):
        extractor = FeatureExtraction()
        model = DecisionTree(extractor)
        model.run(url_label[0], url_label[1])


main = Main()