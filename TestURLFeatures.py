


TP = 0 #TruePhishing = Labelled as phishing, is phishing
FP = 0 #FalsePhishing = Labelled as phishing, is Benign
TB = 0 #TrueBenign = Labelled as benign, is benign
FB = 0 #FalseBenign = Labelled as benign, is phishing


def featureURLLength(URL, label):
    #print(URL)
    decision = ""
    if len(URL) > 30:
        if label == "0":
            decision = "TruePhishing"
        if label == "1":
            decision = "FalseBenign"
    else:
        if label == "0":
            decision = "FalsePhishing"
        if label == "1":
            decision = "TrueBenign"

    return decision

#label 1 = benign
#label 0 = phishing



#benignURLtrain = open('benign_train_data.txt', 'r')
#phishingURLtrain = open('OnlyURL_phishing_train_data.txt', 'r')
with open('URL_train_data.txt', 'r') as URLtraindata:
    for line in URLtraindata:
        url_label = line.strip().split(",")
        decision = featureURLLength(url_label[0], url_label[1])

        if decision == "TruePhishing":
            TP += 1
        elif decision == "FalsePhishing":
            FP += 1
        elif decision == "TrueBenign":
            TB += 1
        elif decision == "FalseBenign":
            FB += 1


print("TruePhishing: " + str(TP))
print("FalsePhishing: " + str(FP))
print("TrueBenign: " + str(TB))
print("FalseBenign: " + str(FB))
