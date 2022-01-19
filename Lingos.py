from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from alive_progress import alive_bar
from selenium import webdriver
from selenium.webdriver.common.by import By
from firebase_admin import firestore
from firebase_admin import credentials
from cmath import log
from socket import dup
import subprocess
import sys
from time import sleep
#funckja do instalcji modulow potrzebnych do uruchomienia aplikajcji


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip",
                          "-q", "-q", "install", package])


#sprawdzamy czy moduly zostaly wczesniej zainstalowane
try:
    from selenium import webdriver
    from alive_progress import alive_bar
    import firebase_admin

    from webdriver_manager.chrome import ChromeDriverManager
    print("all modules are installed")

#jezeli nie to instaujem je za pomoca funckji install
except ModuleNotFoundError:

    print("Installating modules")
    #instalowanie pakietow
    install("selenium")
    install("firebase-admin")
    install("alive-progress")
    install("webdriver-manager")

#import potrzebnych bibliotek

credential = credentials.Certificate({
    "type": "service_account",
    "project_id": "lingos-c1978",
    "private_key_id": "45a92811d479ef37cf42ab0e7eb8c89ef19dda86",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDRCeSpQ/hpNZ6T\nc3h0HTVQq9aagTL9UhWG5uiXn++CQGt2MbhK7THyzX4jQeJpNyLnwDVK411mP+LJ\nP2oOG3Hvem8w2g+mTAH7oJu6A79uVyClc2kWOCzwC6v1l3gurYbs5bYEXsOxl7L3\nI6tEE74/ODcffTd2utD9Hs20Mpawv+omj38KzXKhC854t6bDJyAl6IenUmnJ1g4f\nnOAi/5PKl7oALutSw98uVjWxlNYLQ5qepi83W8YhiZNRPSFGFOWIzc31uZeLeTrK\nQ82Z5DvMSktwxi0uor2JrV99JkYyChcP1L5rEHdYB/StcrGHWKc3cWsVjayf+JBX\n3lpPpzhhAgMBAAECggEAAfG+WjimyDx8mHhcXgIzVQgfToPcsHUmRxakLPcdX/Nd\n69km0BUDxrNx61rjPngZ+YYA1DowOULcoZNhlD69ywYtxSUllwNQaPL9niZyAMPT\nuBXo69551JxLWSJo5pr+8Q/qdFuOP5tYBE8ad8Hvi58tVCl+wdp3QQ/2O7P1NtY9\nVbQCNhlyjL4V+A2MvYSyGgH0t596XJV4mEdlwbCB1b83cdM4m/8i3xbZG9gWk6mT\nfp5jyH66iJMg0dhWDaXZZgGhcf8Yd9X8N50Rt3/HwchkT9nMcD9dkUFfLS0g9F1M\ngr8Jz4JNRXlTN0hHFciUMjRZZKAbU9GbmCgGfiK4wQKBgQDtYZziWUINXNWCo/z3\nVc/KvPHTgS//2dHbRDumzwJAGV4BCaeVT7tVvyKVtF0ZGvH1S75sBgUTDtX4fQUl\nlctCmDVJOx8UL+DqUT79jIqBU4VMlq8eHBoMwwTPLfOQB2RloFlCD6jSvrzkLUq8\nwGIGB/QG1FUgbL2rGKc8ucgBoQKBgQDhby/v0sX1I4mr2mQTSOsf3c3KFvW7to9e\nXyAhu+znKg/uBwjaY5wj73PvxaEl1FTRLTWcdJpHu1ZryDk7taXtLU/5+1FsWqOX\nfRgCiZm32wA/7Yqdv+nfT5WO6UI9OB2HGt1lqvITHinLVOpVbCa2EJcT9KWqs2h/\nkMCPrtk+wQKBgEvW5dKDBdFTGXu1fLpglhSFrRUPrxAkvSE6eXxfoq5r7FaUiQ/w\n+z7348rEZwIAU9E0s8+7VJ+0G7RZ7O0HIHtUOaH9234NleQGtQM4hX+v+WRwt938\nyG3PWJgAbFJVqkO1qQ6sBhneimaz+a64IBkhLVuJNvE3DJm/NJ74E+hBAoGAf3AT\ncUd9kK6eTQAQQrad9E22399K2urA8WBlEazip2snxi9D2fEle0sKByl5h6EYsYcV\nH3TrIlHM8PEnKZHuUr2i0HY5+T7j6+dTg1u2AjFTWtA15CdxVkPvD/Lc9y6Zwp51\nOdwBLL2IcuF19wREffey8B0E6hKxqCt0L8VwGgECgYEA5vtCwsp1mmST2JFRSMc1\n6kmZ9EZ5amBq0bUb/97htEeznpTnSWBQK55lkT43ZqJ2sdowxdPAkQPbB04E+u/k\n+cPaEFngJuiAgUqmGWslfeoPTpuLDZSi7rWjloW5peIA/Ps21Gyw8L1+g7X0PDtb\nagpB2mnFZWXx+ufqDI498yY=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-uanzs@lingos-c1978.iam.gserviceaccount.com",
    "client_id": "104558507613750714836",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-uanzs%40lingos-c1978.iam.gserviceaccount.com"
}
)
default_app = firebase_admin.initialize_app(credential)

