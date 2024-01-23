from django.shortcuts import render , redirect , get_object_or_404
from .models import chat , exchange , product , service , verify , cart , order
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import login , authenticate , logout
# Create your views here.


def home(request):
    u = request.user
    return render ( request , 'app/home.html',{'u':u})


def register(request):
    if request.method == 'POST':
        u = request.POST.get('u')
        p = request.POST.get('p')
        e = request.POST.get('e')
        print(u,p)
        User.objects.create_user(username = u , email = e , password = p).save()
        return redirect (loginn)
    return render ( request , 'app/register.html' )

def loginn(request):
    if request.method == 'POST':
        u = request.POST.get('u')
        p = request.POST.get('p')
        print(u,p)
        n = authenticate(request , username = u , password = p)
        print(n)
        if n  is not None:
            login(request , n )
            return redirect (home)
    return render ( request , 'app/login.html')

def logoutt(request):
    logout(request)
    return redirect (loginn)


def sell(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        model = request.POST.get('model')
        email = request.POST.get('email')
        discription = request.POST.get('discription')
        image = request.FILES.get('image')
        
        verify.objects.create(name = name , model = model , email = email , discription = discription   , img = image  ).save()
        return redirect (home)
    return render ( request , 'app/sell.html')

def verifyy(request):
    p = 'admin'
    n = 'no obj'
    if request.user.username  == p:
        n = verify.objects.all()
        return render ( request , 'app/verify.html',{'n':n,'m':f'welcome {request.user}'})
    return render ( request , 'app/verify.html',{'n':n,'m':f'no entry for {request.user}'})    
    


def ver(request,id =id):
    n = get_object_or_404(verify , id = id )
    product.objects.create(name = n.name , model = n.model , email = n.email , discription = n.discription  , img = n.img ).save()
    n.delete()
    return redirect (verifyy)


def buy(request):
    n = product.objects.all()
    return render ( request , 'app/buy.html' , {'n':n})

def b(request , id = id ):
    n = get_object_or_404(product , id = id )
    return render ( request , 'app/b.html' , {'n':n})

def exchangee(request):
    n = exchange.objects.all()
    if request.method == 'POST':
        n = request.POST.get('n')
        m = request.POST.get('m')
        e = request.POST.get('e')
        d = request.POST.get('d')
        image = request.FILES.get('image')
        exchange(name = n , model = m ,email = e , discription = d , img = image ).save()
        return redirect (exchangee)
    return render ( request , 'app/exchange.html' , {'n' :n })

def servicee(request):
    p = 'admin'
    if request.user.username == p:
        n =service.objects.all()
        return render ( request , 'app/service.html',{'n' : n})
    else:
        if request.method == 'POST':
            m = request.POST.get('m')
            p = request.POST.get('p')
            service.objects.create(model = m , problem = p).save()
            return redirect (home)

        return render ( request , 'app/service.html',{'n':'no obj'})
    

def chatt(request):
    p = 'admin'
    if request.user.username == p:
        n = chat.objects.all()
        m='p'
        return render ( request , 'app/chat.html' ,{'n' : n ,'m':m})
    else:
        n = chat.objects.filter ((Q(user__username=request.user.username) & Q(t = 'admin')) | (Q(user__username='admin') & Q(t = request.user.username)))
        if request.method == 'POST':
            m = request.POST.get('m')
            chat.objects.create(user=request.user, message_f=m , t = 'admin').save()
            
            return redirect (chatt)
        
        return render ( request , 'app/chat.html' ,{'n' : n ,'m':'no obj' })
        


def c(request , id ):
    n = chat.objects.filter(user__id = id)
    t  = chat.objects.filter(user__id = id).first()
    print(t.user.username)
    if request.method == 'POST':
        m = request.POST.get('m')
        chat.objects.create(user = request.user , message_f = m , t = t.user.username ).save()
        return redirect (chatt)
    return render ( request , 'app/c.html' , {'n' : n})

def cartt(request , id = id):
    p = get_object_or_404(product , id = id )
    cart.objects.create(user = request.user ,name = p.name , model = p.model , email = p.email , discription = p.discription ).save()
    return redirect (home)

def ca(request , id = id ):
    n = cart.objects.filter(user__username = request.user.username )
    return render ( request , 'app/ca.html',{'n':n})


def dc(request , id = id ):
    print(id)
    n = get_object_or_404(cart , id  = id )
    n.delete()
    return redirect (ca , n.user.id)


def orderr(request , id = id ):
    p = get_object_or_404(cart , id = id)
    n = p
    p.delete()
    order.objects.create(user = request.user , name = n.name , model = n.model , email = n.email , discription = n.discription ).save()
    return redirect (ca , n.user.id )

def ord(request , id = id):
    n = order.objects.filter(user__id = id )
    return render ( request , 'app/or.html' , {'n' : n})



def de(request):
    n = User.objects.exclude(id = 1 )
    return render ( request , 'app/de.html' , {'n' : n})

def ud(request , id = id ):
    n = get_object_or_404(User , id = id )
    n.delete()
    return redirect (de)