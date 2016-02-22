from instagram.client import InstagramAPI
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from scipy.misc import imread
from stop_words import get_stop_words
import keys

api = InstagramAPI(access_token=keys.access_token,
                   client_secret=keys.client_secret)
recent_media, next_ = api.user_recent_media(user_id="10206720", count=70)

captions = [media.caption.text for media in recent_media]

stop_words = {word for word in get_stop_words('french')}


def wordcloud(data, mask='extras/instagram_mask.png', stopwords=stop_words, save=True):
    ''' Compute wordcloud '''
    twitter_mask = imread(mask, flatten=True)

    more_stopwords = STOPWORDS  # English stopwords
    stopwords = stopwords.union(more_stopwords)

    wordcloud = WordCloud(
        font_path='extras/quartzo.ttf',
        stopwords=stopwords,
        background_color='white',
        width=1800,
        height=1400,
        mask=twitter_mask
    ).generate(data)

    plt.imshow(wordcloud)
    plt.axis('off')

    if save:
        plt.savefig('wordclouds/wordcloud.png', dpi=300)
    plt.show()


texts = ' '.join(captions)
wordcloud(data=texts, stopwords=stop_words)
