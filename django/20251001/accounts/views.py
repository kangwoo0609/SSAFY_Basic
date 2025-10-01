from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm, CustomUserChangeForm


# 회원 가입 페이지 (GET)
# 회원 가입 기능 (POST)
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()  # DB 저장 (저장한 유저 객체를 반환)
            auth_login(request, user)  # 자동 로그인 (세션 만들기)
            return redirect("bakeries:index")
    else:
        form = SignupForm()
    
    context = {
        'form': form,
    }

    return render(request, "accounts/signup.html", context)


# 로그인 페이지 (GET)
# 로그인 기능 (POST)
def login(request):
    if request.user.is_authenticated:
        return redirect("bakeries:index")

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)  # 로그인

            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect("bakeries:index")
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, "accounts/login.html", context)


# GET - URL 안에 계정 정보를 담아야 함 --> 남들이 우리 id 로그아웃 시켜버림
# GET vs POST (DB의 데이터 (세션) 를 삭제)
def logout(request):
    auth_logout(request)
    return redirect("bakeries:index")

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        # form = CustomUserChangeForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)