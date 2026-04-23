from sorting import random_numbers
class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        skore=self.scores[index]
        if skore >= 90:
            return "A"
        elif skore >= 80:
            return "B"
        elif skore >= 70:
            return "C"
        elif skore >= 60:
            return "D"
        elif skore >= 50:
            return "E"
        else:
            return "F"

    def find(self, body):
        index=[]
        for value in range(len(self.scores)):
            if self.scores[value] == body:
                index.append(value)
                return index

    def get_sorted(self):
        scores = list(self.scores)
        for i in range(len(scores) - 1):
            for x in range(len(scores) - 1):
                if scores[x] > scores[x + 1]:
                    scores[x + 1], scores[x] = scores[x], scores[x + 1]
        return scores
def main():
    # results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    results = StudentsGrades(random_numbers(30, 0, 100))
    print(f"Test psalo: {results.count()} studentů")
# print(results.get_by_index(2))  # 91
# print(results.scores) # [85, 42, 91, 67, 50, 73, 100, 38, 58]
# print(results.get_grade(2))
    print(f"Plný počet bodů měl/i studenti na : {results.find(100)} indexu")
    print(f"Seřazené výsledky: {results.get_sorted()}")
    for index in range(results.count()):
        print(f"Student {index}: {results.get_by_index(index)} points - {results.get_grade(index)}")

if __name__ == "__main__":
    main()

