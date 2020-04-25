from django.contrib import admin
from .models import Team, Player, RatingPlayer, Rating, Conference

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Rating)
admin.site.register(RatingPlayer)
admin.site.register(Conference)