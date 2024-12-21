from twilio.rest import Client
from threading import Thread

# Twilio credentials (replace with your actual credentials)
account_sid = 'your_account_sid'  # Replace with your Twilio Account SID
auth_token = 'your_auth_token'    # Replace with your Twilio Auth Token
client = Client(account_sid, auth_token)

# List of phone numbers to call (use placeholders or your real numbers)
phone_numbers = [
    'your_phone_number_1',  # Replace with actual phone numbers
    'your_phone_number_2',
    # Add all 60 numbers here
]

# The text message you want to convert into speech
text_message = "Hello, this is a test message sent using Twilio’s text-to-speech feature."

def make_call(number):
    try:
        call = client.calls.create(
            to=number,
            from_='your_twilio_phone_number',  # Replace with your Twilio phone number
            twiml=f'<Response><Say>{text_message}</Say></Response>'
        )
        print(f"Call initiated to {number} - Call SID: {call.sid}")
    except Exception as e:
        print(f"Failed to initiate call to {number}: {str(e)}")

def call_members_simultaneously():
    threads = []
    for number in phone_numbers:
        thread = Thread(target=make_call, args=(number,))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    call_members_simultaneously()
