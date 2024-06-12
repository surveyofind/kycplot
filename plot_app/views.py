
import os
from django.shortcuts import render
from .models import *
from .models import Plot_data, State,District
from django.conf import settings
from PIL import Image
from django.http import HttpResponse
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
from django.http import JsonResponse




def display_Images(request):
    # Get the path to qc_plots and qc_Plots_UP directory within MEDIA_ROOT
    qc_plots_path = os.path.join(settings.MEDIA_ROOT, 'qc_plots')
    # qc_plots_up_path = os.path.join(settings.MEDIA_ROOT, 'qc_plots_up')
    try:
        # List site folders in qc_plots directory
        site_folders = os.listdir(qc_plots_path)
        # site_folders_1 = os.listdir(qc_plots_path, "MP")
        # site_folders_2 = os.listdir( qc_plots_up_path, "UP")
        # site_folders_1 = [(folder, "MP") for folder in os.listdir(qc_plots_path)]
        # site_folders_2 = [(folder, "UP") for folder in os.listdir(qc_plots_up_path)]
        # site_folders = site_folders_1 + site_folders_2
        
        for site_code, state in site_folders:
            
            # Construct full path to site folder
            if state == "MP":
                site_folder_path = os.path.join(qc_plots_path, site_code)
            elif state == "UP":
                site_folder_path = os.path.join(qc_plots_path, site_code)

            if os.path.isdir(site_folder_path):
                # List PNG images in the site folder
                png_images = [image for image in os.listdir(site_folder_path) if image.lower().endswith('.png')]
                
                # Check if there are at least 4 PNG images
                if len(png_images) >= 4:
                    # state = "MP" 
                     # Fetch site_name from District model based on site_code
                    district = District.objects.filter(name=site_code).first()
                    site_name = district.site_name if district else ""
                    coordinates = " "

                    # Create Plot_data instance
                    plot_data = Plot_data.objects.create(
                        state=state,
                        site_code=site_code,
                        site_name =site_name,
                        coordinates=coordinates,
                        image_Cycle_Slip_PLOT=os.path.join('qc_plots', site_code, png_images[0]),
                        image_MP_PLOT=os.path.join('qc_plots', site_code, png_images[1]),
                        image_Percentage_Observation=os.path.join('qc_plots', site_code, png_images[2]),
                        image_TS_PLOT=os.path.join('qc_plots', site_code, png_images[3])
                    #     image_Cycle_Slip_PLOT=os.path.join('qc_plots' if state == "MP" else 'qc_plots_up', site_code, png_images[0]),
                    #     image_MP_PLOT=os.path.join('qc_plots' if state == "MP" else 'qc_plots_up', site_code, png_images[1]),
                    #     image_Percentage_Observation=os.path.join('qc_plots' if state == "MP" else 'qc_plots_up', site_code, png_images[2]),
                    #     image_TS_PLOT=os.path.join('qc_plots' if state == "MP" else 'qc_plots_up', site_code, png_images[3])
                    )
                    
                    # Save the instance
                    
                    plot_data.save()
                   
    except FileNotFoundError:
        # Handle the case where qc_plots directory does not exist
        pass
    
    return render(request, 'Display_Images.html')


 
    
def plot_data(request):
    states = State.objects.all()
    data = None
    if request.method == 'POST':
         # Debug statement to print POST data
        state = request.POST.get('state')
        request.session['state'] = state 
        site_name = request.POST.get('site_name').strip()
        request.session['site_name'] = site_name 
        data = Plot_data.objects.filter(site_name=site_name)
        print(data)
        return render(request, 'plot_data.html', {'data':data})
    return render(request, 'plot_data.html', {'states': states})
   


def load_districts(request):
    state_id = request.GET.get('state_id')
    districts = District.objects.filter(state_id=state_id).order_by('site_name')
    return JsonResponse(list(districts.values('id', 'site_name')), safe=False)




def generate_pdf(request):
    state_id = request.session.get('state')
    site_code = request.session.get('site_code')
    site_name = request.session.get('site_name')

    if not site_name or not state_id:
        return HttpResponse("site_name or state not found in session.", status=400)

    state_data = State.objects.filter(id=state_id).values_list('name', flat=True).first()
    if not state_data:
        return HttpResponse("State not found.", status=400)
    
    # Fetch site code and coordinates from SiteData model based on site_name
    site_data = SiteData.objects.filter(site_name=site_name).first()
    if not site_data:
        return HttpResponse("Site data not found.", status=400)
    
    site_code = site_data.site_code
    coordinates = f"Lat: {site_data.coordinates_of_sites_dms_lat}, Long: {site_data.coordinates_of_sites_dms_long}, Height: {site_data.coordinates_of_sites_dms_elp_height}"
    
    
    data = Plot_data.objects.filter(site_name=site_name)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{site_name}_data.pdf"'
    
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    # Add site code, coordinates, state, and site name as text elements
    styles = getSampleStyleSheet()
    site_code_text = f"Site Code: {site_code}"
    state_text = f"State: {state_data}"
    site_text = f"Site Name: {site_name}"
    coordinates_text = f"Coordinates: {coordinates}"
    elements.append(Paragraph(site_code_text, styles['Normal']))
    elements.append(Paragraph(state_text, styles['Normal']))
    elements.append(Paragraph(site_text, styles['Normal']))
    elements.append(Paragraph(coordinates_text, styles['Normal']))
    elements.append(Paragraph("<br/> <br/>", styles['Normal'])) # Add some space after the texts
    
# Add images 
  
    for item in data:
        image_path = item.image_Cycle_Slip_PLOT.path
        image = Image(image_path, width=360, height=260)
        elements.append(image)
        
        image_path = item.image_MP_PLOT.path
        image = Image(image_path, width=360, height=260)
        elements.append(image)
        image_path = item.image_Percentage_Observation.path
        image = Image(image_path, width=360, height=260)
        elements.append(image)
        image_path = item.image_TS_PLOT.path
        image = Image(image_path, width=360, height=260)
        elements.append(image)


    
    doc.build(elements)
    pdf_bytes = buffer.getvalue()
    buffer.close()
    
    response.write(pdf_bytes)
    return response





def delete_all_states(request):
    State.objects.all().delete()
    return HttpResponse("All states have been deleted.")




