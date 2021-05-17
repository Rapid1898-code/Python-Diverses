import pprint as pp

sample_dict = {
    'name': 'Chris',
    'age': 33,
    'message': 'Thank you for reading my article!',
    'topic':'Python Programming'
}
pp.pprint(sample_dict)                  # pretty print dict line by line
pp.pprint(sample_dict, width=30)        # pretty print with max line-length 30

sample_list = ['level1', ['level2', ['level3']]]
pp.pprint(sample_list, depth=1)           # pretty print only level 1 of nested list eg. ['level1', [...]]
pp.pprint(sample_list, depth=2)           # pretty print only level 2 of nested list eg. ['level1', ['level2', [...]]]

