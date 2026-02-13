from django.shortcuts import render

def gst_amt_calculator(request):
    gst_amt = None
    if request.method == 'POST':
        try:
            price = float(request.POST.get('price'))
            gst = float(request.POST.get('gst'))
           

            if price >= 0 and gst >= 0:
                gst_amt = price + ((price * gst) / 100)
            else:
                # Handle potential negative inputs error
                gst_amt = "Error: Inputs cannot be negative."
        except ValueError:
            # Handle potential non-numeric inputs error
            gst_amt = "Error: Invalid input. Please enter numeric values."

    # Pass the result to the template
    context = {
        'gst_amt': gst_amt
    }
    return render(request, 'calculator.html', context)