from deepgram import Deepgram
import asyncio, json
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from textblob import TextBlob

DEEPGRAM_API_KEY = 'your key'
reviews = ["2020/Google Pixel 3a Review_ A for Ace! (128 kbps).mp3", "2020/Google Pixel 4 Review_ Inside the Hype Machine! (128 kbps).mp3", "2020/Samsung Galaxy S20 Ultra Review_ Attack of the Numbers! (128 kbps).mp3", "2020/Galaxy S20 Impressions_ New Year, New Samsung! (128 kbps).mp3", "2020/iPhone 11 Pro Review_ For the Love of Cameras! (128 kbps).mp3", "2020/iPhone 11 Review_ Too Easy! (128 kbps) (1).mp3", "2020/Samsung Galaxy Note 10+ Review_ The Favorite Child! (128 kbps).mp3"]
async def main():
    sents = []
    ts = []
    r2 = ["Pixel 3a", "Pixel 4", "iPhone 11 Pro", "iPhone 11", "Galaxy S20 Ultra", "Galaxy S20", "Galaxy Note 10+"]
    for i in range(len(reviews)):
        PATH_TO_FILE = reviews[i]
        deepgram = Deepgram(DEEPGRAM_API_KEY)
        with open(PATH_TO_FILE, 'rb') as audio:
            source = {'buffer': audio, 'mimetype': 'audio/mp3'}
            response = await deepgram.transcription.prerecorded(source, {'punctuate': True})
            response = response["results"]
            response = response["channels"]
            response = response[0]["alternatives"]
            response = str(response[0]["transcript"])
            sentiment = TextBlob(response)
            sents.append(float(round(sentiment.sentiment.polarity*100, 2)))
    y_pos = np.arange(len(r2))
    performance = sents
    ts.append((sents[0]+sents[1])/2)
    ts.append((sents[2]+sents[3])/2)
    ts.append((sents[4]+sents[5]+sents[6])/3)
    print("\nAverage smartphone sentiment for each brand:")
    print("Google: "+str(ts[0]))
    print("Apple: "+str(ts[1]))
    print("Samsung: "+str(ts[2]))
    if ts.index(max(ts)) == 0:
        print("Favorite brand of the year: Google\n") 
    elif ts.index(max(ts)) == 1:
        print("Favorite brand of the year: Apple\n") 
    else:
        print("Favorite brand of the year: Samsung\n")
    plt.rc('xtick', labelsize=7)
    plt.bar(y_pos, performance, align='center', alpha=1)
    plt.xticks(y_pos, r2, rotation=60)
    plt.ylabel('Sentiment')
    plt.title('Smartphone Reviews (2020)')

    plt.show()

asyncio.run(main())
