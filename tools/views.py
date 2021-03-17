from django.shortcuts import render

from .forms import PCAFileForm
from .file_processing import process_pca_file


def upload_pca_file_view(request):
    if request.method == 'POST':
        form = PCAFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['pca_file']
            variance = form.cleaned_data.get('no_of_components')
            if str(file).endswith('.csv'):
                corr = process_pca_file(file, variance)
                return render(request, 'pca_analysis.html', {'corr': corr})
            else:
                ind = 'File type is incorrect, must be .CSV'
                return render(request, 'upload_pca_file.html', {'form': form, 'upload_ind': ind})
        else:
            pass
    else:
        form = PCAFileForm()
    return render(request, 'upload_pca_file.html', {'form': form})


def how_to_pca_view(request):
    data = {
        'prices': [['2020-01-31', 100, 150, 60, 170, 301, 122, 24, 83],
                   ['2020-02-01', 110, 163, 67, 171, 250, 123, 25, 74],
                   ['2020-02-02', 108, 156, 65, 172, 240, 122, 24, 72],
                   ['2020-02-03', 109, 145, 64, 176, 245, 130, 25, 73],
                   ['2020-02-04', 112, 149, 66, 177, 251, 126, 25, 77],
                   ['2020-02-05', 113, 148, 67, 176, 252, 129, 25, 70],
                   ['2020-02-06', 111, 152, 69, 178, 249, 135, 25, 75]]
    }
    return render(request, 'how_to_upload_pca_file.html', data)
