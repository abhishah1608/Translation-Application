from dataclasses import dataclass
from numbers import Number
from typing import Any

from model.Sentences import Sentences


@dataclass
class BeginnerBo:
    id, english_sentence, translated_sentence = None, None, None

    id: Number
    english_sentence: str
    translated_sentence: Sentences

    @staticmethod
    def from_dict(obj: Any) -> 'BeginnerBo':
        _id = Number(obj.get("id"))
        _english_sentence = str(obj.get("english_sentence"))
        _translated_sentence = Sentences(obj.get("translated_sentence"))
        return BeginnerBo(_id, _english_sentence,_translated_sentence)