# coding: utf-8
# Импортирует поддержку UTF-8.
from __future__ import unicode_literals

# Импортируем модули для работы с JSON и логами.
import json
import logging
import pymorphy2
# Импортируем подмодули Flask для запуска веб-сервиса.
from flask import Flask, request
app = Flask(__name__)

morph = pymorphy2.MorphAnalyzer()


logging.basicConfig(level=logging.DEBUG)

# Хранилище данных о сессиях.
sessionStorage = {}

# Задаем параметры приложения Flask.
@app.route("/", methods=['POST'])
def main():
# Функция получает тело запроса и возвращает ответ.
    logging.info('Request: %r', request.json)

    response = {
        "version": request.json['version'],
        "session": request.json['session'],
        "response": {
            "end_session": False
        }
    }

    handle_dialog(request.json, response)

    logging.info('Response: %r', response)

    return json.dumps(
        response,
        ensure_ascii=False,
        indent=2
    )

def norm(word):
    #полноценная морфолгия
    lword = word.lower()
    #if lword in wordform_cache:
    #    return wordform_cache[lword]
    nform =  morph.parse(lword)[0].normal_form
    #wordform_cache[lword] = nform
    return nform
def do_dialog(w):
    tokens = tokenize(w)
    for t in tokens:
        if t in list(data.keys()):
            return data[t]
    return "Это девушки различают миллионы цветов а я знаю только семь"
    
data =   { "красный": "К красному цвету подойдет зеленый или синий цвета",
     "оранжевый": "К оранжевому подойдет синий или зеленый цвета",
     "жёлтый": "К жёлтому цвету подойдет синии или карсный цвета ",
     "зеленый": "К зелёному подойдет красный или синий цвета ",
     "голубой": "К голубому подойдет оранджевый или филетовый цвета",
     "синий": "К синему подойдет зеленый или карасный цвета ", 
     "фиолетовый": "К фиолетовому подойдет зеленый или оранжевый цвета ",
     "чёрный": "Этот цвет нейтральный к немуподойдут все цвета ",
     "белый": "Этот цвет нейтральный к немуподойдут все цвета",
     }

SEPARATORS={u'': u'', u'\u20ac': u'', u'\u2014': u'', u'\u2018': u'', u'\u201c': u'', u'\u2020': u'', u'\xa3': u'', u'\u2122': u'', u'$': u'', u'\xa7': u'', u'\u02b0': u'', u'(': u'', u'\xab': u'', u',': u'', u'\xaf': u'', u'\u2030': u'', u'\xb3': u'', u'\u02b2': u'', u'\xb7': u'', u'\xbb': u'', u'<': u'', u'\xbf': u'', u'\u02b4': u'', u'@': u'', u'\u02c3': u'', u'\u02c7': u'', u'\u02cb': u'', u'\u02b6': u'', u'\u02cf': u'', u'\u02d3': u'', u'\u0152': u'', u'\u02d7': u'', u'\u02b8': u'', u'\u02db': u'', u'\\': u'', u'\u02df': u'', u'`': u'', u'\u02e3': u'', u'\u02ba': u'', u'\u02e7': u'', u'\u02eb': u'', u'\u02ef': u'', u'\u02bc': u'', u'\u02f3': u'', u'\u02f7': u'', u'\u02fb': u'', u'\u02be': u'', u'\ufffd': u'', u'|': u'', u'\u02ff': u'', u'\u017e': u'', u'\u2013': u'', u'\u0192': u'', u'#': u'', u'\xa4': u'', u"'": u'', u'\xa8': u'', u'+': u'', u'\xac': u'', u'/': u'', u'\xb0': u'', u'\xb4': u'', u'\xb8': u'', u';': u'', u'\xbc': u'', u'?': u'', u'\u02c0': u'', u'\u02c4': u'', u'\u02c8': u'', u'\u02cc': u'', u'\u02d0': u'', u'\u2022': u'', u'\u02d4': u'', u'\u02d8': u'', u'[': u'', u'\u02dc': u'', u'_': u'', u'\u0161': u'', u'\u02e0': u'', u'\u02e4': u'', u'\u02e8': u'', u'\u2026': u'', u'\u02ec': u'', u'\u02f0': u'', u'\u02f4': u'', u'\u02f8': u'', u'{': u'', u'\u017d': u'', u'\u02fc': u'', u'\u201a': u'', u'\u201e': u'', u'\xa1': u'', u'\u02b1': u'', u'"': u'', u'\xa5': u'', u'&': u'', u'\xa9': u'', u'*': u'', u'\xad': u'', u'\u02b3': u'', u'.': u'', u'\xb1': u'', u'\xb5': u'', u'\xb9': u'', u'\u02b5': u'', u':': u'', u'\xbd': u'', u'>': u'', u'\u02c1': u'', u'\u02c5': u'', u'\u02b7': u'', u'\u02c9': u'', u'\u02cd': u'', u'\u02d1': u'', u'\u02b9': u'', u'\u02d5': u'', u'\u02d9': u'', u'\u02dd': u'', u'\u02bb': u'', u'^': u'', u'\u02e1': u'', u'\u0160': u'', u'\u203a': u'', u'\u02e5': u'', u'\u02e9': u'', u'\u02bd': u'', u'\u02ed': u'', u'\u02f1': u'', u'\u02f5': u'', u'\u02bf': u'', u'\u02f9': u'', u'\u0178': u'', u'\u02fd': u'', u'~': u'', u'\u2019': u'', u'\u201d': u'', u'!': u'', u'\xa2': u'', u'%': u'', u'\xa6': u'', u')': u'', u'\xaa': u'', u'-': u'', u'\xae': u'', u'\xb2': u'', u'\xb6': u'', u'\u2039': u'', u'\xba': u'', u'=': u'', u'\xbe': u'', u'\u2021': u'', u'\u02c2': u'', u'\u02c6': u'', u'\u02ca': u'', u'\u02ce': u'', u'\u0153': u'', u'\u02d2': u'', u'\u02d6': u'', u'\u02da': u'', u']': u'', u'\u02de': u'', u'\u02e2': u'', u'\u02e6': u'', u'\u02ea': u'', u'\u02ee': u'', u'\u02f2': u'', u'\u02f6': u'', u'\u02fa': u'', u'}': u'', u'\u02fe': u''}
 
