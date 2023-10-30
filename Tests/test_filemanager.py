
import my_bank_account
import victory


def test_finish_text():
    assert victory.finish_text('12.23.56.23.2.124') == ['12', '23', '56', '23', '2', '124']


def test_separator():
    assert my_bank_account.separator() == '---------------------------'
