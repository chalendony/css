from selector.phineo.parser import Parser
url = 'https://www.phineo.org/projekte/details/jung-alt-begegnung-von-kindern-und-alten-menschen?tx_phineoprojectslite_pi1%5Bpointer%5D=5&tx_phineoprojectslite_pi1%5Bpps%5D=25'


def themen():
    parser = Parser()
    res = parser.themen(url)
    assert 'Gesundheit & Pflege' == res


def test_zielgruppe():
    parser = Parser()
    res = parser.zielgruppe(url)
    assert "Kinder & Jugendliche" == res[0]


def test_standord():
    parser = Parser()
    res = parser.standort(url)
    assert "Niedersachsen" == res


def test_reichweite():
    parser = Parser()
    res = parser.reichweite(url)
    assert "regional" == res


def test_auf_einen_blick():
    parser = Parser()
    res = parser.auf_einen_blick(url)
    assert "Menschen" == res[0:8]

def test_leistung_image():
    url = 'https://www.phineo.org/projekte/details/dialog-demenz-im-pfaffenwinkel-demenzfreundliche-kommune'
    parser = Parser()
    res = parser.wirk_image(url)
    assert ".jpg" == res[-4 :]

def test_wirk_image():
    url = 'https://www.phineo.org/projekte/details/dialog-demenz-im-pfaffenwinkel-demenzfreundliche-kommune'
    parser = Parser()
    res = parser.wirk_image(url)
    assert ".jpg" == res[-4 :]

def test_flipBoxPages():
    url = 'https://www.phineo.org/projekte'
    parser = Parser()
    res = parser.flipBoxPages()
    assert 5 == len(res)

