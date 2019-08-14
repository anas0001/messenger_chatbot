from wit import Wit

access_token = 'XZB5RJAZUADNCMR6M5IAILDQ76EFUDWJ'

client = Wit(access_token)

message_text = 'i want sports news'

resp = client.message(message_text)

print(resp)
