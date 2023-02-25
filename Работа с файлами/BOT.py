import telebot
from random import *
import json
from telebot import types
films=[]


def save():
    with open("films.json","w",encoding="utf-8") as fh:
        fh.write(json.dumps(films,ensure_ascii=False))
    print("РќР°С€Р° С„РёР»СЊРјРѕС‚РµРєР° Р±С‹Р»Р° СѓСЃРїРµС€РЅРѕ СЃРѕС…СЂР°РЅРµРЅР° РІ С„Р°Р№Р»Рµ films.json")

def load():
    global films
    with open("films.json","r",encoding="utf-8") as fh:
        films=json.load(fh)
    print("Р¤РёР»СЊРјРѕС‚РµРєР° Р±С‹Р»Р° СѓСЃРїРµС€РЅРѕ Р·Р°РіСЂСѓР¶РµРЅР°")   


API_TOKEN='6025495112:AAEBtLeDcvqlcqPiRD0_0j8fett55e8T71Q'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    try:
        load()
        bot.send_message(message.chat.id,"Фильмотека упешно загружена")

    except:
        films.append("РњР°С‚СЂРёС†Р°")
        films.append("РЎРѕР»СЏСЂРёСЃ")
        films.append("Р’Р»Р°СЃС‚РµР»РёРЅ РєРѕР»РµС†")
        films.append("РўРµС…Р°СЃСЃРєР°СЏ СЂРµР·РЅСЏ Р±РµРЅР·РѕРїРёР»РѕР№")
        films.append("РЎР°РЅС‚Р° Р‘Р°СЂР±Р°СЂР°") 
        bot.send_message(message.chat.id,"привет")


@bot.message_handler(commands=['all'])
def show_all(message):
    bot.send_message(message.chat.id,"Р’РѕС‚ СЃРїРёСЃРѕРє С„РёР»СЊРјРѕРІ")
    bot.send_message(message.chat.id, ", ".join(films))

@bot.message_handler(content_types='text')
def message_reply(message):
    if 'РїСЂРёРІРµС‚' in message.text :
        bot.send_message(message.chat.id,'Рё С‚РµР±Рµ РїСЂРёРІРµС‚')


bot.polling()
import shelve
class PhoneBook:
    def __init__(self, nameBook, dicRec={}):
        self.nameBook = nameBook
        self.dicRec = dicRec
    def loadBook(self):
        db = shelve.open(self.nameBook)
        self.dicRec = dict(db.items())
        db.close()
    def saveBook(self):
        db = shelve.open(self.nameBook)
        for (key, record) in self.dicRec.items():
            db[key] = record
        db.close()
 
    def createRec(self):
        print(self.nameBook)
        label = input('название записи: ')
        phone = input('телефон : ')
        print('ФИО,коммент. - Если нет, просто нажимайте Enter')
        familyName = input('ФИО: ')
        comment = input('Комментарий: ')
        if len(self.dicRec)>0:
            L = sorted(self.dicRec.items(), key=lambda item: item[0])
            keyRec = str(int(L[-1][0]) + 1)
        else:
            keyRec = "1"
        record = PhoneRec(keyRec, label, phone, familyName, comment)
        self.dicRec[keyRec] = record
    def delPhoneRec(self, key):
        del dicRec[key]
    def readPhoneRec(self):
        for key in t1.dicRec.keys():
            print("{:<3}- {:<25}- {:<20}- {:<30}- {:<30}".format(key, t1.dicRec[key].label, 
                                                                            t1.dicRec[key].phone, 
                                                                            t1.dicRec[key].familyName,  
                                                                            t1.dicRec[key].comment))
class PhoneRec:
    def __init__(self, keyRec, label, phone, familyName, comment):
        self.keyRec = keyRec
        self.label = label
        self.phone = phone
        self.familyName = familyName
        self.comment = comment
 
if __name__ == '__main__':
    t1 = PhoneBook("Телефоны")
    t1.loadBook()
    t1.createRec()
    t1.readPhoneRec()
 
    t1.saveBook()

