from twilio.rest import Client
from threading import Thread

# Twilio credentials
account_sid = 'AC4241705bddc9eff11fcf1c8663500454'  # Replace with your Twilio Account SID
auth_token = '32b66d8d91ec5b7955fbdc521fb1e90f'    # Replace with your Twilio Auth Token
client = Client(account_sid, auth_token)

# List of phone numbers to call
phone_numbers = [
    '+919442794502',
    '+918754102493',
    # Add all 60 numbers here
]

# The text message you want to convert into speech
text_message = "Hello, this is a test message sent using Twilio’s text-to-speech feature."

def make_call(number):
    try:
        call = client.calls.create(
            to=number,
            from_='+12513135031',  # Replace with your Twilio phone number
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

