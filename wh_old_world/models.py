from django.db import models

unit_choices = (
    ('Character', 'Character'),
    ('Core', 'Core'),
    ('Special', 'Special'),
    ('Rare', 'Rare')
)

faction_choices = (
    ('Tomb Kings', 'Tomb Kings'),
)

class OldWorldFactions(models.Model):
    faction_name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    def __str__(self):
        return self.faction_name

class OldWorld(models.Model):
    unit_name = models.CharField(max_length=100, null=False, blank=False)
    unit_type = models.CharField(max_length=50, null=False, blank=False, choices=unit_choices, default='Core')
    forces_of_evil_page = models.IntegerField()
    arcane_journal_page = models.IntegerField()
    points_cost = models.IntegerField(null=False, blank=False)
    is_built = models.BooleanField(default=False, null=False, blank=False)
    is_painted = models.BooleanField(default=False, null=False, blank=False)
    faction = models.ForeignKey(OldWorldFactions, on_delete=models.SET_DEFAULT, default=2, related_name='old_world_units')

    def __str__(self):
        return self.unit_name
