import math
class Stats:
    @staticmethod
    def get_recomendations(reviews):
        recomendation = {'polecam': 0, 'nie_polecam': 0}
        for review in reviews:
            if review['recomendation'] == 'Polecam':
                recomendation['polecam'] += 1
            else:
                recomendation['nie_polecam'] += 1
        return recomendation

    @staticmethod
    def get_ratings(reviews):
        score = {'0,5': 1 , '1': 0, '1,5': 0, '2': 0, '2,5': 0, '3': 0, '3,5': 0, '4': 0, '4,5': 0, '5': 0}
        
        for review in reviews:
            rating = review['score'].split('/')[0]
            score[rating] += 1
        return score

    @staticmethod
    def calculate_stats(reviews):
        stats = {}
        stats['number_of_opinions'] = len(reviews)
        number_of_props = 0
        number_of_cons = 0
        sum_of_ratings = 0
 
        for review in reviews:
            number_of_props += review['props']
            number_of_cons += review['cons']
            sum_of_ratings += float(review['score'].split('/')[0].replace(',', '.'))

        stats['number_of_props'] = number_of_props
        stats['number_of_cons'] = number_of_cons
        stats['mean_rating'] = round(sum_of_ratings / len(reviews), 2) 
        return stats
