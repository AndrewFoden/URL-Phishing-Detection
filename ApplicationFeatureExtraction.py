
class ApplicationFeatureExtraction:

    def getDomain(self, url):
        removedprotocolURL = url.replace("https://", "").replace("http://", "")
        domain = removedprotocolURL.split("/")[0]
        return domain

    def URLLength(self, URL):
        if len(URL) >= 40:
            return "Phishing"
        else:
            return "Benign"

    def containsAtSymbol(self, URL):
        if "@" in URL:
            return "Phishing"
        else:
            return "Benign"

    def containsHTTPS(self, URL):
        if "https" in URL:
            return "Benign"
        else:
            return "Phishing"

    def containsURLshortening(self, URL):
        decision = ""
        urlshorteningservices = ["tinyurl.com", "rebrand.ly", "ow.ly", "bit.ly", "shorturl.at", "shorturl.ac", "bl.ink",
                                 "t2m.io", "dub.sh", "short.gy", "short.io", "is.gd", "dweb.link"]

        for shorteningservice in urlshorteningservices:
            if shorteningservice in URL:
                return "Phishing"
        return "Benign"

    def containsWWW(self, URL):
        if "www." in URL:
            return "Benign"
        else:
            return "Phishing"

    def domainLength(self, domain):
        if len(domain) <= 33:
            return "Benign"
        else:
            return "Phishing"

    def suffixInDomain(self, domain):
        if "-" in domain:
            return "Phishing"
        else:
            return "Benign"


def TestDecisionTree(self=None):
    correctDecision = 0
    incorrectDecision = 0
    with open('URL_test_data.txt', 'r') as URLtraindata:
        for line in URLtraindata:
            url_label = line.strip().rsplit(",", 1)
            decision = ApplicationFeatureExtraction.containsWWW(self, url_label[0])  # 1st layer
            if url_label[1] == 1 and decision == "Benign":
                correctDecision += 1
            else:
                decision = ApplicationFeatureExtraction.containsHTTPS(self, url_label[0])  # 2nd layer
                if url_label[1] == 1 and decision == "Benign":
                    correctDecision += 1
                else:
                    decision = ApplicationFeatureExtraction.containsAtSymbol(self, url_label[0])  # 3rd layer
                    if url_label[1] == 1 and decision == "Benign":
                        correctDecision += 1
                    else:
                        decision = ApplicationFeatureExtraction.containsURLshortening(self, url_label[0])  # 4th layer
                        if url_label[1] == 1 and decision == "Benign":
                            correctDecision += 1
                        else:
                            decision = ApplicationFeatureExtraction.URLLength(self, url_label[0]) #5th layer
                            if url_label[1] == 1 and decision == "Phishing":
                                correctDecision += 1
                            else:
                                domain = ApplicationFeatureExtraction.getDomain(self, url_label[0])
                                decision = ApplicationFeatureExtraction.suffixInDomain(self, domain)  # 6th layer
                                if url_label[1] == 1 and decision == "Phishing":
                                    correctDecision += 1
                                else:
                                    domain = ApplicationFeatureExtraction.getDomain(self, url_label[0])
                                    decision = ApplicationFeatureExtraction.domainLength(self, domain)  # 7th layer


testdecisiontree = TestDecisionTree()
