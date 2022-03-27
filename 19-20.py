from deepgram import Deepgram
import asyncio, json
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from textblob import TextBlob

DEEPGRAM_API_KEY = '32a59470034fea3fe30231e6d3a43fc65c44df91'
reviews = ["y3/Google Pixel 3 XL Review_ The Shadow of the Notch! (128 kbps).mp3","y3/Google Pixel 3a Review_ A for Ace! (128 kbps).mp3","y3/Apple iPhone Xs Review_ A (S)mall Step Up! (128 kbps).mp3","y3/iPhone XR Review_ No Need to Panic! (128 kbps).mp3","y3/Samsung Galaxy S9 Review_ The Perfect... Samsung! (128 kbps).mp3","y3/Samsung Galaxy S10e Review_ Why Not_ (128 kbps).mp3","y3/Samsung Galaxy Note 9 Review_ The Total Package! (128 kbps).mp3","y3/Samsung Galaxy S10+ Review_ The Bar is Set! (128 kbps).mp3"]
async def main():
    sents = []
    ts = []
    r2 = ["Pixel 3 XL","Pixel 3a","iPhone Xs","iPhone XR","Galaxy S9","Galaxy S10e","Galaxy Note 9","Galaxy S10+"]
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
    print(sents)
    ts.append((sents[0]+sents[1])/2)
    ts.append((sents[2]+sents[3])/2)
    ts.append((sents[4]+sents[5]+sents[6]+sents[7])/4)
    print("\nAverage smartphone sentiment for each brand:")
    print("Google: "+str(ts[0]))
    print("Apple: "+str(ts[1]))
    print("Samsung: "+str(ts[2]))
    if ts.index(max(ts)) == 0:
        print("Favorite brand of the year: Google") 
    elif ts.index(max(ts)) == 1:
        print("Favorite brand of the year: Apple") 
    else:
        print("Favorite brand of the year: Samsung\n")
    plt.rc('xtick', labelsize=7)
    plt.bar(y_pos, performance, align='center', alpha=1)
    plt.xticks(y_pos, r2, rotation=60)
    plt.ylabel('Sentiment')
    plt.title('Smartphone Reviews (2019-2020)')

    plt.show()

asyncio.run(main())

