from typing import Any, Callable
from dataclasses import dataclass

@dataclass
class Rule:
    name: str
    description: str
    condition: Callable[[dict[str, Any]], bool]
    recommendation: str


class KnowledgeBase:
    def __init__(self, rules: list[Rule]):
        self.rules = rules

    def infer(self, facts: dict) -> list[Rule]:
        fired = []
        for rule in self.rules:
            try:
                if rule.condition(facts):
                    fired.append(rule)
            except Exception:
                continue
        return fired