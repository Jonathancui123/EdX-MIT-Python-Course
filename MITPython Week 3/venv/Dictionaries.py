#Given a string/song lyric, build a dictionary of word:frequency

OGlyrics = """She loves you, yeah, yeah, yeah
She loves you, yeah, yeah, yeah
She loves you, yeah, yeah, yeah
You think you've lost your love
Well, I saw her yesterday-yi-yay
It's you she's thinking of
And she told me what to say-yi-yay
She says she loves you
And you know that can't be bad
Yes, she loves you
And you know you should be glad
She said you hurt her so
She almost lost her mind
And now she says she knows
You're not the hurting kind
She says she loves you
And you know that can't be bad
Yes, she loves you
And you know you should be glad
Oo, she loves you, yeah, yeah, yeah
She loves you, yeah, yeah, yeah
With a love like that
You know you should be glad
You know it's up to you
I think it's only fair
Pride can hurt you too
Apologize to her
Because she loves you
And you know that can't be bad
Yes, she loves you
And you know you should be glad
Oo, she loves you, yeah, yeah, yeah
She loves you, yeah, yeah, yeah
With a love like that
You know you should be glad
With a love like that
You know you should be glad
With a love like that
You know you should be glad
Yeah, yeah, yeah,
Yeah, yeah, yeah, yeah"""


def lyrics_to_frequencies(OGlyrics):
    OGlyrics = OGlyrics.lower()
    lyrics = ''
    for char in OGlyrics:
        if char  in ' abcdefghijklmnopqrstuvwxyz':
            lyrics += char

    ListLyrics = lyrics.split()
    BigDic = {}
    for word in ListLyrics:
        if word in BigDic.keys():
            BigDic[word] += 1
        else:
            BigDic[word] = 1

    return BigDic

def most_common(freqs):
    values = freqs.values()
    k = max(values)

    words = []

    for word in freqs:
        if freqs[word] == k:
            words.append(word)

    return (words, k)

def aboveThreshold(freqs, thresh):
    list = []
    done = False
    while not done:
        temp = most_common(freqs)
        if temp[1] >= thresh:
            list.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return list

thresh = int(input("What is threshold:"))
newlist = []
for entry in (aboveThreshold(lyrics_to_frequencies(OGlyrics), thresh)):
    newlist += (entry[0])
print(newlist)