from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# -----------------------
# Data Model (Ticket)
# -----------------------
class Ticket(BaseModel):
    title:str = " internet connection"
    description: str = " My internet connection is not working properly."
    priority: str = "high"

# -----------------------
# In-memory database
# -----------------------
tickets = []

# -----------------------
# Root route
# -----------------------
@app.get("/")
def home():
    return {"message": "AI Helpdesk API is running"}

# -----------------------
# Create ticket
# -----------------------
@app.post("/tickets")
def create_ticket(ticket: Ticket):
    tickets.append(ticket)
    return {
        "message": "Ticket created successfully",
        "ticket": ticket
    }

# -----------------------
# Get all tickets
# -----------------------
@app.get("/tickets")
def get_tickets():
    return tickets