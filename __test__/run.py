class A:

    def __init__(self):

        self.b = "c"

    def _mapping(self):

        return {"tamere": self.b}

    def run(self):

        m = self._mapping()
        m["tamere"] = "d"
        print(self.b)


a = A()
a.run()