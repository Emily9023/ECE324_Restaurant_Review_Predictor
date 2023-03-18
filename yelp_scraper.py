# I pip installed selenium and webdriver_manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# set up initial google search to the yelp site
s = Service('C:\\Users\\anika\\Documents\\ECE324_Restaurant_Review_Predictor\\chromedriver.exe')
wd = webdriver.Chrome(service=s)
wd.maximize_window()
wd.implicitly_wait(50)
start_url = 'https://www.yelp.ca/search?find_desc=Restaurants&find_loc=Toronto%2C+ON'
wd.get(start_url)
wait = WebDriverWait(wd, 20)

d = {}
i = 3
total_entries = 3
while i < 20 and len(d) < total_entries:
    # each run of the while loop is one page on yelp
    rest_element = None
    try:
        rest_element = wd.find_elements(By.XPATH, "//*[@id='main-content']/div/ul/li[{}]/div[1]".format(i))
    except:
        print("could not find restaurant element")
        if i > 9:
            wd.quit()
    if rest_element:
        restaurant = rest_element[0].text.split('\n')
        if restaurant[0] != 'Sponsored Results' and restaurant[0] != 'Sponsored Result' and restaurant[0] != "All \"restaurants\" results in Toronto, Ontario" and len(restaurant[0]) > 2:
            aria_label, stars = None, None
            try:
                stars = wd.find_element(By.XPATH, "//*[@id='main-content']/div/ul/li[{}]/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[1]".format(i))
                print("stars text:", stars[0].text)
            except:
                print("This entry does not have a star rating")
            if stars:
                try:
                    if i == 8:
                        n = 1
                    else:
                        n = 2
                    aria_label = stars.find_element(By.CSS_SELECTOR, "#main-content > div > ul > li:nth-child({}) > div.container__09f24__mpR8_.hoverable__09f24__wQ_on.border-color--default__09f24__NPAKY > div > div > div.arrange-unit__09f24__rqHTg.arrange-unit-fill__09f24__CUubG.border-color--default__09f24__NPAKY > div:nth-child(1) > div:nth-child(1) > div:nth-child({}) > div > div > div > div.display--inline-block__09f24__fEDiJ.margin-r1__09f24__rN_ga.border-color--default__09f24__NPAKY > span > div".format(i, n)).get_attribute("aria-label")
                except:
                    print("did not get aria_label")
                    if i > 9:
                        wd.quit()
                if aria_label:
                    print("aria_label is:", aria_label)
                    restaurant.append(aria_label)
                    d[restaurant[0]] = restaurant[2:]
                    print("Added:", restaurant[0])
    rest_element = None
    if i == 19:
        # go to next page
        WebDriverWait(wd, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/div/ul/li[21]/div/div[1]/div/div[11]/span/a"))).click()
        i = 3
    i += 1


wd.quit()

js = json.dumps(d)
# Open new json file if not exist it will create
fp = open('data.json', 'a')
# write to json file
fp.write(js)
# close the connection
fp.close()