next = False
english_words = ""


def main(user, password, database_name):

    db = firestore.client()
    documents = db.collection(database_name).stream()
    counter = 0
    # print (documents.)
    for doc in documents:
        counter += 1
    print(counter)
    #opcje dla przegladark
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--mute-audio")
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument('log-level=3')
    #automatyczny silnik przegladarki
    driver = webdriver.Chrome(
        ChromeDriverManager().install(), options=chrome_options)

    #logowanie do przegladarki
    driver.get('https://lingos.pl/home/login')
    driver.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys(user)
    driver.find_element(
        By.CSS_SELECTOR, 'input[type="password"]').send_keys(password)
    element = driver.find_element(
        By.CSS_SELECTOR, 'button.btn.btn-primary.btn-lg.w-100')
    webdriver.ActionChains(driver).move_to_element(
        element).click(element).perform()

    #funkcja glowna ktora robi lekcje
    def lesson():
        flag = False
        driver.get("https://lingos.pl/students/learning/")
        #sprawdzenie czy zrobilismy 5 lekcji
        try:
            driver.find_element(
                By.CSS_SELECTOR, "a.btn.rounded-circle.btn-outline-green.disabled")
            print("masz zrobione 5 lekcji")
            next = True
            print(next)
            driver.quit()
           

        #jezeli nie odpalamy bota ktory zapisuje slowka ddo bazy danych

        except NoSuchElementException:
            #szukamy polskiego słowka
            try:
                PL = driver.find_element(By.CSS_SELECTOR, 'h3.mb-0.h3').text
            #przeszukujemy baze danych gdzie wystepuje polskie slowk0 (mozna zrobic to troche inaczej)
                check_Doc = db.collection(database_name).where(
                u"WordPLN", u"==", PL).stream()
            except NoSuchElementException:
                driver.get("https://lingos.pl/students/learning/")
     

            #pobieramy angieslkie slowko
            for doc in check_Doc:
                eng_odp = doc.get('WordENG')
                print(PL, "=>", eng_odp)
                flag = True
            #jezeli pobralismy angielskie slowko program moze przystapic do dzialania
            if flag == True:
                sleep(1)

                try:
                    #znajdujemy element gdzie trzeba wpisac odpowiedz
                    driver.find_element(
                        By.CSS_SELECTOR, 'input#answer').send_keys(eng_odp)
                    #klikamy w element ktory sprawdza nasza odpowiedz
                    driver.find_element(
                        By.CSS_SELECTOR, "button.btn.btn-primary.w-100").click()
                    #jezeli podane slowko jest zle robimy to 
                    english_words = driver.find_element(
                        By.CSS_SELECTOR, 'strong').text
                    #jezeli podane przez nas haslo jest zle a lingos podal nam dobre robimy update w bazie danych
                    if eng_odp != english_words:
                        check_Doc = db.collection(database_name).where(
                            u"WordPLN", u"==", PL).stream()
                    #update bazy danych
                    for doc in check_Doc:
                        print(doc.id)
                        city_ref = db.collection(
                            database_name).document(doc.id)
                        city_ref.update({u'WordENG': english_words})
                        flag = True

                except NoSuchElementException:
                    driver.find_element(
                        By.CSS_SELECTOR, "button.btn.btn-primary.w-100").click()
                flag = False

            else:

                driver.find_element(
                    By.CSS_SELECTOR, "button.btn.btn-primary.w-100").click()

                try:
                    ENG = driver.find_element(By.CSS_SELECTOR, 'strong').text
                    new_doc = db.collection(database_name).document()

                    new_doc.set({
                        u"WordPLN": PL,
                        u"WordENG": ENG,
                    })

                except NoSuchElementException:
                    driver.get("https://lingos.pl/students/learning/")

    for i in range(100):
        lesson()
    driver.close()

#Zawodowy angielski

main("Hubert Kinstler", "Hubert123", "Words_Zaw")
# main("mikolajklosowski112@gmail.com", "Marycha3", "Words_Pod")