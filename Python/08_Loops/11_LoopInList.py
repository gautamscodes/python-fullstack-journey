countries = ["India", "United States", "Australia", "Ireland", "Sri Lanka",
             "Iceland", "Cuba", "Iran", "Poland"]

# Count all the countries which are starting with "I"
# Also, print all these countries as a list
# ['India', 'Ireland', 'Iceland', 'Iran']



counter = 0
output = []
for country in countries:
    # if country[0] == 'I':
    if country.startswith('I'):
        counter = counter + 1
        output.append(country)
print(counter)
print(output)




