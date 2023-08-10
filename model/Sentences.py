import json
from typing import List
from typing import Any
from dataclasses import dataclass

from model.Sentence import Sentence


@dataclass
class Sentences:
    sentences: List[Sentence]

    @staticmethod
    def from_dict(obj: Any) -> 'Sentences':
        _sentences = json.loads(obj)
        return Sentences(_sentences)