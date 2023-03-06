
# Created by Noah Syler

from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from datetime import datetime
from time import sleep
import re
import sys
import copy

d = DesiredCapabilities.EDGE
d['ms:loggingPrefs'] = { 'browser':'ALL' }

options = webdriver.EdgeOptions()
#options.headless = True
options.add_argument('--headless')
driver = webdriver.Edge(options = options)
edge_options = EdgeOptions()
edge_options.use_chromium = True
edge_options.binary_location = R"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
edge_options.set_capability("ms:edgeOptions",d)

driver = webdriver.Edge(capabilities=d)

urls = []

#Navigate to the page with the desired resources
driver.get("<website with news links>")

#Unprocessed links holds all of the elements with the specified class name on the page
unprocessed_links = driver.find_elements(By.CLASS_NAME, "<unique class name to the desired links>")

#Appending all the urls to a list
for link in unprocessed_links:
	urls.append(link.get_attribute("href"))

#Open a new  and switch to a new window process the URLs
driver.execute_script(f"window.open('');")
driver.switch_to.window(driver.window_handles[1])

for url in urls:

	
	try:
		#List to store tables. It is unkown if any page has more than 2, someof them have 0 though.
		tables = []
		#String to store paragraph values
		inner = ''


		driver.get(url)	

		release_body = driver.find_element(By.XPATH, '<xpath to main body>')
		content = release_body.find_element(By.XPATH, "<xpath to the content>")
		title_element = driver.find_element(By.CLASS_NAME, "<unique class name to title element>")
		title_element = title_element.find_element(By.TAG_NAME, 'h1')
		title = title_element.get_attribute("innerHTML")

		#Formatting the title elemement to title case
		title = title.title()

		date_element = driver.find_element(By.XPATH, '<xpath to the date element>')
		date = date_element.get_attribute("innerHTML") 

		#Grab the paragraph elements. The tables and content need to be uploaded into different fields.
		paragraph_elements = release_body.find_elements(By.TAG_NAME, 'p')

		#This prevents 'p' elements in the tables from being included into the content
		for element in paragraph_elements:
			if '<common beginning text heading the tables>' in element.get_attribute('innerHTML'):
				break
			#Converting the content to one string	
			inner = inner + element.get_attribute("outerHTML")

		#Removing the old CSS classes from the original submissions
		inner_scrubbed = re.sub('class="([^"]*)"', '', inner)
		print(inner_scrubbed)

		#Try except block filters out the articles without tables
		try:
			table_elements = release_body.find_elements(By.TAG_NAME, 'table')
			for table in table_elements:
				table_txt = table.get_attribute("outerHTML")
				table_scrubbed = re.sub('class="([^"]*)"', '', table_txt)
				tables.append(table_scrubbed)
		except Exception as ex:
			print(f'failed to obtain a table. Error: \n{ex}')

		
		date_found = driver.find_element(By.CLASS_NAME, '<unique class name for the date elements>').get_attribute('innerHTML')
		
		#Formatting the date to be used on the new site
		date_found = date_found[:-3]
		hour = date_found[-5:-3]
		minute = date_found[-2:]
		hour = int(hour)
		if hour >= 12:
			time = f"{hour-12}:{minute} PM"
		elif hour == 0:
			time = f"{12}:{minute} AM"
		else:
			time = f"{hour}:{minute} AM"	
			
		date_found = f"{date_found[:-5]}{time}"

		day = datetime.strptime(date_found, "%b %d, %Y, %I:%M %p")
		day = day.strftime("%m/%d/%Y %I:%M %p")

		driver.execute_script(f"window.open('');")
		driver.switch_to.window(driver.window_handles[1])
		driver.get("<website login page>") # ExpressionEngine login page

		user_name = driver.find_element(By.NAME, "username")
		password = driver.find_element(By.NAME, "password")
		sign_in = driver.find_element(By.NAME, "submit")

		user_name.send_keys("<username>")
		password.send_keys("<password>")
		sign_in.click()

		#Redirect to the article submission page
		driver.get('<Article submission page URL>')
		add_html_text_button = driver.find_element(By.XPATH, '<xpath to "Add HTML" button>')
		add_html_text_button.click()


		html_txt_field = driver.find_element(By.XPATH, '<xpath to the html text entry field>')
		html_txt_field.send_keys(inner_scrubbed)

		#If the tables list is not empty, the tables will be uploaded.
		if tables:
			#The first index is at a div[2], and increments by one thereafter
			txt_index = 2
			for table in tables:
				
				add_html_text_button = driver.find_element(By.XPATH, '<xpath to the html text button>')
				add_html_text_button.click()
				
				print(f'txt_index: {txt_index}')		 
				html_txt_field = driver.find_element(By.XPATH, f'<xpath to the html text field, the div location has {txt_index} inserted>')
				html_txt_field.send_keys(table)
				txt_index += 1
		

		title_element = driver.find_element(By.XPATH, '<title element xpath>')
		title_element.send_keys(title)

		#Enter the back dated date
		date_button = driver.find_element(By.XPATH, '<date button to switch to the date entry view.>')
		date_button.click()										

		date_entry = driver.find_element(By.XPATH, '<date entry xpath>')
		date_entry.clear()							
		date_entry.send_keys(day)
		
		print(f'Date: {day}')
		print(f'Title: {title}')
		print(f'URL: {url}')


		save_button = driver.find_element(By.XPATH, '<save button xpath>')
		save_button.click()	
		print(f"title: completed")
		print("="*20)
		print(f"PROGRESS: {int((urls.index(url)+1)/len(urls)*100)}")
		print(f"Index: {urls.index(url)}")

	#Save the urls that did not upload. This is most commonly due to articles sharing the same title as another
	except Exception as ex:
		with open ('failed_urls.txt', 'a', encoding='utf8') as f:
			f.write(f'{url}\n')
			f.write(f'{ex}\n')
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.close()