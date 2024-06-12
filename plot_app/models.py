from django.db import models



class Plot_data(models.Model):
    state = models.CharField(max_length=100, blank=True, null=True)
    site_name = models.TextField(blank=True, null=True)
    site_code = models.TextField(blank=True, null=True)
    image_Cycle_Slip_PLOT = models.ImageField(upload_to='media')
    image_MP_PLOT = models.ImageField(upload_to='media')
    image_Percentage_Observation = models.ImageField(upload_to='media')
    image_TS_PLOT = models.ImageField(upload_to='media')
    coordinates = models.CharField(max_length=100, blank=True, null=True)



class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class District(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    site_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
    
class SiteData(models.Model):
    corsid = models.CharField(max_length=20)
    state = models.CharField(max_length=50)
    site_name = models.CharField(max_length=100)
    site_code = models.CharField(max_length=10)
    coordinates_of_sites_dms_lat = models.CharField(max_length=50)
    coordinates_of_sites_dms_long = models.CharField(max_length=50)
    coordinates_of_sites_dms_elp_height = models.FloatField()

    def __str__(self):
        return self.site_name
    
