import pandas as pd


def SavePhishingURLs():

    phishing_URLs = df[df['label'] == 0]
    phishing_URLs= phishing_URLs.sample(50000, random_state=42)

    split_ratio = 0.8
    split_index = int(split_ratio * len(phishing_URLs))

    phishing_train_data = phishing_URLs[:split_index]
    phishing_test_data = phishing_URLs[split_index:]

    phishing_train_data.to_csv("phishing_train_data.txt", index=False, header=False)
    phishing_test_data.to_csv("phishing_test_data.txt", index=False, header=False)

def SaveBenignURLs():

    benign_URLs = df[df['label'] == 1]
    benign_URLs= benign_URLs.sample(50000, random_state=42)

    split_ratio = 0.8
    split_index = int(split_ratio * len(benign_URLs))

    benign_train_data = benign_URLs[:split_index]
    benign_test_data = benign_URLs[split_index:]

    benign_train_data.to_csv("benign_train_data.txt", index=False, header=False)
    benign_test_data.to_csv("benign_test_data.txt", index=False, header=False)

df = pd.read_csv("PhiUSIIL_Phishing_URL_Dataset.csv")
#SavePhishingURLs()
SaveBenignURLs()