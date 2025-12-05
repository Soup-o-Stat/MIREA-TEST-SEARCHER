# MIREA Test Searcher

**Description**
This script allows you to search for available tests on MIREA course pages (online-edu.mirea.ru). It is simple to use and designed for students who want to quickly find tests without manual browsing.

---

## Features

* Find all tests on a course page.
* Configure cookie and course URL.
* Display test name, ID, and a direct link to the test.

---

## Installation

1. Make sure you have Python 3.7+ installed.
2. Install dependencies:

```bash
pip install requests beautifulsoup4
```

3. Download the script to your computer.

---

## Usage

1. Open your course in a browser and get the `MoodleSession` cookie:

   * Press F12 --> go to the **Application** tab --> **Cookies**.
   * Copy the value of `MoodleSession` (value only, do not copy extra characters).

2. Get the full course URL, for example:
   `https://online-edu.mirea.ru/course/view.php?id=12345`

3. Run the script:

```bash
python main.py
```

4. Menu options:

   * **1** — Search tests
   * **2** — Setup cookie and course URL
   * **3** — Help
   * **0** — Exit

5. After choosing “Search tests”, the script will display:

   * Test name
   * Module ID
   * Direct URL to the test

---

## Example Output

```
I found: 3 test(s)!

Name: Mathematics Test 1
ID: 1234
URL: https://online-edu.mirea.ru/mod/quiz/view.php?id=1234
----------------------------------------
Name: Physics Test 2
ID: 5678
URL: https://online-edu.mirea.ru/mod/quiz/view.php?id=5678
----------------------------------------
```

---

## Important Notes

* The script will not work without a valid cookie and course URL.
* Use it only for your own courses and for educational purposes.
* The script does not submit tests — it only finds them.

---
