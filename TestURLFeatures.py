

def featureURLLength(URL):
    phishing = 0
    benign = 0
    if (URL > 30):
        phishing = phishing + 1
    else:
        benign = benign + 1




benignURLtrain = open('benign_train_data.txt', 'r')
phishingURLtrain = open('phishing_train_data.txt', 'r')
URL = 10
featureURLLength(URL)