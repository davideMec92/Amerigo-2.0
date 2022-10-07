import json


class JsonPrintable:
    def toJson(self) -> str:
        return json.dumps(self, default=lambda o: dict(
            (key, value) for key, value in o.__dict__.items() if self.filter(value)), allow_nan=False, sort_keys=True, separators=(',',':'))

    def toPrettyJson(self) -> str:
        return json.dumps(self, default=lambda o: dict((key, value) for key, value in o.__dict__.items() if self.filter(value)),
                          allow_nan=False, sort_keys=True, indent=4)

    def filter(self, value) -> bool:
        if value is None:
            return False

        return True
