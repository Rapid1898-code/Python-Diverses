import dateutil.parser as parser

dat1 = "2020-03-31"
dat2 = "02.03.20"

print(parser.parse(dat1).year)
print(type(parser.parse(dat1).year))
print(parser.parse(dat2).year)
print(type(parser.parse(dat2).year))
