class Question:
    def __init__(self, path):
        with open(path, "r") as file:
            data = file.read()

        data = data.split('\n')
        self.question = data[0]
        self.answers = [data[1][2:], data[2][2:], data[3][2:], data[4][2:]]
        correct_answer = data[5][-1:]
        match correct_answer:
            case "A":
                self.correct_answer = 0
            case "B":
                self.correct_answer = 1
            case "C":
                self.correct_answer = 2
            case "D":
                self.correct_answer = 3
