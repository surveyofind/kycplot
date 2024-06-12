# myapp/management/commands/import_csv.py
import csv
from django.core.management.base import BaseCommand
from plot_app.models import SiteData

class Command(BaseCommand):
    help = 'Import CSV data into the SiteData model'

    def handle(self, *args, **kwargs):
      
        csv_file_path = 'CORS_CODE_COORDINATES4.csv'

        with open(csv_file_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                 SiteData.objects.create(
                    corsid=row['corsid'],
                    state=row['state'],
                    site_name=row['site_name'],
                    site_code=row['site_code'],
                    coordinates_of_sites_dms_lat=row['coordinates_of_sites_dms_lat'],
                    coordinates_of_sites_dms_long=row['coordinates_of_sites_dms_long'],
                    coordinates_of_sites_dms_elp_height=row['coordinates_of_sites_dms_elp_height'],
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported data'))
