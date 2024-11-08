from django.shortcuts import render


def resume(request):
    context = {
        'name': 'Dhruv Nair',
        'title': 'Student',
        'contact_info': {
            'email': 'dhruv14nair@gmail.com',
            'phone': '+91 9958823091',
            'linkedin': 'www.linkedin.com/in/dhruv-nair-8525aa2a7',
            'github': 'https://github.com/Nair3091',
        },
        'education': [
            {
                'institution': 'Sri Chaitanya School',
                'degree': 'Class 10',
                'year': '2021',
            },
            {
                'institution': 'Meluha School',
                'degree': 'Class 12',
                'year': '2023',
            },
            {
                'institution': 'KL University, Hyderabad',
                'degree': 'Bachelor of Technology in Artificial Intelligence and Data Science',
                'year': '2023-2027',
            },
            # Add more entries as needed
        ],
        'achievements': [
            'Article Published in National Newspaper',
            'C2 Level in English',
        ],
        'skills': [
            'Python Programming',
            'Java Programming',
            'Professional Writing',
        ],
        'hobbies_and_interests': [
            'Public Speaking',
            'Writing',
            'Reading Manga',
            'Martial Arts'
        ],
        'languages': [
            'English',
            'Hindi',
            'Telugu'
        ]
    }
    return render(request, 'resume.html', context)