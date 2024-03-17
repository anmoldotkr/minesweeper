import json
import datetime


class TopScorer:
    def __init__(self, name):
        self.player_name = name+f"_{datetime.datetime.now()}_"
        self.score = 0
        self.file_name = "score.json"

    def read_file(self):
        try:
            with open(self.file_name, 'r') as file:
                scores = json.load(file)
                sorted_scores = sorted(scores.values(), reverse=True)
                if self.score >= sorted_scores[0] :
                    print("CONGRATS YOU ARE THE TOP SCORER\n"
                          + "NAME : " + scores[str(sorted_scores[0])]
                          + "\nSCORE : " + str(sorted_scores[0]) + "\n")
                else:
                    print(f"YOUR SCORE\nNAME : {self.player_name}\nSCORE : {self.score}\n")

                    print(f"HIGHEST SCORE IS SCORED BY \nNAME : {scores[str(sorted_scores[0])]}\nSCORE : {sorted_scores[0]}\n")

        except FileNotFoundError:
            print("No scores found!")

    def write_file(self):
        try:
            scores = {}
            try:
                with open(self.file_name, 'r') as file:
                    scores = json.load(file)
            except FileNotFoundError:
                pass

            scores[self.player_name] = self.score
            with open(self.file_name, 'w') as file:
                json.dump(scores, file, indent=4)
        except IOError as e:
            print(f"Error writing to file: {e}")

    def set_score(self, score: int):

        self.score = score