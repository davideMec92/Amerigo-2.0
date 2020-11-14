class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

person_string = '{"name": "Bob", "age": 25}'

person_dict = json.loads(person_string)
person_object = Person(**person_dict)
