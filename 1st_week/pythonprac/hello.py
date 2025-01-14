def get_age(name):
    people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]
    reply = '그런 이름이 없습니다.'
    for p in people:
        if p['name'] == name:
            reply = str(p['age'])

    return reply


print(get_age('bob'))
print(get_age('john'))
print(get_age('bk'))