from django.db import models

unit_choices = (
    ('HQ', 'HQ'),
    ('Troops', 'Troops'),
    ('Elites', 'Elites'),
    ('Fast Attack', 'Fast Attack'),
    ('Heavy Support', 'Heavy Support'),
    ('Flyer', 'Flyer'),
    ('Dedicated Transport', 'Dedicated Transport'),
    ('Lord of War', 'Lord of War'),
    ('Fortification', 'Fortification'),
)

faction_choices = (
    ('Blood Angels', 'Blood Angels'),
    ('Dark Angels', 'Dark Angels'),
    ('Salamanders', 'Salamanders'),
    ('Ultramarines', 'Ultramarines'),
    ('Chaos Space Marines', 'Chaos Space Marines'),
    ('Astra Militarum', 'Astra Militarum'),
    ('Orks', 'Orks'),
    ('Necrons', 'Necrons'),
    ('Tau', 'Tau'),
    ('Tyranids', 'Tyranids'),
    ('Genestealer Cults', 'Genestealer Cults'),
    ('Chaos Daemons', 'Chaos Daemons'),
    ('Sisters of Battle', 'Sisters of Battle'),
    ('Adeptus Mechanicus', 'Adeptus Mechanicus'),
    ('Adeptus Custodes', 'Adeptus Custodes'),
    ('Grey Knights', 'Grey Knights'),
    ('Death Guard', 'Death Guard'),
    ('Thousand Sons', 'Thousand Sons'),
    ('Harlequins', 'Harlequins'),
    ('Drukhari', 'Drukhari'),
    ('Craftworlds', 'Craftworlds'),
    ('Ynnari', 'Ynnari'),
    ('Imperial Knights', 'Imperial Knights'),
    ('Chaos Knights', 'Chaos Knights'),
)

# Simple factions table to link to the force org
class Factions(models.Model):
    faction_name = models.CharField(max_length=100, choices=faction_choices, unique=True, null=False, blank=False)
    def __str__(self):
        return self.faction_name

# Simple force org model all fields are required except the codex page
class wh40k(models.Model):
    unit_name = models.CharField(max_length=100, null=False, blank=False)
    unit_type = models.CharField(max_length=50, choices=unit_choices, default='Troops', null=False, blank=False)
    codex_page = models.IntegerField()
    points_cost = models.IntegerField(null=False, blank=False)
    is_built = models.BooleanField(default=False, null=False, blank=False)
    is_painted = models.BooleanField(default=False, null=False, blank=False)
    faction = models.ForeignKey(Factions, on_delete=models.SET_DEFAULT, default=2, related_name='force_orgs')

    def __str__(self):
        return self.unit_name
