#!/usr/bin/env python
#https://github.com/xeinherjar
#Version: 0.01

import sys

#build dictionary to hold key:value
#single characters -- vowels and n
hgv = {'a':'あ', 'i':'い', 'u':'う', 'e':'え', 'o':'お', 'n':'ん' }

#Two characters
hg  = {'ka':'か', 'ki':'き', 'ku':'く', 'ke':'け', 'ko':'こ',
       'sa':'さ',            'su':'す', 'se':'せ', 'so':'そ',
       'ta':'た',                       'te':'て', 'to':'と',
       'na':'な', 'ni':'に', 'nu':'ぬ', 'ne':'ね', 'no':'の',
       'ha':'は', 'hi':'ひ', 'fu':'ふ', 'he':'へ', 'ho':'ほ',
       'ma':'ま', 'mi':'み', 'mu':'む', 'me':'め', 'mo':'も',
       'ya':'や',            'yu':'ゆ',            'yo':'よ',
       'ra':'ら', 'ri':'り', 'ru':'る', 're':'れ', 'ro':'ろ',
       'wa':'わ', 'wi':'ゐ',            'we':'ゑ', 'wo':'を',
     
       'ga':'が', 'gi':'ぎ', 'gu':'ぐ', 'ge':'げ', 'go':'ご',
       'za':'ざ', 'ji':'じ', 'zu':'ず', 'ze':'ぜ', 'zo':'ぞ',
       'da':'だ', 'di':'ぢ', 'zu':'づ', 'de':'で', 'do':'ど',
       'ba':'ば', 'bi':'び', 'bu':'ぶ', 'be':'べ', 'bo':'ぼ',
       'pa':'ぱ', 'pi':'ぴ', 'pu':'ぷ', 'pe':'ぺ', 'po':'ぽ',

       'ja':'じゃ', 'ju':'じゅ', 'jo':'じょ'

      }

#Three characters
hgg = {'shi':'し', 'chi':'ち', 'tsu':'つ',

       'kya':'きゃ', 'kyu':'きゅ', 'kyo':'きょ',
       'sha':'しゃ', 'shu':'しゅ', 'sho':'しょ',
       'cha':'ちゃ', 'chu':'ちゅ', 'cho':'ちょ',
       'nya':'にゃ', 'nyu':'にゅ', 'nyo':'にょ',
       'hya':'ひゃ', 'hyu':'ひゅ', 'hyo':'ひょ',
       'mya':'みゃ', 'myu':'みゅ', 'myo':'みょ',
       'rya':'りゃ', 'ryu':'りゅ', 'ryo':'りょ',

       'gya':'ぎゃ', 'gyu':'ぎゅ', 'gyo':'ぎょ',
       'bya':'びゃ', 'byu':'びゅ', 'byo':'びょ',
       'pya':'ぴゃ', 'pyu':'ぴゅ', 'pyo':'ぴょ',

       'xya':'ゃ', 'xyu':'ゅ', 'xyo':'ょ', 'xtu':'っ'

 }



#list to hold translated values
kana = []


#Determine if ther is anything to do.
if len(sys.argv) < 2:
    sys.exit("Nothing entered to convert.\n")

def validate():
#First arg is program name... lets skip it.
    for arg in sys.argv:
        if arg == sys.argv[0]:
            continue
        else:
            convert(arg)


def convert(phrase):
    wList = list(phrase)
    i = 0
    kana.append(' ')
    while i < len(wList):
        if wList[i] + wList[i+1] in hg:
            buildOutput(hg[wList[i] + wList[i+1]])
            i = i + 2
        elif wList[i] in hgv:
            buildOutput(hgv[wList[i]])
            i = i + 1
        elif wList[i] + wList[i+1] + wList[i+2] in hgg:
            buildOutput(hgg[wList[i] + wList[i+1] + wList[i+2]])
            i = i + 3
        else:
            buildOutput(wList[i])
            i = i + 1


def buildOutput(letter):
    kana.append(letter)
   

validate()
output = ''.join(kana)
print(output)
