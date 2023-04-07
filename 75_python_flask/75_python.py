import re
import flask
import requests
from flask import redirect, url_for, request

app = flask.Flask(__name__)

MENU_TITLE = ['main', 'news', 'management', 'facts', 'contacts', 'history']

CONTENT_NEWS = ['Мешканка Хмельницька "потрапила на гачок" '
                'через власні інтимні фото. У прокуратурі повідомляють, '
                'що 27-річний хмельничанин вимагав чималу суму коштів у своєї однолітки. '
                'Він погрожував 27-річній дівчині, що поширить відверті фотографії, '
                'на яких вона зображена. Спочатку мова йшла про 2 тисячі доларів США, '
                'але згодом зловмисник підвищив ціну до 4,5 тисяч']

CONTENT_MANAGEMENT = {
    'Мер': 'Симчишин Олександр Сергійович',
    'Прапор': 'https://zname.com.ua/watermark/watermark.php?image=https://zname.com.ua/image/cache/catalog/content/Flagi-UK/Flagi_UG/FUG407-Khmelnytskyi-01-800x533.jpg'

}
CONTENT_CONTACTS = [
    ['Пожежна служба', '101'],
    ['Поліція', '102'],
    ['Медицина', '103'],
    ['Газова служба', '104']

]
CONTENT_FACTS = [
    ['Факт 1. '
     'Перша писемна згадка - 10 чи 12 лютого? В науковій літературі зазначено, що найдавніша писемна згадка '
     'про місто - 10 лютого 1431 року. Вона стосується поселення Ploskirоwcze – Плоскирівці, яке нині має назву '
     'Хмельницький. Віднайшов згадку кам’янчанин, історик Віталій Михайловський. Він натрапив на документ у '
     '2000-у році, працюючи в архівах Польщі. Про те, за яких обставин було знайдено найдавнішу згадку про Хмельницький,'
     ' про що йшлося в документі та як місто стало старшим одразу на 62 роки Віталій Михайловський свого '
     'часу розповідав сайту «Є».«Загалом, правильна дата, вказана у віднайденому документі, – 12 лютого, '
     'а не 10-те, - зазначає доктор історичних наук Віталій Михайловський. - Помилка сталася через особливість '
     'читання латиномовних дат: зазвичай, тоді їх писали як день тижня до чи після якогось з католицьких свят. '
     'Саме під час трактування написаного і сталася ця помилка. Пізніше я її виправив, але на момент публікації '
     'статті як було зазначено 10 лютого, так і ця дата увійшла в науковий обіг».'],

    ['Факт 2. '
     'У 2006-у місто «постаріло» одразу на понад 60 років На початку 90-х, а саме у 1993 році, Хмельницький, '
     'як і чимало населених пунктів, відсвяткували 500-ліття від першої писемної згадки. За джерело цієї дати були '
     'взяті публікації Михайла Грушевського з історії пізньосередньовічного Подільського воєводства. Зокрема, '
     'реєстр димів, який було складено у 1493 році. Саме тут згадувалося чимало населених пунктів, серед яких і '
     'Плоскирівці. Тож інформацією про віднайдену нову згадку Віталій Михайловський поділився з викладачами '
     'історичного факультету в Кам’янці-Подільському. А згодом, у 2004-у, наукова публікація «Джерельні згадки '
     'про Проскурів у XV столітті» з’явилася в Українському археографічному щорічнику. З того часу дату ввели в '
     'науковий обіг. У 2006 році дату першої писемної згадки про Хмельницький було офіційно перенесено на '
     '1431 рік. Відтак, місто замість свого 513-річчя відсвяткувало 575 річницю від першої писемної згадки. '
     'Так Хмельницький на понад 60 років став древнішим.'],

    ['Факт 3. '
     'Острів кохання у Хмельницькому – створений штучно Острів на Південному Бузі, що в Хмельницькому, '
     'місцеві мешканці називають доволі романтично - Островом кохання. Але звідки пішла ця назва? Як взагалі '
     'виник острів посеред річки? Чи природний він, чи створений людьми? Краєзнавець та кандидат історичних наук, '
     'провідний науковий співробітник Хмельницького обласного краєзнавчого музею Сергій Єсюнін розповідає, що вже '
     'в ХХ столітті було вирішено облагородити місцевість в заплаві річки Плоскої і зробити там відпочинкову зону.'
     '«Ця ідея виникла в 30-х роках ХХ століття, ще до початку Другої світової війни, - розповідає Сергій Єсюнін. - '
     'Її підтримали архітектори, і в 1937 році був розроблений генеральний план розбудови Проскурова. Зокрема, '
     'в заплаві річки Плоска планували створити парк та водосховище з пляжем. Утім, на заваді планам стала Друга '
     'світова війна. За цей час Проскурів встиг стати обласним центром (1941 рік). Реалізовувати задум взялися вже '
     'після війни, в 1947 році». Щоб осушити болотяну місцевість в заплаві Плоскої прокопали канали, які до речі, '
     'гуляючи парком, ми бачимо і зараз. А ще насадили дерева та заклали парк. Одночасно було вирішено збудувати і '
     'нове водосховище та оновити греблю. Масштабне будівництво розпочалося в 1949 році.'],

]
CONTENT_HISTORY = 'У Хмельницькому понад 1000 різних вулиць та провулків, площ та майданів, але 200 років тому ' \
                  'все було інакше. В місті їх було всього 9. Завдяки вигідному розташуванню на перетині двох ' \
                  'торговельних та поштових шляхів, які вели на Летичів та Камянець-Подільський, місто отримало ' \
                  'чималу користь від торгівлі та промисловості, яка була реалізована лише у XIX столітті. ' \
                  'Впродовж століть Плоскирів, а згодом Проскурів, як його тоді називали, можна було вважати ' \
                  'пересічним містечком, яких було сотні по всій Україні, та чому саме він став центром області? ' \
                  'Своєму розвитку місто завдячує, звичайно, містянам. Проскурів віддавна був багатонаціональним ' \
                  'містом. На початку XX століття майже половину його населення складали євреї, було тут також ' \
                  'чимало українців, поляків та росіян. Православне населення становило третину міської громади.'
