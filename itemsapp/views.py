from django.shortcuts import render
from .models import Item
# Create your views here


# class Treasure:
#     def __init__(self, name, value, material, location):
#         self.name = name
#         self.value = value
#         self.material = material
#         self.location = location
#         # self.img_url = img_url


# treasures = [
#     Treasure('Gold nugget', 500.00, 'gold', 'O.K. Corral Canion'),
#     Treasure('Fool\'s Gdld', 0.00, 'pyrite', 'Blue River'),
# ]


def home(request):
    items = Item.objects.all()
    return render(request, 'generalapp/home.html', {'items': items})



# now in the index template we may iterate through the list with
# {% for treasure in treasures %}
#   <p>{{ treasue }} {{ treasure.name }}, {{ treasure.value }} etc...
#   </p>
# {% endfor %}
"""
and more:
{% for treasure in treasures %}
    {% if treasure.value > 0 %}
        <p> We found a treasure {{ treasure.name }}! It may be worth about {{ treasure.value }}.</p>
    {% else %}
        <p>We found something, yet it does not seem to be valuable... It's {{ treasure.name }}.</p>
    {% endif %}
{% endfor %}

"""
