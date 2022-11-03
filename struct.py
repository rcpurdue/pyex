import json

class Struct():
    """Recursivly convert dictionary to object"""
    # From https://stackoverflow.com/a/1305682

    def __init__(self, data):
        for name, value in data.items():
            setattr(self, name, self._wrap(value))

    def _wrap(self, value):
        if isinstance(value, (tuple, list, set, frozenset)):
            return type(value)([self._wrap(v) for v in value])
        else:
            return Struct(value) if isinstance(value, dict) else value

if __name__ == "__main__":

    with open('example.json', 'rt') as fid:
        data = json.loads(fid.read())

    struct = Struct(data)
    print(struct.glossary.GlossDiv.title)
