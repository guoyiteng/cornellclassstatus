from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def login(browser, username, password):
    url = "https://studentcenter.cornell.edu/"
    browser.get(url)
    browser.implicitly_wait(10)
    netid = browser.find_element_by_id('netid')
    netid.clear()
    netid.send_keys(username)
    pwd = browser.find_element_by_id('password')
    pwd.clear()
    pwd.send_keys(password)
    loginButton = browser.find_element_by_name('Submit')
    loginButton.click()
    browser.implicitly_wait(10)

def selectUntilPresence(wait, id):
    return wait.until(EC.presence_of_element_located((By.ID, id)))

def searchCourse(browser, subject, number, gap = 60*15):
    wait = WebDriverWait(browser, 5)
    selectUntilPresence(wait, 'ptifrmtgtframe')
    browser.switch_to_frame('ptifrmtgtframe')
    searchButton = selectUntilPresence(wait, "DERIVED_SSS_SCL_SSS_GO_4$83$")
    searchButton.click()
    subjectSelector = Select(selectUntilPresence(wait, "SSR_CLSRCH_WRK_SUBJECT_SRCH$0"))
    subjectSelector.select_by_value(subject)
    courseNum = selectUntilPresence(wait, "SSR_CLSRCH_WRK_CATALOG_NBR$1")
    courseNum.clear()
    courseNum.send_keys(number)
    showClickBox = selectUntilPresence(wait, "SSR_CLSRCH_WRK_SSR_OPEN_ONLY$3")
    if showClickBox.is_selected():
        showClickBox.click()
    searchButton = selectUntilPresence(wait, "CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH")
    searchButton.click()

    courseButton = selectUntilPresence(wait, "MTG_CLASSNAME$0")
    courseButton.click()

    while True:
        enrollment = selectUntilPresence(wait, "SSR_CLS_DTL_WRK_ENRL_TOT")
        enrollmentCap = browser.find_element_by_id("win0divSSR_CLS_DTL_WRK_ENRL_CAP")
        print(enrollment.text, "/", enrollmentCap.text)
        if int(enrollment.text) < int(enrollmentCap.text):
            break
        time.sleep(gap)

        viewSearchResults = browser.find_element_by_id("CLASS_SRCH_WRK2_SSR_PB_BACK")
        viewSearchResults.click()
        courseButton = selectUntilPresence(wait, "MTG_CLASSNAME$0")
        courseButton.click()

def enroll(browser):
    wait = WebDriverWait(browser, 5)
    enrollButton = wait.until(EC.presence_of_element_located((By.XPATH, "//tbody/tr[@role='tablist']/td[3]/a")))
    enrollButton.click()
    wait.until(EC.presence_of_element_located)

    proceedButton = selectUntilPresence(wait, "DERIVED_REGFRM1_LINK_ADD_ENRL$82$")
    proceedButton.click()

    finishButton = selectUntilPresence(wait, "DERIVED_REGFRM1_SSR_PB_SUBMIT")
    finishButton.click()

    message = wait.until(EC.presence_of_element_located((By.XPATH, "//tr[@id='trSSR_SS_ERD_ER$0_row2']/td[2]/div/div")))
    print(message.text)


def main():
    browser = webdriver.PhantomJS()
    login(browser, 'username', 'password')
    print("Successfully Login.")
    if len(sys.argv) == 2:
        searchCourse(browser, "MATH", "4710", gap = int(sys.argv[1]))
    else:
        searchCourse(browser, "MATH", "4710")
    enroll(browser)
    print("Finish enrolling")

if __name__ == '__main__':
    main()
