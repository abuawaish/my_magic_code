from twilio.rest import Client
from datetime import datetime, timedelta
import time

# Initialize Twilio client with account credentials
account_sid: str = "YOUR_SID" # get it from twilio
auth_token: str = "YOUR_AUTH_TOKEN" # get it from twilio
client: Client = Client(account_sid, auth_token)


def send_message(recipient_number: str, message_body: str) -> None:
    """
    Sends a WhatsApp message to the specified recipient.
    """
    try:
        message = client.messages.create(
            from_='whatsapp:YOUR_PHONE_NUMBER', # get it from twilio
            body=message_body,
            to=f'whatsapp:{recipient_number}'  # Corrected to use 'whatsapp:' prefix
        )
        print(f'Message sent successfully! Message SID -> {message.sid}')
    except Exception as e:
        print(f"An error occurred -> {e}")


def get_user_input() -> tuple[str, ...]:
    """
    Gathers input from the user regarding the recipient and the message.
    """
    name: str = input("Enter the recipient name: ")
    recipient_number: str = input("Enter the recipient WhatsApp number with country code (e.g., +91): ")
    message_body: str = input(f"Enter the message you want to send to {name}: ")
    return name, recipient_number, message_body


def get_schedule_time() -> tuple[float, datetime]:
    """
    Gets the date and time from the user and calculates the delay in seconds.
    """
    date_str: str = input("Enter the date to send the message (YYYY-MM-DD): ")
    time_str: str = input("Enter the time to send the message (HH:MM:SS in 24-hour format): ")

    schedule_time: datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M:%S")
    current_datetime: datetime = datetime.now()

    time_difference: timedelta = schedule_time - current_datetime
    delay_seconds: float = time_difference.total_seconds()

    return delay_seconds, schedule_time


def main() -> None:
    """
    The main function that orchestrates the scheduling and sending of the message.
    """
    name, recipient_number, message_body = get_user_input()  # Gather user input
    delay_seconds, schedule_time = get_schedule_time()  # Get scheduling information

    if delay_seconds <= 0:
        print("The specified time is in the past. Please enter a future date and time.")
    else:
        print(f"Message scheduled to be sent to {name} at {schedule_time}.")
        time.sleep(delay_seconds)  # Wait until the scheduled time
        send_message(recipient_number, message_body)  # Send the message


if __name__ == "__main__":
    main()

