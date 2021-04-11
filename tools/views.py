from django.shortcuts import render

from .forms import CorrFileForm
from .file_processing import process_corr_file


def upload_corr_file_view(request):
    if request.method == 'POST':
        form = CorrFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['corr_file']
            if str(file).endswith('.csv'):
                stocks, corr = process_corr_file(request.FILES['corr_file'])
                return render(request, 'corr_analysis.html', {'stocks': stocks, 'corr': corr})
            else:
                ind = 'File type is incorrect, must be .CSV'
                return render(request, 'upload_corr_file.html', {'form': form, 'upload_ind': ind})
        else:
            pass
    else:
        form = CorrFileForm()
    return render(request, 'upload_corr_file.html', {'form': form})


def how_to_corr_view(request):
    data = {
        'prices': [['2020-01-31', 100, 150, 60, 170, 301, 122, 24, 83],
                   ['2020-02-01', 110, 163, 67, 171, 250, 123, 25, 74],
                   ['2020-02-02', 108, 156, 65, 172, 240, 122, 24, 72],
                   ['2020-02-03', 109, 145, 64, 176, 245, 130, 25, 73],
                   ['2020-02-04', 112, 149, 66, 177, 251, 126, 25, 77],
                   ['2020-02-05', 113, 148, 67, 176, 252, 129, 25, 70],
                   ['2020-02-06', 111, 152, 69, 178, 249, 135, 25, 75]]
    }
    return render(request, 'how_to_upload_corr_file.html', data)


def how_to_save_csv_view(request):
    data = {
        'prices': [['2020-01-31', 100, 150, 60, 170, 301, 122, 24, 83],
                   ['2020-02-01', 110, 163, 67, 171, 250, 123, 25, 74],
                   ['2020-02-02', 108, 156, 65, 172, 240, 122, 24, 72],
                   ['2020-02-03', 109, 145, 64, 176, 245, 130, 25, 73],
                   ['2020-02-04', 112, 149, 66, 177, 251, 126, 25, 77],
                   ['2020-02-05', 113, 148, 67, 176, 252, 129, 25, 70],
                   ['2020-02-06', 111, 152, 69, 178, 249, 135, 25, 75]]
    }
    return render(request, 'how_to_save_as_csv.html', data)
