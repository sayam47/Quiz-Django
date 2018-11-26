from django.shortcuts import render,HttpResponse
import random
import json
from django.contrib.auth.decorators import login_required

#from .models import QuizQna as Q,QuizScore as S,QuizHistory as H,AuthUser as AU
import pymysql.cursors
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='samyak20',
                             db='quiz',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def homepage(request):
	return render(request,'homepage.html')
prev_a=9

@login_required
def score(request):
	error=True
	if request.session['q']==0:
		error=False
	context={
	'error': error,
	'noq':(request.session['q']),
	'score':request.session['score']
	}
	with connection.cursor() as cursor:
		sql = "UPDATE `quiz_score` SET `s`=`s`+ {} , `noq`=`noq`+ {} WHERE `user`= '{}'".format(request.session['score'],request.session['q'],request.user)
		cursor.execute(sql)
		connection.commit()
		cursor.close()
	request.session['q']=0
	request.session['score']=0

	return render(request,'score.html',context)


@login_required
def qna(request):
	if 'q' not in request.session.keys():
		request.session['q']=0
		request.session['score']=0
	global prev_a
	a=int(random.randint(9,158))
	
	s='jdfwk'
	if request.method == 'POST':
		request.session['q']+=1
		s=str(request.POST.get('selected'))
		a=prev_a
		with connection.cursor() as cursor:
			sql = "SELECT `c` FROM `quiz_qna` WHERE `id`=%s"
			cursor.execute( sql,(a) )
			mm=dict(cursor.fetchone())
			if mm['c']==s:
				request.session['score']+=1


	with connection.cursor() as cursor:
		sql = "SELECT `q`,`c`,`c1`,`c2`,`c3`,`c4` FROM `quiz_qna` WHERE `id`=%s"
		cursor.execute( sql,(a) )
		m=dict(cursor.fetchone())
	prev_a=a

	context={
	'noq': request.session['q'],
	'score': request.session['score'],
	'q':m['q'],
	'c':m['c'],
	'c1':m['c1'],
	'c2':m['c2'],
	'c3':m['c3'],
	'c4':m['c4'],
	's':s,
	}
	return render(request,'qna.html',context)

def lb(request):
	global html
	with connection.cursor() as cursor:
			sql = "SELECT user,s,noq FROM `quiz_score` ORDER BY s DESC, noq ASC"
			cursor.execute( sql )
			m=list(cursor.fetchall())
			k=[]
			j=1
			for i in m:
				temp=0
				try:
					temp= round((i['s']*100)/i['noq'],2)
				except ZeroDivisionError:
					temp=0.00
				k.append({'id':j,'name':i['user'],'score':i['s']})
				j+=1
			data = json.dumps(k)
			m={'m':k}
			return render(request,'leaderboard.html',{'m':data})

			#return render(request,'leaderboard.html',context)









