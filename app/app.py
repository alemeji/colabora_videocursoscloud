from selenium import webdriver
from datetime import date
import time

def process():
	browser = webdriver.Firefox()
	browser.get('https://www.humblebundle.com/')
	button = browser.find_element_by_xpath("//a[@class='navbar-item not-dropdown button-title']")
	button.click()
	time.sleep(3)
	
	try:
		hrefs = browser.find_elements_by_xpath("//a[@class='full-tile-view one-third bundle']")
		packs = []
		# if hrefs:
		# 	print("Found ", len(hrefs))
		for href in hrefs:
			link = transform_href(href)
			title = extract_title(href)
			days = extract_days_left(href)
			if title:
				packs.append({'title': title, 'link':link, "days": days})

		if packs:
			# print(packs)
			with open('colabora.md','w') as new_file:
				new_file.write("# Packs de libros en humble bundle\n\n")
				today = date.today()
				updated = "Actualizado: %s\n\n" % today.strftime("%B %d, %Y")
				new_file.write(updated)
				# sorted(lis, key = lambda i: i['age'])
				for pack in sorted(packs, key = lambda i: i['days']):
					days_left = "Es hoy, apurate!" if pack['days'] == 0 else "Dias faltantes:" + str(pack['days'])
					name_pack = "[%s - %s](%s)\n\n" % (pack['title'],days_left, pack['link'])
					new_file.write(name_pack)

	except Exception as e:
		print(str(e))
	finally:
		browser.quit()

def transform_href(href, partner_charity = 'partner=videocursoscloud&charity=3843'):
	link = href.get_attribute('href').split('?')
	if link[0]:
		return link[0] + "?" + partner_charity
	return href

def extract_title(href):
	result = None
	title = href.find_element_by_xpath(".//div[@class='tile-info bundle']/div[@class='info-section']/span")
	if title:
		result = title.text
	return result

def extract_days_left(href):
	result = None
	days = href.find_element_by_css_selector("span.js-days")
	if days:
		num = days.text.split(' ')[0]
		result = 0 if len(num) == 0 else int(num)
	return result

if __name__=="__main__":
	process()
