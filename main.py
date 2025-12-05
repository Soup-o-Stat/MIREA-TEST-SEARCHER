import requests
from bs4 import BeautifulSoup

course_url = "https://online-edu.mirea.ru/course/view.php?id=????"
cookie = {
    "MoodleSession": ""}

def menu():
    global course_url, cookie
    print("-" * 40)
    print("MIREA TEST SEARCHER")
    print("-" * 40)
    print("1. Search tests")
    print("2. Setup arguments")
    print("3. Help")
    print("0. Exit")
    choose=str(input(">> "))
    if choose == "1":
        find_tests(cookie, course_url)
    elif choose == "2":
        setup()
    elif choose == "0":
        exit()
    elif choose == "3":
        print("-" * 40)
        print("----------------------------------------\n"
              "HELP MESSAGE\n"
              "So, here's the deal.\n\n"
              "This script lets you scan a MIREA course page for available tests.\n"
              "Yeah, it’s simple — unless you screw up the cookie or the URL.\n\n"
              "1) Make sure your MoodleSession cookie is correct.\n"
              "   - Open the course in your browser.\n"
              "   - Press F12.\n"
              "   - Go to \"Application\" --> \"Cookies\".\n"
              "   - Copy the MoodleSession value. ONLY the value, don’t paste random shit.\n\n"
              "2) Put the full course URL.\n"
              "   - Something like: https://online-edu.mirea.ru/course/view.php?id=12345\n"
              "   - If you see \"????\" instead of digits — fix it.\n\n"
              "3) Don’t ask why it doesn’t work if you didn’t fill the cookie.\n"
              "   90% of issues are just \"forgot to paste the cookie\n\n"
              "----------------------------------------")

def setup():
    global course_url, cookie
    print("Input your cookie")
    cookie_to_setup=str(input(">> "))
    print("Input your course url")
    course_url=str(input(">> "))
    cookie = {"MoodleSession": cookie_to_setup}

def find_tests(cookie, url):
    r = requests.get(url, cookies=cookie)

    if r.status_code != 200:
        print("Error!")
        return

    soup = BeautifulSoup(r.text, "html.parser")
    quizzes = soup.find_all("li", class_="modtype_quiz")

    if not quizzes:
        print("Shit, i cant find any test!")
        return

    print(f"I found: {len(quizzes)} test!\n")

    for q in quizzes:
        module_id = q.get("id").replace("module-", "")
        name_tag = q.select_one(".instancename")
        name = name_tag.text.strip() if name_tag else "No name"
        url = f"https://online-edu.mirea.ru/mod/quiz/view.php?id={module_id}"
        print(f"Name: {name}")
        print(f"ID: {module_id}")
        print(f"URL: {url}")
        print("-" * 40)

if __name__=="__main__":
    while True:
        menu()
