#!/usr/bin/env python
#https://github.com/xeinherjar
#Version: 0.02

import sys

#build dictionaries to hold key:value
#single characters -- vowels, n, punctuation
hgv = {'a':'あ', 'i':'い', 'u':'う', 'e':'え', 'o':'お', 'n':'ん',
       '.':'。', ',':'、', '-':'ー'
      }

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

def convert(phrase):
    kana = '' 
    i = 0
    while i < len(phrase):
        if i < len(phrase) - 2:
            if phrase[i:i+3] in hgg:
                kana = kana + hgg[phrase[i:i+3]]
                i = i + 3
            elif phrase[i:i+2] in hg:
                kana = kana + hg[phrase[i:i+2]]
                i = i + 2
            elif phrase[i] in hgv:
                kana = kana + hgv[phrase[i]]
                i = i + 1
            else:
                kana = kana + phrase[i]
                i = i + 1
        elif i < len(phrase) - 1:
            if phrase[i:i+2] in hg:
                kana = kana + hg[phrase[i:i+2]]
                i = i + 2
            elif phrase[i] in hgv:
                kana = kana + hgv[phrase[i]]
                i = i + 1
            else:
                phrase[i]
                i = i + 1
        elif i < len(phrase):
            if phrase[i] in hgv:
                kana = kana + hgv[phrase[i]]
                i = i + 1
            else:
                kana = kana + phrase[i]
                i = i + 1
    return kana


#Map convert() over aruments, skipping the first argument [filename]
print(''.join(map(convert, sys.argv[1:]))) 

