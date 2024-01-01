from django.shortcuts import render
from django.conf import settings
import os
import subprocess


def file_upload(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        file_path = os.path.join('/home/itlab/ctc/python/input', 'input.jpg')
        with open(file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        script_path = '/home/itlab/ctc/python/age_prediction_for_several_1227/age_prediction_for_several_1227.py'
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
     
        output = result.stdout
        return_code = result.returncode
        
        if return_code == 0:
            return render(request, 'upload_success.html')
        else:

            return render(request, 'error_page.html')
        
    return render(request, 'file_upload.html')

def upload_success(request):
   
    image_path = '/static/output.png'

    return render(request, 'upload_success.html', {'image_path': image_path})
