from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

@dataclass
class TicketUpdate:
    timestamp: str
    note: str

@dataclass
class Ticket:
    id: int
    title: str
    requester: str
    priority: str = "Medium"   # Low / Medium / High
    status: str = "Open"       # Open / In Progress / Closed
    created_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))
    updates: List[TicketUpdate] = field(default_factory=list)

    def add_update(self, note: str) -> None:
        self.updates.append(TicketUpdate(datetime.now().isoformat(timespec="seconds"), note))

tickets: List[Ticket] = []

def create_ticket() -> None:
    title = input("Title: ").strip()
    requester = input("Requester: ").strip()
    priority = input("Priority (Low/Medium/High): ").strip().title() or "Medium"
    ticket_id = (tickets[-1].id + 1) if tickets else 1
    t = Ticket(id=ticket_id, title=title, requester=requester, priority=priority)
    t.add_update("Ticket created.")
    tickets.append(t)
    print(f"\nCreated ticket #{t.id}\n")

def list_tickets() -> None:
    if not tickets:
        print("\nNo tickets yet.\n")
        return
    print("\nTickets:")
    for t in tickets:
        print(f"#{t.id} | {t.status:<11} | {t.priority:<6} | {t.title} (Requester: {t.requester})")
    print()

def find_ticket(ticket_id: int) -> Optional[Ticket]:
    return next((t for t in tickets if t.id == ticket_id), None)

def update_ticket() -> None:
    try:
        ticket_id = int(input("Ticket ID: ").strip())
    except ValueError:
        print("Invalid ID.\n")
        return

    t = find_ticket(ticket_id)
    if not t:
        print("Ticket not found.\n")
        return

    print(f"\nSelected: #{t.id} {t.title} [{t.status}]\n")
    new_status = input("New status (Open/In Progress/Closed) or leave blank: ").strip().title()
    note = input("Update note: ").strip()

    if new_status:
        t.status = new_status
        t.add_update(f"Status changed to {new_status}.")
    if note:
        t.add_update(note)

    print("\nTicket updated.\n")

def view_ticket() -> None:
    try:
        ticket_id = int(input("Ticket ID: ").strip())
    except ValueError:
        print("Invalid ID.\n")
        return

    t = find_ticket(ticket_id)
    if not t:
        print("Ticket not found.\n")
        return

    print(f"\n--- Ticket #{t.id} ---")
    print(f"Title: {t.title}")
    print(f"Requester: {t.requester}")
    print(f"Priority: {t.priority}")
    print(f"Status: {t.status}")
    print(f"Created: {t.created_at}")
    print("Updates:")
    for u in t.updates:
        print(f"- {u.timestamp}: {u.note}")
    print()

def main() -> None:
    while True:
        print("1) Create ticket")
        print("2) List tickets")
        print("3) Update ticket")
        print("4) View ticket")
        print("5) Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            create_ticket()
        elif choice == "2":
            list_tickets()
        elif choice == "3":
            update_ticket()
        elif choice == "4":
            view_ticket()
        elif choice == "5":
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()
