"""
Write a class Train which has methods to book a ticket, get status (no of seats)
and get fare information of train running under Indian Railways.
"""

from random import randint

class Train:
    
    def __init__(slf, trainNo):
        slf.trainNo = trainNo
        
    def book(slf, fro, to):
        print(f"Ticket is booked in train no: {slf.trainNo} from {fro} to {to}")
        
    def getStatus(slf):
        print(f"Train no: {slf.trainNo} is running on time!")
        
    def getFare(slf, fro, to):
        print(f"Ticket fare in train no: {slf.trainNo} from {fro} to {to} is {randint(222, 5555)}")
        
t=Train(123999)
t.book("Rampur", "Delhi")
t.getStatus(123999)
t.getFare("Rampur", "Delhi")