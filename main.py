from ApplicationFeatureExtraction import ApplicationFeatureExtraction
from DecisionTree import DecisionTree
from FeatureExtraction import FeatureExtraction


class Main:

    def __init__(self):
        #self.Training()
        self.Application

    def Training(self):
        url_labels = self.openDataSet()
        self.callModel(url_labels)



    def openDataSet(self):
        dataset = []
        with open('URL_train_data.txt', 'r') as URLtraindata:
            for line in URLtraindata:
                url_label = line.strip().rsplit(",", 1)

                dataset.append(url_label)
        return dataset

    def callModel(self, url_labels):
        extractor = FeatureExtraction()
        model = DecisionTree(extractor)

        for url_label in url_labels:
            model.runTraining(url_label[0], url_label[1])

    def Application(self, url):
        extractor = ApplicationFeatureExtraction()
        model = DecisionTree(extractor)


main = Main()