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

# Simple force org model all fields are required except the codex page
class ForceOrg(models.Model):
    unit_name = models.CharField(max_length=100, null=False, blank=False)
    unit_type = models.CharField(max_length=50, choices=unit_choices, default='Troops', null=False, blank=False)
    codex_page = models.IntegerField()
    points_cost = models.IntegerField(null=False, blank=False)
    is_built = models.BooleanField(default=False, null=False, blank=False)
    is_painted = models.BooleanField(default=False, null=False, blank=False)
    
    def __str__(self):
        return self.unit_name
