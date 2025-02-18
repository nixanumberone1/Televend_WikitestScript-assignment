from selenium import webdriver                                   #import of selenium webdriver lib
from selenium.webdriver.common.by import By                      #For location webpage elements
from selenium.webdriver.common.keys import Keys                  #For inlcuding special keys presses
from selenium.webdriver.chrome.options import Options            #Used to setup Chrome Webdriver with different options
from selenium.webdriver.support.ui import WebDriverWait          #Used in waiting for a elements conditions to become true before continuing the test
from selenium.webdriver.support import expected_conditions as EC #provides common conditions
import logging                                                   #Used for logging errors and console messages
from datetime import datetime                                    #capturing currenttime for test report start and end

# flag condition for headed/headless mode
headless_mode = True

# Initialize the chrome WebDriver with some options
chrome_options = Options()
if headless_mode:
    chrome_options.add_argument("--headless")  # Only added as option if the flag is set to True
driver = webdriver.Chrome(options=chrome_options)

# Setup for logging and displaying info messages
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


#Creates a report based on assigment requirments
def generate_report(test_method, start_time, end_time, browser_type, duration):
    
    report_content = f"""
    TestMethod: {test_method}
    Duration: {duration}
    Started: {start_time.strftime('%Y-%m-%d %H:%M:%S')}           
    Ended: {end_time.strftime('%Y-%m-%d %H:%M:%S')}
    Browsers: {browser_type}
    """

    # Saving report to a file with write along with seperator lines
    with open("test_report.txt", "a") as report_file:
        report_file.write(report_content)
        report_file.write("\n" + "-"*50 + "\n")

#Go to wikipedia landing page and log action
def open_wikipedia():
    driver.get("https://hr.wikipedia.org/")
    logger.info("Opened Wikipedia homepage.")

#Click on search input and search article name and confirm
def search_for_article(article_name):
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys(article_name)
    search_box.send_keys(Keys.RETURN)
    logger.info(f"Searched for article: {article_name}")

#Locate history tab and click on it
def go_to_history_tab():
    history_tab = driver.find_element(By.LINK_TEXT, "Vidi povijest")
    history_tab.click()
    logger.info("Clicked on the 'Vidi povijest' tab.")

#Find filtering option and click on it
def open_filter_options():
    filter_button = driver.find_element(By.CSS_SELECTOR, "legend.oo-ui-fieldsetLayout-header.mw-collapsible-toggle")
    filter_button.click()
    logger.info("Opened 'Filtriranje inacica'.")

#Go trough year,month,date selectors, select all and confirm choice
def set_date_range():
    date_picker = driver.find_element(By.CSS_SELECTOR, "#mw-input-date-range-to")
    date_picker.click()

    button=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.mw-widget-calendarWidget-labelButton .oo-ui-labelElement-label")))
    button.click()
    button.click()
    
    year_2020 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='mw-widget-calendarWidget-item mw-widget-calendarWidget-year' and text()='2020']")))
    year_2020.click()

    month_srp = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='mw-widget-calendarWidget-item mw-widget-calendarWidget-month' and text()='srpanj']")))
    month_srp.click()

    day_1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='mw-widget-calendarWidget-item mw-widget-calendarWidget-day' and text()='1']")))
    day_1.click()
    
    logger.info("Set the date range to 1st July 2020.")

#Click on 'Prikazi inacice' button
def apply_filters():
    apply_button = driver.find_element(By.ID, "ooui-php-9")
    apply_button.click()
    logger.info("Applied filters.")

#Validate timestamp on first item shown on the filtered list and if validated, exit the test script
def validate_timestamp():
    try:
        timestamp_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//a[@class='mw-changeslist-date'])[1]")))
        assert "21:33, 24. travnja 2020." in timestamp_element.text, "Timestamp does not match expected"
        logger.info("Timestamp is equal to 21:33, 24. travnja 2020 and is correct and visible.")
    except Exception as e:
        logger.error(f"Error: {e}")
        driver.quit()

# main part of the script, calls in functions defined in a script for execution
def main():
    test_method = "Selenium_Python test script "  # Name of the test method 
    browser_type = "Chrome / Headless" if headless_mode else "Chrome"  # Dynamic browser type report change
    start_time = datetime.now()  # Capture start time of test script

    open_wikipedia()
    search_for_article("Juraj Dobrila")
    go_to_history_tab()
    open_filter_options()
    set_date_range()
    apply_filters()
    validate_timestamp()

    # End time
    end_time = datetime.now()
    
    # Calculate the duration form start to end time
    duration = end_time - start_time
    duration_str = str(duration).split(".")[0]  # Format as hh:mm:ss (ignoring milliseconds)

    # Generate the report with test details
    generate_report(test_method, start_time, end_time, browser_type, duration_str)

    #Log a sucess msg if test passes and exit the browser
    logger.info("Test passed successfully.")
    driver.quit()

#ensures that main() block is called when this script is run directly and not imported as a module
if __name__ == "__main__":
    main()
