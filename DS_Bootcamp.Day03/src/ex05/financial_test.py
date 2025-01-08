from financial import parse
import pytest

def test_parse_for_ticket_table_name():
    ticket = 'MSFT'
    table_name = 'Total Revenue'
    result = parse(ticket, table_name)
    assert result[0] == table_name
    assert result[1] is not None

def test_parse_is_tuple():
    ticket = 'MSFT'
    table_name = 'Total Revenue'
    result = parse(ticket, table_name)
    assert type(result) == tuple

def test_parse_for_error_url():
    ticket = 'Error :)'
    table_name = 'Total Revenue'
    with pytest.raises(ValueError):
        parse(ticket, table_name)


def test_parse_for_error_args():
    ticket = 'MSFT'
    table_name = 'Error :)'
    with pytest.raises(AttributeError):
        parse(ticket, table_name)

if __name__ == "__main__":
    test_parse_for_ticket_table_name()
    test_parse_is_tuple()
    test_parse_for_error_url()
    test_parse_for_error_args()