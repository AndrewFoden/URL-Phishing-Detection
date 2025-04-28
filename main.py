from ApplicationFeatureExtraction import ApplicationFeatureExtraction
from DecisionTree import DecisionTree
from FeatureExtraction import FeatureExtraction
from UserInterface import UserInterface


class Main:

    def __init__(self, extractor):
        #self.Training()
        #print("init")
        self.url_input = None
        self.extracted_features = []
        #self.openDataSet()  #Tests Model
        self.Application() #Runs Application


    def openDataSet(self):
        dataset = []
        correctNoPrediction = 0
        incorrectNoPrediction = 0
        TP = 0
        TB = 0
        FP = 0
        FB = 0
        extractor = ApplicationFeatureExtraction()
        model = DecisionTree()
        with open('URL_test_data.txt', 'r') as URLtraindata:
            for line in URLtraindata:
                url_label = line.strip().rsplit(",", 1)

                features = extractor.getFeatures(url_label[0])
               # print(features)
                decision = model.runUserInput(features)
                #print(decision)
                if decision == "phishing" and url_label[1] == "0":
                    correctNoPrediction += 1
                    TP += 1
                elif decision == "benign" and url_label[1] == "1":
                    correctNoPrediction += 1
                    TB += 1
                elif decision == "phishing" and url_label[1] == "1":
                    incorrectNoPrediction += 1
                    FP += 1
                elif decision == "benign" and url_label[1] == "0":
                    incorrectNoPrediction += 1
                    FB += 1

        print("Model Test")
        print("True Phishing: " + str(TP))
        print("True Benign: " + str(TB))
        print("False Phishing: " + str(FP))
        print("False Benign: " + str(FB))
        print("Correctly predicted: " + str(correctNoPrediction))
        print("Incorrectly predicted: " + str(incorrectNoPrediction))
        total = TP + TB + FP + FB
        accuracy = (correctNoPrediction / total) * 100
        print("Accuracy: " + str(accuracy) + "%")

    def callModel(self, url_labels):
        extractor = FeatureExtraction()
        model = DecisionTree(extractor)

        for url_label in url_labels:
            model.runTraining(url_label[0], url_label[1])

    def Application(self):
        interface = UserInterface(input_callback = self.urlInput)
        #print("Application")
        #interface.LoadWindow()


    def urlInput(self, urlinput):
        self.url_input = urlinput
        #print(self.url_input)
        extractor = ApplicationFeatureExtraction()
        features = extractor.getFeatures(self.url_input)
        #print(features)
        model = DecisionTree()
        decision = model.runUserInput(features)
        #print(decision)
        return decision

        #self.url_input = urlinput




main = Main(extractor=FeatureExtraction())