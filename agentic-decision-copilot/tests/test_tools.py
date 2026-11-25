from src.tools.decision_tools import weighted_score, rank_options


def test_weighted_score():
    scores = weighted_score(
        {
            "A": {"impact": 10, "ease": 5},
            "B": {"impact": 7, "ease": 9},
        },
        {"impact": 0.6, "ease": 0.4},
    )
    assert scores["A"] == 8.0
    assert scores["B"] == 7.8


def test_rank_options():
    assert rank_options({"A": 8.0, "B": 7.8}) == ["A", "B"]
