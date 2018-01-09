import random

class survey:

    def __init__(self, population, sample):
        self.population = population
        self.sample = sample
        self.votes = []

    def mock_votes(self):
        for i in range(0, int(self.population)):
            vote = self.get_vote()
            self.votes.append(vote)

    def get_vote(self):
        prob = random.random()
        if prob < 0.3:
            return 'Lula'
        elif prob < 0.4:
            return 'Marina'
        elif prob < 0.5:
            return 'Alckmin'
        elif prob < 0.6:
            return 'Marcio'
        elif prob < 0.7:
            return 'Luciano'
        else:
            return 'Bolsonaro'

    def mock_survey_results(self):
        survey_votes = []
        for i in range(0, int(self.sample)):
            survey_votes.append(random.choice(self.votes))
        return survey_votes

    def survey_results_percentage(self, survey_votes):
        grouped_votes = {}
        total_vote_count = 0
        for value in survey_votes:
            if value not in grouped_votes:
                grouped_votes[value] = 0
            grouped_votes[value] += 1
            total_vote_count += 1

        normalized_grouped_votes = {} 
        for vote_group, vote_count in grouped_votes.items():
            normalized_grouped_votes[vote_group] = float(vote_count)/float(total_vote_count) * 100
        return normalized_grouped_votes

    def run(self):
        self.mock_votes()
        results = self.mock_survey_results()
        percentage = self.survey_results_percentage(results)
        print percentage

app = survey(population = 200E6, sample = 1000)
app.run()
