class Stats:
    def __init__(self, point):
        self.point = point
        self.score = 0

    def calcule_score(self):
        self.score = self.score + self.point
        return self.score

    def get_score(self):
        pass

    def set_score(self):
        pass
