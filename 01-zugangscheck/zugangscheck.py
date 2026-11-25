alter = int(input("Enter Dein alter : "))
ticket_answer = input("Hast du ein Ticket? (ja/nein) ").strip().lower()
has_ticket = ticket_answer == "ja"
print("Ticket vorhanden : " , has_ticket )
full = alter >= 18
print("Volljährig : " , full)
can_enter = full and has_ticket
print("Zugang erlaubt : " , can_enter)
need_check = alter<18 or not has_ticket
print("Prüfung notwendig : " , need_check )
