from django.core.exceptions import ValidationError
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Candidate
from .utils import extract_information_from_file  # Assuming this function exists
from datetime import datetime

def upload_form(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']

        # Save the file to a temporary directory
        fs = FileSystemStorage(location='uploaded_files/')
        file_path = fs.save(uploaded_file.name, uploaded_file)
        file_path = fs.path(file_path)

        try:
            # Extract data
            extracted_data = extract_information_from_file(file_path)

            if extracted_data and 'candidate_info' in extracted_data:
                candidate_info = extracted_data['candidate_info']

                # Validate required fields
                required_fields = ['first_name', 'last_name', 'mobile']
                missing_fields = [field for field in required_fields if not candidate_info.get(field)]

                if missing_fields:
                    return render(request, 'upload.html', {
                        'message': f"Missing required fields: {', '.join(missing_fields)}",
                        'extracted_data': candidate_info
                    })

                # Save to database (only if all required fields are present)
                candidate = Candidate(
                    first_name=candidate_info.get('first_name'),
                    middle_name=candidate_info.get('middle_name', ''),
                    last_name=candidate_info.get('last_name'),
                    email=candidate_info.get('email', ''),
                    mobile=candidate_info.get('mobile'),
                    pan_no=candidate_info.get('pan_no', ''),
                    passport=candidate_info.get('passport', ''),
                    permanent_address=candidate_info.get('permanent_address', '')
                )
                candidate.save()

                return redirect('candidate_list')  # Redirect to the candidate list page after saving data
            else:
                message = "Failed to extract candidate information. Please check the file format and content."
                return render(request, 'upload.html', {'message': message})

        except Exception as e:
            # Handle any unexpected errors
            return render(request, 'upload.html', {
                'message': f"An error occurred while processing the file: {str(e)}"
            })

    return render(request, 'upload.html')

def candidate_list(request):
    candidates = Candidate.objects.all()
    return render(request, 'candidate_list.html', {
        'candidates': candidates,
        'current_year': datetime.now().year
    })

def delete_candidate(request, candidate_id):
    Candidate.objects.filter(id=candidate_id).delete()
    return redirect('candidate_list')  # Redirect to the candidates list

def delete_all_candidates(request):
    Candidate.objects.all().delete()
    return redirect('candidate_list')  # Redirect to the candidates list
