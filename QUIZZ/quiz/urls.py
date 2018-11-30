from django.urls import path,include
from django.contrib.auth import urls
from .views import homepage,qna,score,lb,profile
from .feeds import LatestEntriesFeed
urlpatterns = [
	path('',homepage, name='home'),
	path('',include(urls)),
	path('qna/',qna, name='qna'),
	path('score/',score, name='score'),
	path('leaderboard/',lb, name='leaderboard'),
	#path('signup/',signup, name='signup'),
	path('feeds/', LatestEntriesFeed(),  name='feeds'),
	path('profile/<str:user_name>/',profile,name='profile')
]