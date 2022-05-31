# This script is for scrapping www.allocine.fr movies and series french reviews
# with their respective ranking. Result will be stored in a csv file.

import bs4
import requests
import tqdm
import pandas as pd

CSV_FILENAME = "allocine_reviews.csv"

# Movie names and their respective review urls manually collected from www.allocine.fr

movies_series_dict = {'Top Gun: Maverick': {'number of pages': 34,
                                            'review url': 'https://www.allocine.fr/film/fichefilm-186636/critiques/spectateurs/'},

                      'Don Juan': {'number of pages': 3,
                                   'review url': "https://www.allocine.fr/film/fichefilm-279869/critiques/spectateurs/"},

                      'Docteur Strange in the multiverse of madness': {'number of pages': 34,
                                                                       'review url': "https://www.allocine.fr/film/fichefilm-251390/critiques/spectateurs/"},

                      'Les animaux fantastiques: Les secrets de Dumbledore': {'number of pages': 31,
                                                                              'review url': "https://www.allocine.fr/film/fichefilm-228087/critiques/spectateurs/"},

                      'Les secrets de la cite perdue': {'number of pages': 12,
                                                        'review url': "https://www.allocine.fr/film/fichefilm-287082/critiques/spectateurs/"},

                      'Sonic 2 Le film': {'number of pages': 10,
                                          'review url': "https://www.allocine.fr/film/fichefilm-281203/critiques/spectateurs/"},

                      'The Northman': {'number of pages': 20,
                                       'review url': "https://www.allocine.fr/film/fichefilm-278182/critiques/spectateurs/"},

                      'Stranger things': {'number of pages': 61,
                                          'review url': "https://www.allocine.fr/series/ficheserie-19156/critiques/"},

                      'Star Wars Obi-Wan Kenobi': {'number of pages': 6,
                                                   'review url': "https://www.allocine.fr/series/ficheserie-25501/critiques/"},

                      'Game of Thrones': {'number of pages': 248,
                                          'review url': "https://www.allocine.fr/series/ficheserie-7157/critiques/"},

                      'The Walking Dead': {'number of pages': 226,
                                           'review url': "https://www.allocine.fr/series/ficheserie-7330/critiques/"}}


def main():
    # Data initialisation
    data = {'movie_series_name': [], 'review_note': [], 'review_text': []}

    number_of_extractions = 0

    # Loop through all movies/series in dictionary
    for movie_series_name, movie_infos in movies_series_dict.items():

        number_of_pages = movie_infos['number of pages']
        review_url = movie_infos['review url']

        print(f'Scrapping "{movie_series_name}" reviews:')

        # Loop through all pages in the movie reviews critic page
        for page_number in tqdm.tqdm(range(1, number_of_pages + 1)):

            # scrap page contents

            page_url = f"{review_url}?page={page_number}"

            source = requests.get(page_url)

            if source is None:
                continue

            soup = bs4.BeautifulSoup(source.text, 'lxml')

            # loop through all reviews in the html text
            for review in soup.find_all('div', class_="hred review-card cf"):

                try:

                    # Get ranking and text review
                    review_note = float(review.find('span', class_="stareval-note").text.replace(',', '.'))
                    review_text = review.find('div', class_="content-txt review-card-content").text

                    # Append them in data
                    data['movie_series_name'].append(movie_series_name)
                    data['review_note'].append(review_note)
                    data['review_text'].append(review_text)

                    number_of_extractions += 1

                except AttributeError:
                    continue

        print()

    # Transform dictionary into a pandas DataFrame
    data_df = pd.DataFrame(data)

    # Save the DataFrame into a csv file
    data_df.to_csv(CSV_FILENAME)

    print(f'\nTotal of {number_of_extractions} reviews scrapped. File saved in "{CSV_FILENAME}" .')


if __name__ == '__main__':
    main()
