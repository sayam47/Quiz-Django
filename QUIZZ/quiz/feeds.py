from django.contrib.syndication.views import Feed
from django.urls import reverse
import pymysql.cursors
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='samyak20',
                             db='quiz',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


class LatestEntriesFeed(Feed):
    title = "Maximum Score"
    link = "/feeds"
    description = "Updates When Leaderboards top 5 are changed"

    def items(self):
        with connection.cursor() as cursor:
            sql = " SELECT * FROM `quiz_score` ORDER BY `s` DESC LIMIT 5"
            cursor.execute(sql)
        return list(cursor.fetchall())

    def item_title(self, item):
        return item['user']

    def item_description(self, item):
        return item['s']

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('score')