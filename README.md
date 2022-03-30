I wanted to explore audio based Sentiment Analysis using DeepGram. I wanted to use DeepGram to transcribe pieces of audio, and then use a Sentiment Analysis library to analyze the transcribed texts in terms of their sentiment.

I did a bit of thinking about what pieces of audio I'm going to perform sentiment analysis on and decided that it would be a good idea to make a Python app that performs sentiment analysis on [Marques Brownlee](https://www.youtube.com/channel/UCBJycsmduvYEL83R_U4JriQ)'s 
smartphone reviews from the past 3 years to find, each year, what smartphones he liked, what smartphones he didn't like as much, as well as his sentiment towards the different smartphone brands.
Marques Reviews a few different brands but I've chosen the ones that have been reviewed the most by Marques so that I have enough data to work with. These brands are: Google, Samsung and Apple. I'll only be referring to these when talking about smartphones and brands in this article.

I know what you might be thinking: "But sentiment analysis isn't very accurate and can make misjudgments on someone's sentiment towards something such as a smartphone!". I know that Sentiment Analysis has it's limitations.
![Meme haha](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ru8zrdzhlwoqia8x6y1l.png)

Nevertheless, I've used the best Sentiment Analysis Library in my experience to try and programmatically make the best assessment of his reviews.

***************

## Building the App 🛠

The app uses 3 scripts to perform sentiment analysis on Marques' smartphone reviews from each year.

Each script does the following:
1. It performs sentiment analysis on the smartphone review videos from the time represented by the script(2019, 2020, 2021) that I downloaded in `.mp3` format using [this web tool](https://www.bestmp3converter.com/).
2. It prints Marques' sentiment towards the brands throughout the year.
3. It displays a bar graph of Marques' sentiment towards each smartphone from that time span.

The reason why I made 3 different scripts analyze smartphone reviews from 3 years separately is because I felt that the bar for a great smartphone raises every year, so it wouldn't be fair to compare an Iphone review from say 2019 to an Iphone review from 2021.

## The Analysis

Here's the analysis that my python scripts have performed!

### Analysis on Reviews from 2019

Here's the chart of Marques Brownlee's sentiment towards the smartphones he reviewed in 2019:
![2019](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qwaianv5nq4aejxadark.png)

Average smartphone sentiment for each brand:

Google: 20.05

Apple: 14.89

Samsung: 18.53


Favorite smartphone: Galaxy Note 9

Least favorite smartphone: Galaxy S10e


### Analysis on Reviews from 2020

Here's the chart of Marques Brownlee's sentiment towards the smartphones he reviewed in 2020:
![2020](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/wmrbzgi8i89ztb38wh4s.png)

Average smartphone sentiment for each brand:

Google: 17.14

Apple: 14.75

Samsung: 16.47


Favorite smartphone: Galaxy Note 10+

Least favorite smartphone: Iphone 11


### Analysis on Reviews from 2021

Here's the chart of Marques Brownlee's sentiment towards the smartphones he reviewed in 2021:
![2021](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/x2i7wfqulxt7uw3lct15.png)

Average smartphone sentiment for each brand:

Google: 17.26

Apple: 17.84

Samsung: 17.36


Favorite smartphone: Pixel 6/6 Pro

Least favorite smartphone: Galaxy S21 Ultra


### Marques' Brand Sentiment Over the Last 3 Years

Here's Marques Brownlee's smartphone brands ranked by average product sentiment:
1. Google(54.45)
2. Samsung(52.36)
3. Apple(47.48)

## Conclusion

Anyway, I hope that you found this DeepGram project pretty cool!
Byeee👋

