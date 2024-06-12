from django.core.management.base import BaseCommand
from plot_app.models import State

class Command(BaseCommand):
    help = 'Insert all Indian states into the State model'

    def handle(self, *args, **kwargs):
        indian_states = [
            'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh',
            'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand',
            'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
            'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab',
            'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura',
            'Uttar Pradesh', 'Uttarakhand', 'West Bengal'
        ]

        for state_name in indian_states:
            State.objects.create(name=state_name)

        self.stdout.write(self.style.SUCCESS('All Indian states have been inserted successfully.'))


#         from django.core.management.base import BaseCommand
# from myapp.models import Plot_data

# class Command(BaseCommand):
#     def handle(self, *args, **kwargs):
#         # Assuming you have the site_name value available
#         site_name = "Your Site Name"

#         # Create an instance of Plot_data with the site_name value
#         plot_data_instance = Plot_data(site_name=site_name)

#         # Optionally, you can also set other fields if needed
#         plot_data_instance.state = "Your State"
#         plot_data_instance.site_code = "Your Site Code"
#         plot_data_instance.coordinates = "Your Coordinates"

#         # Save the instance to insert data into the database
#         plot_data_instance.save()

#         self.stdout.write(self.style.SUCCESS('Data successfully inserted into Plot_data table'))

