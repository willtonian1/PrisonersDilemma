
class titForTat():
    def __init__(self):
        self.name = "TitForTat"
    def decision():
        return 0

class match():
    def __init__(self, p1, p2):
        p1 = p1
        p2 = p2
    def play():
        return 0
    

class tournament():
    def __init__(self, policies):
        self.policies = policies

    def run(self):
        for policy in self.policies:
            print(policy.name)

a = titForTat()
t = tournament([a])
t.run()
