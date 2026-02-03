def generate_invitations(template, attendees):
    if not isinstance(template, str) or not isinstance(attendees, list) \
       or not all(isinstance(a, dict) for a in attendees):
        print("Invalid input types.")
        return

    if template == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        name = attendee.get("name") if attendee.get("name") else "N/A"
        event_title = attendee.get("event_title") if attendee.get("event_title") else "N/A"
        event_date = attendee.get("event_date") if attendee.get("event_date") else "N/A"
        event_location = attendee.get("event_location") if attendee.get("event_location") else "N/A"

        invitation = invitation.replace("{name}", str(name))
        invitation = invitation.replace("{event_title}", str(event_title))
        invitation = invitation.replace("{event_date}", str(event_date))
        invitation = invitation.replace("{event_location}", str(event_location))

        filename = f"output_{index}.txt"
        with open(filename, "w") as file:
            file.write(invitation)
