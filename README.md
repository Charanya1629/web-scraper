# web-scraper
 which focuses on building a web scraper to extract news headlines from a public website.
 
# Objective

Automate the collection of top news headlines from a public website using Python, requests, and BeautifulSoup.

# Tools Used

Tool-Purpose

1. Python 3-The programming language used for scripting. 

2. requests-Library used to fetch the HTML content of the news page (Step 1: Fetch HTML). 

3. BeautifulSoup-Library used to parse the HTML and extract the desired headline text (Step 2: Parse tags). 

# Deliverables

1. web_scraper.py: The complete Python script.

2. headlines.txt: The text file containing the scraped headlines

# How to Run the Script

1. Setup Environment
 
First, install the necessary Python packages using pip:

pip install requests beautifulsoup4

2. Execution

    Run the main Python script from your terminal:

     python web_scraper.py

3. Output
   
     Upon successful execution, the script will:

- Print a status update showing the headlines it found.

- Create a file named 

headlines.txt in the same directory, containing all the scraped headlines, one per line (Step 3: Save titles)

# Sample Output (headlines.txt)
- The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.
- It is our choices, Harry, that show what we truly are, far more than our abilities.
- There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.
