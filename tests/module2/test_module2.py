from src.module2.module2 import sum_numbers


def test_soma():
    assert sum_numbers('R$2.500', 'R$2.500') == 5000.0
    assert sum_numbers('R$ 2.500', 'R$ 2.500') == 5000.0
    assert sum_numbers('USD2.500', 'USD 2.500') == 5000.0
    assert sum_numbers('2.500', 'R$2.500') == 5000.0
    assert sum_numbers('2500', '2500') == 5000.0
