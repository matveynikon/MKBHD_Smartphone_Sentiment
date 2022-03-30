from deepgram import Deepgram
import asyncio, json
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from textblob import TextBlob

DEEPGRAM_API_KEY = 'your key'
reviews = ["2021/Google Pixel 5 Review_ Software Special! (128 kbps).mp3", "2021/Google Pixel 5A_ Spot the Difference! (128 kbps).mp3", "2021/Google Pixel 4a Review_ Simple and Clean! (128 kbps).mp3", "2021/Pixel 6_6 Pro Review_ Almost Incredible! (128 kbps).mp3", "2021/iPhone 12 Review_ Just Got Real! (128 kbps).mp3", "2021/iPhone 12 Pro Review_ You Sure About That_ (128 kbps).mp3", "2021/iPhone 12 Mini Review_ Tiny Tradeoffs! (128 kbps).mp3", "2021/iPhone 13 Pro Review_ Better Than You Think! (128 kbps).mp3", "2021/iPhone 13 Review_ Lowkey Great! (128 kbps).mp3", "2021/Samsung Z Flip 3 Review_ The First Big Step! (128 kbps).mp3", "2021/Samsung Z Fold 3 Review_ Let's Talk Ambition! (128 kbps).mp3", "2021/Galaxy S21 Review_ Would You Notice_ (128 kbps).mp3", "2021/Samsung Galaxy S21 Ultra Review_ Problems Solved! (128 kbps).mp3"]
r2 = ["Pixel 5", "Pixel 5A", "Pixel 4a", "Pixel 6/6 Pro", "iPhone 12", "iPhone 12 Pro", "iPhone 12 Mini", "iPhone 13 Pro", "iPhone 13", "Z Flip 3", "Z Fold 3", "Galaxy S21", "Galaxy S21 Ultra"]
async def main():
    sents = []
    ts = []
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
    ts.append((sents[0]+sents[1]+sents[2])/3)
    ts.append((sents[3]+sents[4]+sents[5]+sents[6]+sents[7])/5)
    ts.append((sents[8]+sents[9]+sents[10]+sents[11])/4)
    print("\nFavorite smartphone of the year: "+str(r2[sents.index(max(sents))]))
    print("\nLeast favorite smartphone of the year: "+str(r2[sents.index(min(sents))]))
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
    plt.title('Smartphone Reviews (2021)')

    plt.show()

asyncio.run(main())
