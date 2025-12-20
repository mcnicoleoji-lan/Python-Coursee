country_code = {
    'Nigeria': '0234',
    'Australia': '0025',
    'Nepal': '00977'
}

# search dictionary for country code of Nigeria
print("Country code for Nigeria -")
print(country_code.get('Nigeria', 'Not Found'))

# search dictionary for country code of Japan
print("Country code for Japan -")
print(country_code.get('Japan', 'Not Found'))
