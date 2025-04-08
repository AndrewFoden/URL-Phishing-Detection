


TP = 0 #TruePhishing = Labelled as phishing, is phishing. Detected correctly
FP = 0 #FalsePhishing = Labelled as phishing, is Benign. Not Detected correctly
TB = 0 #TrueBenign = Labelled as benign, is benign. Detected correctly
FB = 0 #FalseBenign = Labelled as benign, is phishing. Not Detected correctly


def featureURLLength(URL, label):
    #print(URL)
    decision = ""
    if len(URL) >= 40:
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

def containsAtSymbol(URL, label):
    decision = ""

    if "@" in URL:
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

def presenceOfHTTPS(URL, label):
    decision = ""

    if "https" in URL:
        if label == "1":
            decision = "TrueBenign"
        if label == "0":
            decision = "FalsePhishing"
    else:
        if label == "1":
            decision = "FalseBenign"
        if label == "0":
            decision = "TruePhishing"

    return decision

def URLshortening(URL, label):
    decision = ""
    urlshorteningservices = ["tinyurl.com", "rebrand.ly", "ow.ly", "bit.ly", "shorturl.at", "shorturl.ac", "bl.ink",
                             "t2m.io", "dub.sh", "short.gy", "short.io", "is.gd", "dweb.link"]

    for shorteningservice in urlshorteningservices:
        if shorteningservice in URL:
            if label == "0":
                decision = "TruePhishing"
            if label == "1":
                decision = "FalseBenign"
    if decision == "":
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
        url_label = line.strip().rsplit(",", 1)

        #decision = featureURLLength(url_label[0], url_label[1])
        #decision = containsAtSymbol(url_label[0], url_label[1])
        #decision = presenceOfHTTPS(url_label[0], url_label[1])
        decision = URLshortening(url_label[0], url_label[1])

        if decision == "TruePhishing":
            TP += 1
        elif decision == "FalsePhishing":
            FP += 1
        elif decision == "TrueBenign":
            TB += 1
        elif decision == "FalseBenign":
            FB += 1
        else:
            print("Not Work: " + str(url_label))

print("TruePhishing: " + str(TP))
print("FalsePhishing: " + str(FP))
print("TrueBenign: " + str(TB))
print("FalseBenign: " + str(FB))
