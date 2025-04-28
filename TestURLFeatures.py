


TP = 0 #TruePhishing = Labelled as phishing, is phishing. Detected correctly
FP = 0 #FalsePhishing = Labelled as phishing, is Benign. Not Detected correctly
TB = 0 #TrueBenign = Labelled as benign, is benign. Detected correctly
FB = 0 #FalseBenign = Labelled as benign, is phishing. Not Detected correctly


def getDomain(url):
    removedprotocolURL = url.replace("https://", "").replace("http://","")
    domain = removedprotocolURL.split("/")[0]
    return domain


def URLLength(URL, label):
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

def containsHTTPS(URL, label):
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

def containsWWW(URL, label):
    decision = ""

    if "www." in URL:
        if label == "1":
            decision = "TrueBenign"
        if label == "0":
            decision = "FalsePhishing"
    else:
        if label == "0":
            decision = "TruePhishing"
        if label == "1":
            decision = "FalseBenign"

    return decision

def domainLength(domain, label):
    decision = ""

    if len(domain) <= 33:
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

def suffixInDomain(domain, label):
    decision = ""

    if "-" in domain:
        if label == "0":
            decision = "TruePhishing"
        if label == "1":
            decision = "FalseBenign"
    else:
        if label == "1":
            decision = "TrueBenign"
        if label == "0":
            decision = "FalsePhishing"

    return decision

def GiniIndex(TP, FP, TB, FB):

    left_node = TP + FB
    #print(TP)
    #print(left_node)
    p0 = (TP / left_node) ** 2
    p1 = (FB / left_node) ** 2
    #print(p0)
    #print(p1)
    left_node_gini = 1 - (p0 + p1)

    right_node = TB + FP
    p2 = (TB / right_node) ** 2
    p3 = (FP / right_node) ** 2

    right_node_gini = 1 - (p2 + p3)

    total_dataset = TP + FP + TB + FB
    left_phishing = (left_node * left_node_gini) / total_dataset
    right_benign = (right_node * right_node_gini) / total_dataset
    weighted_gini = left_phishing + right_benign

    return left_node_gini, right_node_gini, weighted_gini



#label 1 = benign
#label 0 = phishing



    #benignURLtrain = open('benign_train_data.txt', 'r')
    #phishingURLtrain = open('OnlyURL_phishing_train_data.txt', 'r')
with open('URL_train_data.txt', 'r') as URLtraindata:
    for line in URLtraindata:
        url_label = line.strip().rsplit(",", 1)

        #decision = URLLength(url_label[0], url_label[1])
        #decision = containsAtSymbol(url_label[0], url_label[1])
        #decision = containsHTTPS(url_label[0], url_label[1])
        #decision = URLshortening(url_label[0], url_label[1])
        decision = containsWWW(url_label[0], url_label[1])
        #decision = domainLength(getDomain(url_label[0]), url_label[1])
        #decision = suffixInDomain(getDomain(url_label[0]), url_label[1])

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


left_node_gini, right_node_gini, weighted_gini = GiniIndex(TP, FP, TB, FB)

print("Feature: Length of URL")
print("TruePhishing: " + str(TP))
print("FalsePhishing: " + str(FP))
print("TrueBenign: " + str(TB))
print("FalseBenign: " + str(FB))
print("Left/Phishing Gini: " + str(left_node_gini))
print("Right/Benign Gini: " + str(right_node_gini))
print("Weighted Gini: " + str(weighted_gini))





