import csv
import json
from modules.event.event_page import EventDetails
from typing import List
from config import FULL_UPDATE


class CSV_Reader:    
    events : List[EventDetails] = []
    path = ""
    def __init__(self,path):
        self.path = path
        self.ReadFromFile()
    
    def LoadEvent(self,row):
        event = EventDetails("")
        event.Load(**row)
        self.events.append(event)
    
    def FindEvent(self,ID:str) -> EventDetails:
        for event in self.events:
            if(event.ID == ID): return event
        return None
    
    def SaveEvent(self,event:EventDetails): 
        e = self.FindEvent(event.ID)
        if(e):
            if(FULL_UPDATE):
                e.Load(**event.__dict__)
                self.SaveToFile()
            return
        self.events.append(event)
        self.SaveToFile()
        
    def ReadFromFile(self):
        if(FULL_UPDATE):
            self.events = []
            return
        with open(self.path, mode='r', newline='') as csv_file:
            for row in csv.DictReader(csv_file):
                self.LoadEvent(row)
    
    def SaveToFile(self):
        if not self.events:
            return  # If there are no events, return early to avoid errors

        # Get the fieldnames from the first event's attributes
        fieldnames = list(self.events[0].__dict__.keys())

        with open(self.path, mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()  # Write the CSV header

            for event in self.events:
                writer.writerow(event.__dict__)  # Write each event's attributes as a row