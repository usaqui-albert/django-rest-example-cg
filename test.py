from ConnectGood.settings import BENEVITY_COMPANY_ID, BENEVITY_API_KEY
from benevity_library import benevity

from pprint import PrettyPrinter

pp = PrettyPrinter(indent=1)

benevity.api_key = 'soothai8to9yab6E'
benevity.company_id = '1VHRBZWMAL'

query_params = {
    'user': '2ec25bf3-5f36-40bd-925a-69b23c15586e',
    'lastname': 'Usaqui',
    'firstname': 'Albert',
    'email': 'usaqui.albert@gmail.com',
    'country': '124',
    'address-city': 'Toronto',
    'address-country': '124',
    'address-state': 'Alberta',
    'address-postcode': '123-456',
    'address-street': 'Plaza Venezuela',
    'active': 'yes'
}

benevity_users = benevity.get_company_user_list()
pp.pprint(benevity_users)

user_updated = benevity.update_user(user='111', firstname='Albert')
pp.pprint(user_updated)
