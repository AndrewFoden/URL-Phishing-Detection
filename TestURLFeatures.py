

URL = []
predictphishing = 0
predictbenign = 0

def featureURLLength(URL):
    #print(URL)
    if len(URL) > 30:
        label = "phishing"
    else:
        label = "benign"
    return label



#benignURLtrain = open('benign_train_data.txt', 'r')
#phishingURLtrain = open('OnlyURL_phishing_train_data.txt', 'r')
with open('OnlyURL_phishing_train_data.txt', 'r') as phishingURLtrain:
    for line in phishingURLtrain:
        #URL.append(line)
        label = featureURLLength(line)
        if label == "phishing":
            predictphishing += 1
        else:
            predictbenign += 1

print(predictphishing)
print(predictbenign)