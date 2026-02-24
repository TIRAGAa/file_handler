import pytest
from script.core import process_data, sort_report_data


@pytest.fixture
def valid_gdp_data():
    return [
        {"country": "Spain", "gdp": "100"},
        {"country": "Spain", "gdp": "200"},
        {"country": "France", "gdp": "300"},
    ]


@pytest.fixture
def inflation_data():
    return [
        {"country": "France", "inflation": "2.0"},
        {"country": "France", "inflation": "4.0"},
        {"country": "Germany", "inflation": "6.0"},
    ]


@pytest.mark.parametrize(
    "data, report_type, expected",
    [
        (
            [
                {"country": "Spain", "gdp": "100"},
                {"country": "Spain", "gdp": "200"},
            ],
            "gdp",
            {"Spain": 150.0},
        ),
        (
            [
                {"country": "France", "inflation": "2.0"},
                {"country": "France", "inflation": "4.0"},
                {"country": "Germany", "inflation": "6.0"},
            ],
            "inflation",
            {"France": 3.0, "Germany": 6.0},
        ),
        (
            [],
            "gdp",
            {},
        ),
    ],
)
def test_process_data_success(data, report_type, expected):
    assert process_data(data, report_type) == expected


@pytest.mark.parametrize(
    "data, report_type",
    [
        ([{"country": "Spain", "gdp": "100"}], "wrong_key"),
        ([{"country": "France", "population": "67"}], "gdp"),
    ],
)
def test_process_data_wrong_key_returns_empty_dict(data, report_type, capsys):
    result = process_data(data, report_type)

    # Проверяем, что вернулся пустой словарь
    assert result == {}

    # Проверяем, что было выведено сообщение об ошибке
    captured = capsys.readouterr()
    assert "Wrongly enter the --report" in captured.out


@pytest.mark.parametrize(
    "input_data, expected_order",
    [
        (
            {"Spain": 150, "France": 300, "Germany": 200},
            ["France", "Germany", "Spain"],
        ),
        (
            {"A": 1, "B": 2},
            ["B", "A"],
        ),
    ],
)
def test_sort_report_data(input_data, expected_order):
    result = sort_report_data(input_data)
    ordered_countries = [row[1] for row in result]
    assert ordered_countries == expected_order


def test_sort_report_data_empty():
    assert sort_report_data({}) == []
