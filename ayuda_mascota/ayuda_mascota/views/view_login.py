from django.shortcuts import render, redirect
import traceback
from django.contrib.auth import login as login_user, authenticate, logout as logout_user

def login(request):
    print('login')
    if request.method == 'GET':
        return render(request, 'login.html', {'message_error' : None}) 
    elif request.method == 'POST':
        try:
            print('request_post:', request.POST)
            user = request.POST['username']
            password = request.POST['password'] 
            
            username = authenticate(username=user, password=password)
            print('username: ', username)                    
            if username is not None:
                login_user(request, username)         
                return redirect('/home/')
            else:
                return render(request, 'login.html', {'message_error' : 'USUARIO O CONTRASEÑA INVALIDA'}) 
        except Exception as e:
            traceback.print_exc()
            return render(request, 'login.html', {'message_error' : 'ERROR INESPERADO INTENTE MAS TARDE'})         


def logout(request): 
    print('logout')
    try:    
        logout_user(request)
    except Exception as e:
        print('Error: ', e)        
    return redirect('/')