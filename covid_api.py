import requests


def get_country(data: dict, country: str) -> int or str:
    """Searches API data for country name, returns data for that country."""
    country_index = None
    for index in range(len(data['Countries'])):
        if data['Countries'][index]['Country'] == country:
            country_index = index
    return data['Countries'][country_index] if country_index != None else 'Not found'

def print_country_overview(country: dict) -> None:
    """Prints the revelant data of a country."""
    for each in country:
        if each not in ['ID', 'Slug', 'Premium', 'NewRecovered', 'TotalRecovered']:
            print(f'{each}: {country[each]}')

def get_all_countries(data: dict) -> list:
    """Returns a list of all the countries in the API data."""
    return [country['Country'] for country in data['Countries']]

def main() -> None:
    try:
        response = requests.get('https://api.covid19api.com/summary')
    except:
        print(f'API CONNECTION FAILED')
    else:
        api_data = response.json()

        # Example of getting a country's data/overview
        nl = get_country(api_data, 'Netherlands')
        print_country_overview(nl)
    finally:
        print('--- END ---')

    
if __name__ == '__main__':
    main()
