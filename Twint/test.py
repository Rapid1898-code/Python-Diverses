import twint

# Configure
c = twint.Config()
c.Username = "krone_at"
# c.Search = "und aber"             # search for twits with "und" and "aber"
# c.Search = "und OR aber"          # serach for twits with "und" or "aber"
c.Search = "\"keine Lieferantin\""  # search exactly for the text "keine Lieferantin"
c.Since = "2021-01-01"
c.Until = "2021-04-20"
c.Limit = 1
c.Store_object = True

# Run
twint.run.Search(c)
tweets = twint.output.tweets_list
for idx,cont in enumerate(tweets):
    print(f"IDX {idx}: {cont.datestamp} {cont.timestamp} {cont.tweet}")


