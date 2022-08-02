import feedparser
import datetime
import delorean

rss = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")

time_limet = delorean.parse(rss.channel.updated) - datetime.timedelta(hours=6)

entries = [entry for entry in rss.entries if delorean.parse(entry.published) > time_limet]

for entry in entries:
    print(f'{entry.title}\n{entry.link}\n{"*"*25}\n')