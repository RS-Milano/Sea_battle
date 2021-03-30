class Cat:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex

    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = str(name)

    def set_sex(self, sex):
        if isinstance(sex, str):
            if sex.lower() == "male" or sex.lower() == "female":
                self.sex = sex
            else:
                return "expects string: male or female"
        else:
            return "expects string: male or female"

    def set_age(self, age):
        if isinstance(age, int):
            if age > 0:
                self.age = age
            else:
                return "expects a non-negative integer"
        else:
            return "expects a non-negative integer"

    def represent(self):
        print(f"\nName: {self.name}\nSex:  {self.sex}\nAge:  {self.age}")