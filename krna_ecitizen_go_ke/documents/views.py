from django.shortcuts import render, redirect
import os

def verify_document(request, application_id, output_id):
    """
    Displays the PDF as a series of images embedded in HTML.
    """
    # Get all images for the PDF
    pdf_images_dir = "documents/static/pdfs/pages"
    image_files = sorted(os.listdir(pdf_images_dir))
    image_urls = [f"/static/pdfs/pages/{img}" for img in image_files]

    return render(request, "verify_document.html", {
        "images": image_urls,
        "application_id": application_id,
        "output_id": output_id,
    })

def root_redirect(request):
    """
    Redirect anyone visiting the root URL to eliud.dev.netlify.app
    """
    return redirect("https://knra.co.ke")