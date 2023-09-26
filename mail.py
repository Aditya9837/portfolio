import requests

def handler(pd: "pipedream"):
  headers = {"Authorization": f'Zoho-oauthtoken {pd.inputs["zoho_mail"]["$auth"]["oauth_access_token"]}'}
  r = requests.get(f'https://mail.{pd.inputs["zoho_mail"]["$auth"]["base_api_uri"]}/api/accounts', headers=headers)
  # Export the data for use in future steps
  return r.json()
print(handler("pipedream"))