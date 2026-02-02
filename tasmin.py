# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 16:41:06 2026

@author: tasmi
"""

import streamlit as st



with open("resume.txt", "r") as g:
    resume = g.readlines()
    
with open("studies.txt", "r") as f:
    studies = f.readlines()   
    
new_job_started = []
new_studies_started = []

#-------------------------------------------------------------
#Employment history 
    
for i, line in enumerate(resume):
    if line == "\n":
        new_job_started.append(i)
new_job_started.append(len(resume))

employment = {}


def get_years(str_line):
    two_years = []
    str_list = str_line.split(" ")
    for s in str_list:
        s = s.strip()
        if s.isdigit() and len(s) == 4:
            two_years.append(int(s))          
    return two_years

def get_tasks(start, end):
    my_tasks = []
    for t in range(start, end):
        clean_task = "•\t" + resume[t].lstrip("•\t")
        my_tasks.append(clean_task)
    return "\n".join(my_tasks)

def extract_job(entry):
    start_end_year = get_years(resume[entry + 4])
    position = resume[entry + 1].strip()
    company = resume[entry + 2].strip()
    location = resume[entry + 3].strip()
    tasks = get_tasks(entry + 5, new_job_started[new_job_started.index(entry)+1])
    job_info = {"Position": position, "Company": company, "Location": location, "Tasks": tasks}

    for y in range(start_end_year[0],start_end_year[1] + 1):
        employment[y]=job_info
    return employment 
    
    
for entry in new_job_started[:-1]:
    extract_job(entry)

def visualise(year, job):
    #position = job["Position"]
    st.write(f"In the year {year}, Tasmin worked as a {job["Position"]}, at {job["Company"]}, in {job["Location"]}. ")
    st.markdown(f'During her time as a {job["Position"]}, she: <br><br> {job["Tasks"]}', unsafe_allow_html=True) 
    #{job["Tasks"]}
    #st.write(employment[employment_year])

#-------------------------------------------------------------
#Study history 

studying = {}
   
for j, lline in enumerate(studies):
    if lline == "\n":
        new_studies_started.append(j)
new_studies_started.append(len(studies))

studying = {}  #instead of employment


#def get_years(str_line):
#    two_years = []
#    str_list = str_line.split(" ")
#    for s in str_list:
#        s = s.strip()
#        if s.isdigit() and len(s) == 4:
#            two_years.append(int(s))          
#    return two_years

def get_study_tasks(start, end):
    my_tasks = []
    for t in range(start, end):
        clean_task = "•\t" + studies[t].lstrip("•\t")
        my_tasks.append(clean_task)
    return "\n".join(my_tasks)

def extract_studies(entry):
    start_end_year = get_years(studies[entry + 4])
    position = studies[entry + 1].strip()
    institution = studies[entry + 2].strip()
    location = studies[entry + 3].strip()
    tasks = get_study_tasks(entry + 5, new_studies_started[new_studies_started.index(entry)+1])
    study_info = {"Position": position, "Institution": institution, "Location": location, "Tasks": tasks}
    for y in range(start_end_year[0],start_end_year[1] + 1):
        studying[y]=study_info
    return studying 
    
    
for entry in new_studies_started[:-1]:
    extract_studies(entry)
    
def visualise_study(year, student_info):
    st.write(f"In the year {year}, Tasmin was {student_info["Position"]}, at {student_info["Institution"]}, in {student_info["Location"]}. ")
    st.markdown(f'During her time as {student_info["Position"]}, she: <br><br> {student_info["Tasks"]}', unsafe_allow_html=True) 



#----------------------------------------------------------------


# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "Employment History", "Study Histroy", "Contact"],
)

if menu == "Researcher Profile":
    st.title("Researcher Profile")

    # Collect basic information
    name = "Tasmin van den Heever"
    field = "Physics"
    institution = "University of the Western Cape"

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")


elif menu == "Employment History":
    st.title("Employment History")
    employment_year = st.slider("Choose a year of employment history", 1988, 2027)
    st.write(f"You picked: {employment_year}")
    if employment_year in employment:
        visualise(employment_year, employment[employment_year])
    else:
        st.write(f"There is a gap in Tasmin's resume for the year {employment_year}. You could check her Study Histroy for clues as to why.")
        
elif menu == "Study Histroy":
    st.title("Study Histroy")
    study_year = st.slider("Choose a year of study history", 1988, 2027)
    st.write(f"You picked: {study_year}")
    if study_year in studying:
        visualise_study(study_year, studying[study_year])
    else:
        st.write(f"There is a gap in Tasmin's study histroy for the year {study_year}. You could check her Employment Histroy for clues as to why.")
    
elif menu == "Contact":
    # Add a contact section
    st.header("Contact Information")
    email = "tasmin.vdh@outlook.com"
    st.write(f"You can reach me at {email}.")







