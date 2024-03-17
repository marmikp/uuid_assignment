

from typing import List
from rule_engine.rules import ValidationRule


class ValidationRuleEngine:
    def __init__(self, rules: List[ValidationRule]):
        self.rules = rules
    
    def execute(self, entity):
        errors = []
        for rule in self.rules:
            if rule.is_applicable(entity):
                errors.append(rule.get_error(entity))
        return errors