CONTENT_PEOPLE = [
    {
        'name': 'дядя Жора',
        'description': 'Украинский шоумен, ведущий, певец и актер. Продюсер женской группы "Opium". '
                       'Участник развлекательных шоу, КВН и Камеди клаб. Настоящее имя шоумена Вадим Мычковский.'
    },
    {
        'name': 'Олександр Пономарьов',
        'description': 'Олександр Пономарьов — український співак, композитор, народний артист України (2006). '
                       'Представник України на 48-му пісенному конкурсі «Євробачення.'
                       '4 травня 2003 року в Латвії відбувся 48-й пісенний конкурс «Євробачення» '
                       'на якому дебютувала Україна з піснею «Hasta la vista» у виконанні Пономарьова. '
                       'Він посів 14-е місце.'
    },
    {
        'name': 'Олександр Педан',
        'description': 'Народився 24 березня 1982 року у м. Хмельницькому. '
                       'У 1999 році здобув вищу освіту менеджера-економіста у Хмельницькому Національному університеті. '
                       'За фахом, дякувати Богу, не працюю. 11 років свого життя присвятив українським народним танцям. '
                       'Нікуди було діватися. Батько – хореограф ансамблю українського народного танцю.'
    }
]
CONTENT_PHOTO = [
    'https://vsim.ua/img/cache/news_new_m/news/0008/29/c947e4753fb95899728c65b133ac9f26398762db.jpeg?hash=2017-11-15-22-34-42'
    '=MnwxMjA3fDB8MHxzZWFyY2h8MXx8b2Rlc3NhfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60',
    'https://vsim.ua/img/cache/news_new_m/news/0007/75/674202-stari-svitlini-hmelnitskogo.jpeg?hash=2018-03-15-13-48-59'
    '=MnwxMjA3fDB8MHxzZWFyY2h8NXx8b2Rlc3NhfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60',
    'https://vsim.ua/img/cache/news_new_m/news/0012/26/1125114-vgadayte-mistse-u-hmelnitskomu-za-starim-foto-test.jpeg?hash=2019-02-14-13-48-09'
    '=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8b2Rlc3NhfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60',


]
RegEx = {
    'main': '^http:\/\/127\.0\.0\.1:5000\/main.*$',
    'news': '^http:\/\/127\.0\.0\.1:5000\/news.*$',
    'management': '^http:\/\/127\.0\.0\.1:5000\/management.*$',
    'facts': '^http:\/\/127\.0\.0\.1:5000\/facts.*$',
    'contacts': '^http:\/\/127\.0\.0\.1:5000\/contacts.*$',
    'history': '^http:\/\/127\.0\.0\.1:5000\/history.*$',
    'history_people': '^http:\/\/127\.0\.0\.1:5000\/history\/people.*$',
    'history_photo': '^http:\/\/127\.0\.0\.1:5000\/history\/photo.*$',

}


