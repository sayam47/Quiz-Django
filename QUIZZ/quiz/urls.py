from django.urls import path,include
from django.contrib.auth import urls
from .views import homepage,qna,score,lb
urlpatterns = [
	path('',homepage,name='home'),
	path('',include(urls)),
	path('qna/',qna,name='qna'),
	path('score/',score,name='score'),
	path('leaderboard/',lb,name='leaderboard'),
]