from src import utils


def test_get_last_five_operations():
    assert utils.get_last_five_operations([{'date': 2},
                                           {'date': 5},
                                           {'date': 4},
                                           {'date': 1},
                                           {'date': 3}
                                           ]) == [{'date': 1},
                                                  {'date': 2},
                                                  {'date': 3},
                                                  {'date': 4},
                                                  {'date': 5}]
    assert utils.get_last_five_operations([{'date': 2},
                                           {'date': 5},
                                           {'date': 4},
                                           {'date': 6},
                                           {'date': 1},
                                           {'date': 3}
                                           ]) == [{'date': 2},
                                                  {'date': 3},
                                                  {'date': 4},
                                                  {'date': 5},
                                                  {'date': 6}]
    assert utils.get_last_five_operations([{'date': 2},
                                           {'dat': 5},
                                           {'date': 4},
                                           {'date': 6},
                                           {'date': 1},
                                           {'date': 3}
                                           ]) == "Отсутствует дата в операции номер - 1"


def test_formation_date():
    assert utils.formation_date([{'date': "2019-02-14 03:09:23"}]) == [{'date': '14.02.2019'}]
    assert utils.formation_date([{'date': "2019-02-1"}]) == 'Ошибка даты: слинком короткая строка'


def test_add_from_in_operations():
    assert utils.add_from_in_operations(
        [{'from': 7, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6},
         {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6},
         {'from': 7, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
         ]) == [{'from': 7, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6},
               {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'from': 'Отсутствует'},
               {'from': 7, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}]
    assert utils.add_from_in_operations(
        [{'from': 7, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6},
         {'from': 7,'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6},
         {'from': 7, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
         ]) == [{'from': 7, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6},
                {'from': 7, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6},
                {'from': 7, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}]


def test_disguise_sender_account():
    assert utils.disguise_sender_account([{"from": 'Visa Gold 7756673469642839'}]) == [{"from": 'Visa Gold 775667******2839'}]
    assert utils.disguise_sender_account([{"from": 'Отсутствует'}]) == [{"from": 'Отсутствует'}]


def test_disguise_recipients_account():
    assert utils.disguise_recipients_account([{'to': 'Счет 61834060137088759145'}]) == [{'to': 'Счет **9145'}]
    assert utils.disguise_recipients_account([{'to': 'Maestro 3806652527413662'}]) == [{'to': 'Maestro **3662'}]
    assert utils.disguise_recipients_account([{'to': 'Visa Platinum 6086997013848217'}]) == [{'to': 'Visa Platinum **8217'}]