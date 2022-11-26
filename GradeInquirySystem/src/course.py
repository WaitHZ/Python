class Course(object):
    school_name = "浙江大学"

    def __init__(self, name, term, credit, score, is_major, is_honor):
        self.name = name
        self.term = term
        self.credit = credit
        self.score = score
        self.GP = self.score_to_gp(score)
        self.isMajor = is_major
        self.isHonor = is_honor

    @staticmethod
    def score_to_gp(score):
        if score >= 95:
            return 5.0
        elif score >= 92:
            return 4.8
        elif score >= 89:
            return 4.5
        elif score >= 86:
            return 4.2
        elif score >= 83:
            return 3.9
        elif score >= 80:
            return 3.6
        elif score >= 77:
            return 3.3
        elif score >= 74:
            return 3.0
        elif score >= 71:
            return 2.7
        elif score >= 68:
            return 2.4
        elif score >= 65:
            return 2.1
        elif score >= 62:
            return 1.8
        elif score >= 60:
            return 1.5
        else:
            return 0

    def __str__(self):
        return f'{self.name}, {self.term}, {self.GP}'
