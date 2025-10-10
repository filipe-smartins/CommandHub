from utils.utils import capitalized_name, format_number, lower_name, upper_name


def test_capitalized_name():
    assert capitalized_name('joao') == 'Joao'
    assert capitalized_name('joão') == 'João'
    assert capitalized_name('João') == 'João'
    assert capitalized_name('JOão') == 'João'
    assert capitalized_name('JoãO') == 'João'
    assert capitalized_name('JOÃO') == 'João'


def test_upper_name():
    assert upper_name('joao') == 'JOAO'
    assert upper_name('joão') == 'JOÃO'
    assert upper_name('João') == 'JOÃO'
    assert upper_name('JOão') == 'JOÃO'
    assert upper_name('JoãO') == 'JOÃO'
    assert upper_name('JOÃO') == 'JOÃO'


def test_lower_name():
    assert lower_name('joao') == 'joao'
    assert lower_name('joão') == 'joão'
    assert lower_name('João') == 'joão'
    assert lower_name('JOão') == 'joão'
    assert lower_name('JoãO') == 'joão'
    assert lower_name('JOÃO') == 'joão'


def test_format_number():
    assert format_number('R$2.500') == 2500.0
    assert format_number('R$ 2.500') == 2500.0
    assert format_number('2.500') == 2500.0
    assert format_number('R$2.500  ') == 2500.0
    assert format_number('USD2.500') == 2500.0
    assert format_number('EUR 2.500') == 2500.0
    assert format_number('2500') == 2500.0
