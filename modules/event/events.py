from pprint import pprint
from Reader import CSV_Reader
from driver import Options
from modules.event.event_page import EventDetails
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from config import EVENT_LIST_CONTSAINER,EVENT_LIST_TILE_SELECTOR,EVENT_LIST_TILE_URL, FULL_UPDATE
from config import PAST,FUTURE
from config import PAGE_WAIT,SEE_MORE_WAIT


########################################



Reader = CSV_Reader("./NoiseSaigon.csv")


def AddDummyEvent():
    Reader.ReadFromFile()
    event = EventDetails("")
    event.ID = "1144131884055628"
    event.Event_Link = "https://web.facebook.com/events/1144131884055628"
    event.Name = "Meetup"
    event.BookingTicketPrice = 500
    event.DoorTicketPrice = 700
    event.Date ="today"
    event.Time = "eventing"
    event.Venue = "rooftop"
    event.Venue_Link = "stairs"
    Reader.SaveEvent(event)

def SyncEvent(eventURL:str):
    driver = webdriver.Chrome(options=Options)
    event = EventDetails(eventURL)
    e = Reader.FindEvent(event.ID)
    if(e):
        if(not FULL_UPDATE):
            return
    
    driver.get(eventURL)
    time.sleep(PAGE_WAIT)
    event.FetchBaseData()
    event.FetchDescription()
    event.ResolveMissingData()
    
    Reader.SaveEvent(event)


def GetAllUpcoming(page):
    Crawl(page,"upcoming_hosted_events")
    
        
def GetAllPast(page):
    Crawl(page,"past_hosted_events")
    
        

def Crawl(page,type):
    Reader.ReadFromFile()
    driver = webdriver.Chrome(options=Options)
    driver.get(f'https://web.facebook.com/pg/{page}/{type}')
    time.sleep(PAGE_WAIT)
    container = driver.find_element(EVENT_LIST_CONTSAINER[0], EVENT_LIST_CONTSAINER[1])
    
    for child in container.find_elements(EVENT_LIST_TILE_SELECTOR[0], EVENT_LIST_TILE_SELECTOR[1]):
        eventURL = child.find_element(EVENT_LIST_TILE_URL[0],EVENT_LIST_TILE_URL[1]).get_attribute("href")
        SyncEvent(eventURL)
    

def Getevents():
    with open("pages.txt") as file:
        for line in file:
            page = line.rstrip()
            if(FUTURE):
                GetAllUpcoming(page)
                continue
            if(PAST):
                GetAllPast(page)
                continue
            