@app.route('/')
@app.route('/main')
def main():
    context = {
        'menu': MENU_TITLE,
        'context': [
            {
                'title': 'facts',
                'content': CONTENT_FACTS
            },
            {
                'title': 'news',
                'content': CONTENT_NEWS
            },
            {
                'title': 'management',
                'content': CONTENT_MANAGEMENT
            },
            {
                'title': 'history',
                'content': CONTENT_HISTORY
            },
            {
                'title': 'contacts',
                'content': CONTENT_CONTACTS
            }
        ]
    }
    return flask.render_template('main.html', context=context)


@app.route('/news')
def news():
    context = {
        'title': 'Новини',
        'menu': MENU_TITLE,
        'content': CONTENT_NEWS
    }
    return flask.render_template('news.html', context=context)


@app.route('/management')
def management():
    context = {
        'title': 'Управління',
        'menu': MENU_TITLE,
        'content': CONTENT_MANAGEMENT
    }
    return flask.render_template('management.html', context=context)


@app.route('/facts')
def facts():
    context = {
        'title': 'Факти нашого краю',
        'menu': MENU_TITLE,
        'content': CONTENT_FACTS
    }
    return flask.render_template('fact.html', context=context)


@app.route('/contacts')
def contacts():
    context = {
        'title': 'Контактні телефони',
        'menu': MENU_TITLE,
        'content': CONTENT_CONTACTS
    }
    return flask.render_template('contacts.html', context=context)


@app.route('/history')
def history():
    context = {
        'title': 'Історія',
        'menu': MENU_TITLE,
        'content': CONTENT_HISTORY
    }
    return flask.render_template('history.html', context=context)


@app.route('/history/people')
def people():
    context = {
        'title': 'Люди з нашого краю',
        'menu': MENU_TITLE,
        'content': CONTENT_PEOPLE
    }
    return flask.render_template('people.html', context=context)


@app.route('/history/photo')
def photos():
    context = {
        'title': 'Фото нашого краю',
        'menu': MENU_TITLE,
        'content': CONTENT_PHOTO
    }
    return flask.render_template('photos.html', context=context)


@app.errorhandler(404)
def page_not_found(e):
    url = str(request.url)

    if re.search(RegEx['news'], url) is not None:
        return flask.redirect(url_for('news'))
    elif re.search(RegEx['management'], url) is not None:
        return flask.redirect(url_for('management'))
    elif re.search(RegEx['contacts'], url) is not None:
        return flask.redirect(url_for('contacts'))
    elif re.search(RegEx['history'], url) is not None:
        return flask.redirect(url_for('history'))
    elif re.search(RegEx['facts'], url) is not None:
        return flask.redirect(url_for('facts'))
    elif re.search(RegEx['people'], url) is not None:
        return flask.redirect(url_for('people'))
    elif re.search(RegEx['photo'], url) is not None:
        return flask.redirect(url_for('photo'))
    else:
        return flask.redirect('main.html')


if __name__ == "__main__":
    app.run(debug=True)
