import requests
import json

googleCivicsAPIKeyString = 'AIzaSyDxM-KB3PNSq4dTWjbj0OWtullNm2FuKw4'

googleCivicsRepresentativeURL = 'https://www.googleapis.com/civicinfo/v2/representatives'


def get_address():
    user_address: str = input("Address: ")
    return user_address


def get_google_civics_representatives_for_address(user_address, office):
    representative_list = []

    if office == 'president':
        role = 'headOfGovernment'
    elif office == 'senate':
        role = 'legislatorUpperBody'
    elif office == 'house':
        role = 'legislatorLowerBody'
    else:
        role = ''
    google_civics_response = requests.get(googleCivicsRepresentativeURL,
                                                 params={'key': googleCivicsAPIKeyString,
                                                         'address': user_address,
                                                         'includeOffices': 'true',
                                                         'levels': 'country',
                                                         'roles': role}).json()
    for electedOfficial in google_civics_response['officials']:
        representative_list.append(electedOfficial['name'])
    return representative_list


def get_federal_representatives_for_address(user_address):
    president = get_google_civics_representatives_for_address(user_address, 'president')
    senators = get_google_civics_representatives_for_address(user_address, 'senate')
    house_reps = get_google_civics_representatives_for_address(user_address, 'house')
    federal_representatives = {"President": president, "Senators": senators, "House Members": house_reps}
    federal_representatives_as_json = json.dumps(federal_representatives)
    return federal_representatives_as_json


userAddress = get_address()
federal_representatives_for_address = get_federal_representatives_for_address(userAddress)

print(federal_representatives_for_address)
