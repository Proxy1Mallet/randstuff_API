class obj_number:
    def __init__(self, data):
        self.json = data
        self.number = None
        self.save = None

    @property
    def obj_number(self):
        try: self.number = self.json['number']
        except(KeyError, TypeError): pass
        try: self.save = self.json['save']
        except(KeyError, TypeError): pass
        return self

class obj_password:
    def __init__(self, data):
        self.json = data
        self.password = None

    @property
    def obj_password(self):
        try: self.password = self.json['password']
        except(KeyError, TypeError): pass
        return self

class obj_ask:
    def __init__(self, data):
        self.json = data
        self.ask = None
        self.question = None

    @property
    def obj_ask(self):
        try: self.ask = self.json['ask']['prediction']
        except(KeyError, TypeError): pass
        try: self.question = self.json['ask']['question']
        except(KeyError, TypeError): pass
        return self

class obj_ticket:
    def __init__(self, data):
        self.json = data
        self.ticket = None
        self.lucky = None
        self.stat = None
        self.count = None
        self.countLucky = None

    @property
    def obj_ticket(self):
        try: self.ticket = self.json['ticket']
        except(KeyError, TypeError): pass
        try: self.lucky = self.json['lucky']
        except(KeyError, TypeError): pass
        try: self.stat = self.json['stat']
        except(KeyError, TypeError): pass
        try: self.count = self.json['stat']['count']
        except(KeyError, TypeError): pass
        try: self.countLucky = self.json['stat']['lucky']
        except(KeyError, TypeError): pass
        return self

class obj_fact:
    def __init__(self, data):
        self.json = data
        self.fact = None
        self.id = None
        self.text = None

    @property
    def obj_fact(self):
        try: self.fact = self.json['fact']
        except(KeyError, TypeError): pass
        try: self.id = self.json['fact']['id']
        except(KeyError, TypeError): pass
        try: self.text = self.json['fact']['text']
        except(KeyError, TypeError): pass
        return self

class obj_saying:
    def __init__(self, data):
        self.json = data
        self.saying = None
        self.author = None
        self.id = None
        self.text = None

    @property
    def obj_saying(self):
        try: self.saying = self.json['saying']
        except(KeyError, TypeError): pass
        try: self.author = self.json['saying']['author']
        except(KeyError, TypeError): pass
        try: self.id = self.json['saying']['id']
        except: pass
        try: self.text = self.json['saying']['text']
        except(KeyError, TypeError): pass
        return self