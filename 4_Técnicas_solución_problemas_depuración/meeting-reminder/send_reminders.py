import sys
import datetime

def message_template(date, title):
    return f"Reminder: {title} on {date} ({dow(date)})"

def dow(date):
    dateobj = datetime.datetime.strptime(date, "%Y-%m-%d")
    return dateobj.strftime("%A")

def send_message(message, emails):
    print("Sending:", message, "to", emails)
    # Aquí iría tu lógica real de envío

def usage():
    print("Usage: send_reminders.py 'date|title|emails'")

def main():
    if len(sys.argv) < 2:
        return usage()

    try:
        date, title, emails = sys.argv[1].split('|')
        message = message_template(date, title)
        send_message(message, emails)
        print("Successfully sent reminders to:", emails)
    except Exception as e:
        print("Failure to send email:", e, file=sys.stderr)

if __name__ == "__main__":
    main()
