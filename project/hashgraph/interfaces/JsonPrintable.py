import json

class JsonPrintable():
    def toJson(self) -> str:
        return json.dumps(self, default=lambda o: dict((key, value) for key, value in o.__dict__.items() if value), allow_nan=False)

    def toPrettyJson(self) -> str:
        return json.dumps(self, default=lambda o: dict((key, value) for key, value in o.__dict__.items() if value), allow_nan=False, sort_keys=True, indent=4)
