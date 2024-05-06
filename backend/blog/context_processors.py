# context_processors.py

def menu_links(request):
    menu = [
        {'name': 'Home', 'url': ''},
        {'name': 'Blog', 'url': 'blog'},
        {'name': 'About', 'url': 'about'},
        {'name': 'Project', 'url': 'project'}
    ]
    site = {
        'gitlab': {
            'url': 'https://gitlab.com/ptmkhanh29',
            'icon': 'img_icon/gitlab-icon.svg'
        },
        'github': {
            'url': 'https://github.com/ptmkhanh29',
            'icon': 'img_icon/github-icon.svg'
        },
        'linkedin': {
            'url': 'https://www.linkedin.com/in/ptmkhanh29',
            'icon': 'img_icon/linkedin-icon.svg'
        },
        'facebook': {
            'url': 'https://www.facebook.com/MinhKhanhPhanTruong',
            'icon': 'img_icon/facebook-icon.svg'
        },
        'email': {
            'url': 'mailto:ptmkhanh29@gmail.com',
            'icon': 'img_icon/email-icon.svg'
        }
    }
    domain = {
        'name': 'Khanh Phan',
        'url': 'http://127.0.0.1:8000/'
    }
    
    return {
        'menu': menu,
        'site': site,
        'domain': domain
    }

