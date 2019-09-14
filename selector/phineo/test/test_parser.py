from selector.phineo.parser import Catalog


def themen():
    url = 'https://www.phineo.org/projekte/details/jung-alt-begegnung-von-kindern-und-alten-menschen?tx_phineoprojectslite_pi1%5Bpointer%5D=5&tx_phineoprojectslite_pi1%5Bpps%5D=25'
    parser = Catalog()
    res = parser.themen(url)
    assert 'Gesundheit & Pflege' == res


def test_zielgruppe():
    url = 'https://www.phineo.org/projekte/details/jung-alt-begegnung-von-kindern-und-alten-menschen?tx_phineoprojectslite_pi1%5Bpointer%5D=5&tx_phineoprojectslite_pi1%5Bpps%5D=25'
    parser = Catalog()
    res = parser.zielgruppe(url)
    assert "Kinder & Jugendliche" == res[0]


def test_standord():
    url = 'https://www.phineo.org/projekte/details/jung-alt-begegnung-von-kindern-und-alten-menschen?tx_phineoprojectslite_pi1%5Bpointer%5D=5&tx_phineoprojectslite_pi1%5Bpps%5D=25'
    parser = Catalog()
    res = parser.standort(url)
    assert "Niedersachsen" == res


def test_reichweite():
    url = 'https://www.phineo.org/projekte/details/jung-alt-begegnung-von-kindern-und-alten-menschen?tx_phineoprojectslite_pi1%5Bpointer%5D=5&tx_phineoprojectslite_pi1%5Bpps%5D=25'
    parser = Catalog()
    res = parser.reichweite(url)
    assert "regional" == res


def test_auf_einen_blick():
    url = 'https://www.phineo.org/projekte/details/jung-alt-begegnung-von-kindern-und-alten-menschen?tx_phineoprojectslite_pi1%5Bpointer%5D=5&tx_phineoprojectslite_pi1%5Bpps%5D=25'
    parser = Catalog()
    res = parser.auf_einen_blick(url)
    assert "Menschen" == res[0:8]

def test_leistung_image():
    url = 'https://www.phineo.org/projekte/details/dialog-demenz-im-pfaffenwinkel-demenzfreundliche-kommune'
    parser = Catalog()
    res = parser.wirk_image(url)
    assert ".jpg" == res[-4 :]

def test_wirk_image():
    url = 'https://www.phineo.org/projekte/details/dialog-demenz-im-pfaffenwinkel-demenzfreundliche-kommune'
    parser = Catalog()
    res = parser.wirk_image(url)
    assert ".jpg" == res[-4 :]


def test_flipBoxPages():
    url = 'https://www.phineo.org/projekte'
    parser = Catalog()
    res = parser.flipBoxPages()
    assert len(res) == 5

def test_count_details_pages():
    url = 'https://www.phineo.org/projekte?tx_phineoprojectslite_pi1%5Bpointer%5D=2&tx_phineoprojectslite_pi1%5Bpps%5D=10'
    parser = Catalog()
    res = parser.count_projects(url)
    assert len(res) == 11


def test_count_details_pages():
    catalog = Catalog()
    res = catalog.details()
    assert res == 251
