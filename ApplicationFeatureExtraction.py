
class ApplicationFeatureExtraction:

    def __init__(self):
        self.features = []

    def getFeatures(self, url):
        self.features = [
            self.containsWWW(url),
            self.containsHTTPS(url),
            self.containsAtSymbol(url),
            self.containsURLshortening(url),
            self.URLLength(url),
            self.suffixInDomain(self.getDomain(url)),
            self.domainLength(self.getDomain(url))
        ]

        return self.features

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





