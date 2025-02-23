# IMPORTATIONS
import json
import logging
import degiro_connector.core.helpers.pb_handler as payload_handler

from degiro_connector.trading.api import API as TradingAPI
from degiro_connector.trading.models.trading_pb2 import Credentials, ProductSearch

# SETUP LOGGING LEVEL
logging.basicConfig(level=logging.DEBUG)

# SETUP CONFIG DICT
with open("config/config.json") as config_file:
    config_dict = json.load(config_file)

# SETUP CREDENTIALS
int_account = config_dict.get("int_account")
username = config_dict.get("username")
password = config_dict.get("password")
totp_secret_key = config_dict.get("totp_secret_key")
one_time_password = config_dict.get("one_time_password")

credentials = Credentials(
    int_account=int_account,
    username=username,
    password=password,
    totp_secret_key=totp_secret_key,
    one_time_password=one_time_password,
)

# SETUP TRADING API
trading_api = TradingAPI(credentials=credentials)

# ESTABLISH CONNECTION
trading_api.connect()

# SETUP REQUEST
request_lookup = ProductSearch.RequestLookup(
    search_text="APPLE",
    limit=2,
    offset=0,
    product_type_id=1,
)

# FETCH DATA
products_lookup = trading_api.product_search(request=request_lookup, raw=False)
products_lookup_dict = payload_handler.message_to_dict(message=products_lookup)
pretty_json = json.dumps(products_lookup_dict, sort_keys=True, indent=4)

print(pretty_json)
