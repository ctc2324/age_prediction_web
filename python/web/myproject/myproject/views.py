from django.shortcuts import render
from django.conf import settings
import os
import subprocess

def file_upload(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        file_path = os.path.join('/home/itlab/ctc/python/input', 'input.jpg')
        with open(file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        script_path = '/home/itlab/ctc/python/age_prediction_for_several_1227/age_prediction_for_several_1227.py'
        subprocess.run(['python', script_path], capture_output=True, text=True)
     
        
        # Pass return_code as part of the context dictionary
        return render(request, 'upload_success.html')
        
    return render(request, 'file_upload.html')

def upload_success(request):
   
    
    return render(request, 'upload_success.html',)

