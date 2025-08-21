from django.shortcuts import render

# Create your views here.

def home(request):
    user_data = {
        'name': 'Thirukumaran',
        'title': 'Software Developer',
        'bio': 'Passionate about building scalable web applications and solving complex problems.',
        'email': 'example@example.com',
        'phone': '+91 9874563210',
        'linkedin': 'https://www.linkedin.com/',
        'github': 'https://github.com/',
        'image_url': 'images/profile.jpg',
    }
    return render(request, 'card.html', {'user': user_data})