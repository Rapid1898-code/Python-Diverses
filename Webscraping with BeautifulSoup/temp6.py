txt = "GuV/Bilanz in Mio. USD nach US GAAP - Geschäftsjahresende: 30.09."
new = "Bilanz in Mio. " + txt[18:22].strip() + " per " + txt[-7:-1].strip()
print(new)
