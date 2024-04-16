data = {'death': ['2022-01-01', '2023-02-15', '2024-03-19', None, '2025-05-10'],
        'birth': ['1994-03-18', '1999-12-31', None, '1988-08-27', '2002-07-10'],
        'year':[2008, 2013, 2009, 2017, 2011]}

birth_years = []
for date in data['birth']:
    if date:
        birth_year = int(date[0:4])
    else:
        birth_year = 2000
    
    birth_years.append(birth_year)

nobel_ages = []
for count in range(len(data['year'])):
    nobel_age = data['year'][count] - birth_years[count]
    nobel_ages.append(nobel_age)

data['nobel age'] = nobel_ages

print(data)