def tokenize(inputText):
   allCharValues=[]
   for oneChar in inputText:
      if oneChar not in SEPARATORS:
         allCharValues.append(oneChar)
         allStringValues=u"".join(allCharValues)
         vectorOfTokens=allStringValues.split()
         vectorResult=[]
         listOfTokens=[]
         for oneToken in vectorOfTokens:
           cleanedToken=norm(oneToken.strip().lower())
           listOfTokens.append(cleanedToken)
   return listOfTokens
# Функция для непосредственной обработки диалога.
def handle_dialog(req, res):
    user_id = req['session']['user_id']

    if req['session']['new']:
        res['response']['text']  = "Привет! я могу помочь тебе подобрать цвет"
        return
        # Это новый пользователь.
        # Инициализируем сессию и поприветствуем его.

        #sessionStorage[user_id] = {
        #    'suggests': [
        #        "Не хочу.",
        #        "Не буду.",
        #        "Отстань!",
        #    ]
        #}
    if (not req['request']['original_utterance']):
        res['response']['text'] = "Пустой запрос пустой текст"
        return
    res['response']['text'] = do_dialog(req['request']['original_utterance'])
        #res['response']['buttons'] = get_suggests(user_id)
    return

    # Обрабатываем ответ пользователя.
    #if req['request']['original_utterance'].lower() in [
   #     'ладно',
   #     'куплю',
   #     'покупаю',
   #     'хорошо',
   # ]:
        # Пользователь согласился, прощаемся.
   #     res['response']['text'] = 'Слона можно найти на Яндекс.Маркете!'
   #     return

    # Если нет, то убеждаем его купить слона!
  #  res['response']['text'] = 'Все говорят "%s", а ты купи слона!' % (
  #      req['request']['original_utterance']
 #   )
 #   res['response']['buttons'] = get_suggests(user_id)

# Функция возвращает две подсказки для ответа.
#def get_suggests(user_id):
#    session = sessionStorage[user_id]
#
    # Выбираем две первые подсказки из массива.
#    suggests = [
#        {'title': suggest, 'hide': True}
#        for suggest in session['suggests'][:2]
#    ]

    # Убираем первую подсказку, чтобы подсказки менялись каждый раз.
#    session['suggests'] = session['suggests'][1:]
#    sessionStorage[user_id] = session

    # Если осталась только одна подсказка, предлагаем подсказку
    # со ссылкой на Яндекс.Маркет.
#    if len(suggests) < 2:
#        suggests.append({
#            "title": "Ладно",
#            "url": "https://market.yandex.ru/search?text=слон",
#            "hide": True
#        })
#
  #  return suggests
