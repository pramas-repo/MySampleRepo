# 3. print() with format() and truncating string data
city = 'amravati'

# basic truncate string data
print('{:.5}'.format(city))  # Truncate to 5 characters
print('{:20.5}'.format(city))  # Truncate to 5 characters, right aligned
print('{:>20.5}'.format(city))  # Truncate to 5 characters, left aligned
print('{:^20.5}'.format(city))  # Truncate to 5 characters, center aligned

# Truncate and fill with *
print('{:*<20.5}'.format(city))  # Truncate to 5 characters, left aligned with *
print('{:*>20.5}'.format(city))  # Truncate to 5 characters 
# Truncate to 5 characters, right aligned with *
print('{:#^20.5}'.format(city))  # Truncate to 5 characters, center aligned with #