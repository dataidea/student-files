# if expression:
#     statements
#     statements
#     statements

adult = input('Are you 18+ enter y for yes, and n for no: ')

if adult == 'y':
    male_or_female = input('Interested in men or women, enter m, and w, women: ')
    if male_or_female == 'm':
        print('Men videos')
    else:
        print('Women videos')
else:
    print('redirect to youtube for kids')
