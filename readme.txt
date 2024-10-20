py ./main.py        #To run the scrapper
config.py           #To configure
                        environment
                        facebook profile
                        paths and selctors

pages.txt           #To manage pages
NoiseSaigon.csv     #To Retrieve scraped data


Workflow:
    read csv for exirting events
    Get a list of files from "pages.txt"
    For each page do:
        Open page:
        Get all events:
            Open event page:
                Crawl for all data
                get missing adata and price using GROQ_AI
            Add event to file (if full_update is true)
            savefile (prevent data lass in case of crash)

