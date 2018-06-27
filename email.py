import flask
from flask_mail import Mail, Message
from threading import Thread


class Configuration(object):
    MAIL_SERVER = 'smtp.your.org'
    MAIL_PORT = 587  # SSL/TLS port
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False  # Disable for POODLE
    MAIL_USERNAME = 'sender@your.org'
    MAIL_PASSWORD = 'secret_password'
    MAIL_DEFAULT_SENDER = 'Your Notifications <noreply@your.org>'


app = flask.Flask(__name__)
app.config.from_object(Configuration)
email = Mail(app)


@app.route('/XWDemo', methods=['POST'])
def membership changed():
    ...


def send_email(name, mac, email):
    subject = 'Virus Definitions Not Up To Date'
    email_data = {
        'name': name,
        'mac_name': mac,
    }
    txt = build_email_body(email_data)
    msg = Message(
        subject,
        recipients=[DESTINATION_EMAIL]
    )
    msg.body = txt
    msg.html = html
    thr = Thread(target=send_async_email, args=[msg])
    thr.start()


def send_async_email(msg):
    with app.app_context():
        email.send(msg)




if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
