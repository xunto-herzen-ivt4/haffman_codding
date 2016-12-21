from haffman_codding import encode, decode
import pprint

messages = [
    (15 * "А") + (7 * "Б") + (6 * "В") + (6 * "Г") + (5 * "Д"),
    "tiis",
    "Код_Шеннона-Фано",
    '''
    А судьи кто? — За древностию лет
    К свободной жизни их вражда непримирима,
    Сужденья черпают из забытых газет
    Времен Очаковских и покоренья Крыма;
    Всегда готовые к журьбе,
    Поют всё песнь одну и ту же,
    Не замечая об себе:
    Что старее, то хуже.
    Где? укажите нам, отечества отцы,
    Которых мы должны принять за образцы?
    Не эти ли, грабительством богаты?
    Защиту от суда в друзьях нашли, в родстве,
    Великолепные соорудя палаты,
    Где разливаются в пирах и мотовстве,
    И где не воскресят клиенты-иностранцы
    Прошедшего житья подлейшие черты.
    ''',
    '''
    Holden Caulfield writes his story from a rest home to which
    he has been sent for therapy. He refuses to talk about his early
    life, mentioning only that his brother D. B. is a Hollywood writer.
    He hints that he is bitter because D. B. has sold out to Hollywood,
    forsaking a career in serious literature for the wealth and fame of
    the movies. He then begins to tell the story of his breakdown,
    beginning with his departure from Pencey Prep, a famous school
    he attended in Agerstown, Pennsylvania.
    '''
]

pp = pprint.PrettyPrinter(indent=4)
for message in messages:
    codes, encoded = encode(message)
    print('\n\n=====')
    print('Message:\n', message)
    print('Codes:')
    pp.pprint(codes)
    print('Encode:\n', encoded)
    print('Decode:\n', decode(codes, encoded))