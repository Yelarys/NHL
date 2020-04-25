from django.db import models

class Conference(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField("Логотип", upload_to="conference/")
    stars = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Конференция"
        verbose_name_plural = "Конференции"

class Team(models.Model):
    name = models.CharField(max_length=255)
    acronym = models.CharField(max_length=5)
    image = models.ImageField("Изображение", upload_to="teams/")
    conference = models.CharField(max_length=255, choices=(("E", "Eastern"), ("W", "Western")))
    seasons_played = models.PositiveIntegerField()
    cup_appearances = models.PositiveIntegerField()
    titles = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"

class Player(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField("Изображение", upload_to="players/")
    country = models.CharField(max_length=150)
    position = models.CharField(max_length=255, choices=(("R", "Right Wing"), ("L", "Left Wing"), ("C", "Center"), ("D", "Defense")))
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    games_played = models.PositiveIntegerField()
    goals = models.PositiveIntegerField()
    assists = models.PositiveIntegerField()
    points = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Игрок"
        verbose_name_plural = "Игроки"

class RatingPlayer(models.Model):

    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Звездный игрок"
        verbose_name_plural = "Звездные игроки"

class Rating(models.Model):
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingPlayer, on_delete=models.CASCADE, verbose_name="Игрок")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name="Команда")

    def __str__(self):
        return f"{self.star} - {self.team}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"
