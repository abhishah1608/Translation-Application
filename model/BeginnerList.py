import json
from typing import List
from dataclasses import dataclass

from model.BeginnerBo import BeginnerBo


@dataclass
class BeginnerList:
    beginnerlst: List[BeginnerBo]


    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4, ensure_ascii= False).encode('utf8')