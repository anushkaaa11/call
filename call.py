from flask import Flask, request, render_template
from twilio.rest import Client

app = Flask(__name__)

# Your Account SID and Auth Token from twilio.com/console
account_sid = 'AC9aeb260122a2916798fc8fcae047d640'
auth_token = '30acc2627bd63d410dd97c2834a395fc'
client = Client(account_sid, auth_token)

@app.route('/')
def index():
    return render_template('call.html')

@app.route('/make_call', methods=['POST'])
def make_call():
    phone_number = request.form['phone_number']

    if not phone_number:
        return "Error: 'To' phone number is required."

    try:
        call = client.calls.create(
            to=phone_number,
            from_='+16034466198',  # provided by Twilio API
            url='http://demo.twilio.com/docs/voice.xml'
        )
        return f"Call initiated! SID: {call.sid}"
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)