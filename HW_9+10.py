import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def pause(seconds):
    time.sleep(seconds)

driver=webdriver.Chrome()
def selectors_phonebook_login():
    try:
        driver.get("https://telranedu.web.app/login")
        pause(2)
        print("--------------------")

        head2=driver.find_element(By.TAG_NAME,"head")
        head1=driver.find_element(By.CSS_SELECTOR, "head")
        head3=driver.find_element(By.XPATH,"//head")
        print(head1.tag_name)
        print(head2.tag_name)
        print(head3.tag_name)
        print("--------------------")

        h1=driver.find_element(By.TAG_NAME,"h1")
        h1_1=driver.find_element(By.CSS_SELECTOR,"h1")
        h1_2=driver.find_element(By.XPATH,"//h1[text()='PHONEBOOK']")
        h1_3 = driver.find_element(By.XPATH, "//h1")
        print(h1.tag_name)
        print(h1_1.tag_name)
        print(h1_2.tag_name)
        print(h1_3.tag_name)
        print("--------------------")

        script=driver.find_element(By.TAG_NAME,"script")
        script1 = driver.find_element(By.CSS_SELECTOR, "script")
        script2 = driver.find_element(By.XPATH, "//script")
        print(script.tag_name)
        print(script1.tag_name)
        print(script2.tag_name)
        print("--------------------")

        clas_s=driver.find_element(By.CLASS_NAME,"active")
        clas_s1 = driver.find_element(By.CSS_SELECTOR, ".active")
        print(clas_s.tag_name)
        print(clas_s1.tag_name)
        print("--------------------")

        color=driver.find_element(By.CLASS_NAME,"navbar-component_nav__1X_4m")
        color1 = driver.find_element(By.CSS_SELECTOR, ".navbar-component_nav__1X_4m")
        color2 = driver.find_element(By.XPATH, "//*[@class='navbar-component_nav__1X_4m']")
        color3 = driver.find_element(By.XPATH, "//*[contains(@class,'component')]")
        print(color.tag_name)
        print(color1.tag_name)
        print(color2.tag_name)
        print(color3.tag_name)
        print("--------------------")

        container=driver.find_element(By.CLASS_NAME,"container")
        container1 = driver.find_element(By.CSS_SELECTOR, ".container")
        container2 = driver.find_element(By.XPATH, "//*[@class='container']")

        print(container.tag_name)
        print(container1.tag_name)
        print(container2.tag_name)
        print("--------------------")

        root=driver.find_element(By.ID,"root")
        root1 = driver.find_element(By.CSS_SELECTOR, "#root")
        root2 = driver.find_element(By.XPATH, "//*[@id='root']")
        print(root.tag_name)
        print(root1.tag_name)
        print(root2.tag_name)
        print("--------------------")

    finally:
        driver.quit()
selectors_phonebook_login()
