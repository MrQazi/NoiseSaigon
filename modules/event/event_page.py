from driver import Options
from config import EVENT_PAGE_TITLE,EVENT_PAGE_DATETIME,EVENT_PAGE_VENUE,EVENT_PAGE_DETAIL_CONTAINTER, SEE_MORE_WAIT
from config import SEE_MORE_WAIT
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from groqAI import ParseWithAI 

class EventDetails:
    ID = ""
    Name = ""
    Date = ""
    Description = ""
    Time = ""
    LineUp = ""
    BookingTicketPrice = ""
    DoorTicketPrice = ""
    Venue = ""

    Event_Link = ""
    Venue_Link = ""
    
    def Load(self,**args):        
        for key, value in args.items():
            setattr(self, key, value)
    
    def __init__(self,URL:str) -> None:
        self.ID = ""
        self.Name = ""
        self.Date = ""
        self.Description = ""
        self.Time = ""
        self.LineUp = ""
        self.BookingTicketPrice = ""
        self.DoorTicketPrice = ""
        self.Venue = ""

        self.Event_Link = ""
        self.Venue_Link = ""
        
        if(len(URL) > 0):
            self.Event_Link = URL
            self.ID = URL.split("/")[-1]
    
    def FetchBaseData(self):
        driver = webdriver.Chrome(options=Options)
        self.Name = driver.find_element(EVENT_PAGE_TITLE[0],EVENT_PAGE_TITLE[1]).text
        d = driver.find_element(EVENT_PAGE_DATETIME[0],EVENT_PAGE_DATETIME[1]).text
        d_t = d.split(" at ")
        
        if(len(d_t) == 1 ):
            d_t = d.split(" from ")
        if(len(d_t) == 2):
            self.Date,self.Time = d_t[0].strip(),d_t[1].strip()
        venue = driver.find_element(EVENT_PAGE_VENUE[0],EVENT_PAGE_VENUE[1])
#        self.Venue = venue.text
        self.Venue_Link = venue.get_attribute("href")
    
    def FetchDescription(self):
        driver = webdriver.Chrome(options=Options)
        _cont = driver.find_element(EVENT_PAGE_DETAIL_CONTAINTER[0],EVENT_PAGE_DETAIL_CONTAINTER[1])
        _desc = _cont.find_elements(By.XPATH,"./*")[-1]
        try:
            _desc.find_element(By.CSS_SELECTOR,"div.x11i5rnm.xat24cr.x1mh8g0r.x1vvkbs.xtlvy1s > div").click()
        except:     
            print("no see more button")
        time.sleep(SEE_MORE_WAIT)
        self.Description = _desc.text
        
    def ResolveMissingData(self):
        query = f"""
        return a json file only containing BookingTicketPrice,DoorTicketPrice,Venue and LineUp fields
        
        strictly follow these instructions
        no extra details
        preserve the currency in given format
        lineup as array of names 
        use full address

        {self.Description}
        """
        data = ParseWithAI(query)
        self.BookingTicketPrice = data["BookingTicketPrice"]
        self.DoorTicketPrice = data["DoorTicketPrice"]
        self.Venue = data["Venue"]
        self.LineUp = data["LineUp"]