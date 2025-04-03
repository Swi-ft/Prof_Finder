from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
import csv
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()
GENAI_API_KEY = os.getenv("GENAI_API_KEY")
genai.configure(api_key=GENAI_API_KEY)

GENAI_API_KEY = "AIzaSyBUFYuzsTJZX2ajL5mF6hGRbtckxn2uo8c"  # Replace with your actual API key
genai.configure(api_key=GENAI_API_KEY)


def home(request):
    professors = []
    all_tags = set()
    file_path = "C:/Users/hello/prof_finder/static/usr/cse_profs.csv"
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Skip header row
        for row in reader:
            professors.append(row)
            tags_column = row[4]
            tags = list(dict.fromkeys(tag.strip() for tag in tags_column.split(',')))
            all_tags.update(tags) 


    file_path = "C:/Users/hello/prof_finder/static/usr/aero_profs.csv"
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Skip header row
        for row in reader:
            professors.append(row)
            tags_column = row[4]
            tags = list(dict.fromkeys(tag.strip() for tag in tags_column.split(',')))
            all_tags.update(tags) 


    file_path = "C:/Users/hello/prof_finder/static/usr/ee_profs.csv"
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Skip header row
        for row in reader:
            professors.append(row)
            tags_column = row[4]
            tags = list(dict.fromkeys(tag.strip() for tag in tags_column.split(',')))
            all_tags.update(tags) 

    file_path = "C:/Users/hello/prof_finder/static/usr/mech_profs.csv"
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Skip header row
        for row in reader:
            professors.append(row)
            tags_column = row[4]
            tags = list(dict.fromkeys(tag.strip() for tag in tags_column.split(',')))
            all_tags.update(tags) 

    file_path = "C:/Users/hello/prof_finder/static/usr/math_profs.csv"
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Skip header row
        for row in reader:
            professors.append(row)
            tags_column = row[4]
            tags = list(dict.fromkeys(tag.strip() for tag in tags_column.split(',')))
            all_tags.update(tags) 
    
    return render(request, 'usr/home.html', {"professors":professors, 'tags':all_tags})
def login(request):
    return render(request, 'usr/login.html')
def signup(request):
    return render(request, 'usr/signup.html')
def mailing(request):
    professors = []
    all_tags = set()
    csv_files = [
        "C:/Users/hello/prof_finder/templates/usr/cse_profs.csv",
        "C:/Users/hello/prof_finder/templates/usr/aero_profs.csv",
        "C:/Users/hello/prof_finder/templates/usr/ee_profs.csv",
        "C:/Users/hello/prof_finder/templates/usr/mech_profs.csv",
        "C:/Users/hello/prof_finder/templates/usr/math_profs.csv"
    ]
    
    for file_path in csv_files:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)  # Skip header row
            for row in reader:
                professors.append(row)
                tags_column = row[4]
                tags = list(dict.fromkeys(tag.strip() for tag in tags_column.split(',')))
                all_tags.update(tags)
    
    return render(request, 'usr/mailing.html', {"professors": professors, 'tags': all_tags})

@csrf_exempt  # Temporary fix, consider using Django's CSRF token properly in production
def generate_mail(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)  # Parse JSON body
        professor_name = data.get("professor")
        tag = data.get("tag")

        # Define the prompt
        prompt = (f"Generate a professional and polite email requesting a research opportunity from Prof. {professor_name}. "
                  f"Express interest in {tag} and inquire about available projects.")

        try:
            model = genai.GenerativeModel("gemini-1.5-flash")  # Use Gemini Pro model
            response = model.generate_content(prompt)
            generated_email = response.text.strip() if response.text else "No response from AI."

            return JsonResponse({"email": generated_email})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)