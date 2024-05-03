'''from bs4 import BeautifulSoup
import requests
import time

html_text = requests.get('https://www.linkedin.com/jobs/search?keywords=Data%20Scientist&location=Worldwide&geoId=92000000&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0').text

soup = BeautifulSoup(html_text, 'lxml')

def find_jobs():
    
    jobs = soup.find_all('div',class_="base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card")
    with open(f'desktop/statsnew.csv','a') as f:
        for index,job in enumerate(jobs):   

            list_date_elem = job.find('time',class_="job-search-card__listdate")
            list_date = list_date_elem.text.strip()

            company_name_elem = job.find('h4',class_="base-search-card__subtitle")
            company_name = company_name_elem.text.strip()
    

            location_elem = job.find('span',class_="job-search-card__location")
            location = location_elem.text.strip()
    

            title_elem = job.find('h3',class_="base-search-card__title")
            title = title_elem.text.strip()

            
            f.write(f'Job Title: {title}')
            f.write(f'Company Name: {company_name}')
            f.write(f'List Date: {list_date}')
            f.write(f'Location: {location}')
            print(f'File Saved:{index}')  
            nplink = job.find('a',class_="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]").get("href")
            np(nplink,f)
def np(link,f):
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'lxml')
    eptype= soup.find_all('span',class_="description__job-criteria-text description__job-criteria-text--criteria")
    for i in eptype:
        print(eptype.index(i))
    f.write(f'Seniority Level:{eptype[0]}')
    f.write(f'Employment Type:{eptype[1]}')
    f.write(f'Job Function:{eptype[2]}')
    f.write(f'Industries:{eptype[3]}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait=10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait* 60)
'''
'''
from bs4 import BeautifulSoup
import requests
import time

def find_jobs():
    html_text = requests.get('https://www.linkedin.com/jobs/search?keywords=Data%20Scientist&location=Worldwide&geoId=92000000&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0').text
    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('div', class_="base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card")
    with open('desktop/statsnew.csv', 'a', encoding='utf-8') as f:  # Added encoding='utf-8'
        for index, job in enumerate(jobs):
            try:
                list_date_elem = job.find('time', class_="job-search-card__listdate")
                list_date = list_date_elem.text.strip() if list_date_elem else 'N/A'

                company_name_elem = job.find('h4', class_="base-search-card__subtitle")
                company_name = company_name_elem.text.strip() if company_name_elem else 'N/A'

                location_elem = job.find('span', class_="job-search-card__location")
                location = location_elem.text.strip() if location_elem else 'N/A'

                title_elem = job.find('h3', class_="base-search-card__title")
                title = title_elem.text.strip() if title_elem else 'N/A'

                f.write(f'Job_Title: {title}\n')
                f.write(f'Company_Name: {company_name}\n')
                f.write(f'List_Date: {list_date}\n')
                f.write(f'Location: {location}\n')
                print(f'File_Saved: {index}')
                nplink = job.find('a', class_="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]").get("href")
                np(nplink, f)
            except Exception as e:
                print(f"Error processing job entry {index}: {e}")

def np(link, f):
    try:
        html_text = requests.get(link).text
        soup = BeautifulSoup(html_text, 'lxml')
        eptype = soup.find_all('span', class_="description__job-criteria-text description__job-criteria-text--criteria")
        
        if eptype:  # Check if the list is non-empty
            for i in eptype:
                print(eptype.index(i))
            f.write(f'Seniority Level: {eptype[0].text.strip()}\n')
            f.write(f'Employment Type: {eptype[1].text.strip()}\n')
            f.write(f'Job Function: {eptype[2].text.strip()}\n')
            f.write(f'Industries: {eptype[3].text.strip()}\n')
    except Exception as e:
        print(f"Error processing job details: {e}")

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
'''
import csv
from bs4 import BeautifulSoup
import requests
import time

def find_jobs():
    html_text = requests.get('https://www.linkedin.com/jobs/search/?currentJobId=3787668311&distance=25&geoId=92000000&keywords=Python%20Developer&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true').text
    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('div', class_="base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card")
    with open('desktop/statsnne.csv', 'a', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['Job_Title', 'Company_Name', 'List_Date', 'Location', 'Seniority_Level', 'Employment_Type', 'Job_Function', 'Industries']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # If the file is empty, write the header
        if csvfile.tell() == 0:
            writer.writeheader()
       
        for index, job in enumerate(jobs):
            try:
                list_date_elem = job.find('time', class_="job-search-card__listdate")
                list_date = list_date_elem.text.strip() if list_date_elem else 'N/A'

                company_name_elem = job.find('h4', class_="base-search-card__subtitle")
                company_name = company_name_elem.text.strip() if company_name_elem else 'N/A'

                location_elem = job.find('span', class_="job-search-card__location")
                location = location_elem.text.strip() if location_elem else 'N/A'

                title_elem = job.find('h3', class_="base-search-card__title")
                title = title_elem.text.strip() if title_elem else 'N/A'

                nplink = job.find('a', class_="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]").get("href")
                seniority_level, employment_type, job_function, industries = np(nplink)

                writer.writerow({
                    'Job_Title': title,
                    'Company_Name': company_name,
                    'List_Date': list_date,
                    'Location': location,
                    'Seniority_Level': seniority_level,
                    'Employment_Type': employment_type,
                    'Job_Function': job_function,
                    'Industries': industries
                })

                print(f'File_Saved: {index}')

            except Exception as e:
                print(f"Error processing job entry {index}: {e}")

def np(link):
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'lxml')
    eptype = soup.find_all('span', class_="description__job-criteria-text description__job-criteria-text--criteria")

    seniority_level = eptype[0].text.strip() if eptype and len(eptype) > 0 else 'N/A'
    employment_type = eptype[1].text.strip() if eptype and len(eptype) > 1 else 'N/A'
    job_function = eptype[2].text.strip() if eptype and len(eptype) > 2 else 'N/A'
    industries = eptype[3].text.strip() if eptype and len(eptype) > 3 else 'N/A'

    return seniority_level, employment_type, job_function, industries

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait )
