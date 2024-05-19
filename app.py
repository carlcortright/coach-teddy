import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flyflowclient import Flyflow

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

client = Flyflow(api_key=os.getenv('FLYFLOW_API_KEY'))

@app.route('/webhook', methods=['POST'])
def webhook():
    event_data = request.get_json()
    event = event_data['event']

    if event == 'call_started':
        call = event_data['call']
        client_number = call['client_number']

        # Get the 10 most recent calls for the client number
        calls = client.list_calls(client_number=client_number, limit=10)

        # Set the context to have the calls and their transcripts
        context = 'Previous calls this client has had with coach teddy: \n\n'
        for i, enumeratedcall in enumerate(calls['calls']):
            call_date = enumeratedcall['created_at'][:10]  # Extract the date portion from the timestamp
            transcript = enumeratedcall['transcript']
            if transcript is not None:
                transcript = transcript[1:]
            if transcript and i != 0:  # Skip the first item in the transcript
                context += f"Call ID: {enumeratedcall['id']}\nDate: {call_date}\nTranscript: {transcript}\n\n"

        client.set_call_context(call['id'], context)

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)