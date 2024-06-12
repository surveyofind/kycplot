import csv
from django.core.management.base import BaseCommand
from plot_app.models import State, District

class Command(BaseCommand):
    help = 'Import data from CSV file into State and District models'

    def handle(self, *args, **kwargs):
        # Path to your CSV file
        csv_file_path = 'sorted_by_state2.csv'

        with open(csv_file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                state_name = row['state_name']
                district_name = row['site_code']
                site_name = row['site_name']  # Get site_name from CSV
                # Get or create the state by name
                state, created = State.objects.get_or_create(name=state_name)

                # Create the district with the state reference
                District.objects.get_or_create(name=district_name, state=state, site_name=site_name )

        self.stdout.write(self.style.SUCCESS('Data successfully imported'))
