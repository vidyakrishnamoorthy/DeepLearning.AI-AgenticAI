from typing import Dict, List


def weighted_score(options: Dict[str, Dict[str, float]],
                   weights: Dict[str, float]) -> Dict[str, float]:
    """Compute weighted decision scores.

    options example:
      {"Build": {"impact": 8, "cost": 3}, "Wait": {"impact": 5, "cost": 8}}
    weights example:
      {"impact": 0.7, "cost": 0.3}

    All criterion values should already use the same direction:
    higher = better.
    """
    results = {}
    for option, criteria in options.items():
        results[option] = round(
            sum(criteria.get(k, 0) * weight for k, weight in weights.items()), 3
        )
    return results


def rank_options(scores: Dict[str, float]) -> List[str]:
    return [
        option for option, _ in
        sorted(scores.items(), key=lambda item: item[1], reverse=True)
    ]


TOOLS = {
    "weighted_score": weighted_score,
    "rank_options": rank_options,
}
