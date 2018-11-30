from django.shortcuts import render
def ipfilter(get_response):
    def middleware(request):
        allowed_ips=['127.0.0.1']
        ip=request.META.get('REMOTE_ADDR')
        ip1=ip.split('.')
        if ip1[0]=='172':
            allowed_ips.append(ip)
        print(ip)
        if ip not in allowed_ips:
        	return render(request,'filter.html')
            #return HttpResponse('ACCESS DENIED')
        response=get_response(request)
        return response
    return middleware