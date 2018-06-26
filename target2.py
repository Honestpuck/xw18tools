import flask
import jss_tools as tools
from threading import Thread

from flask_mail import Mail, Message

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
def membership_changed():
    changes = flask.request.get_json()
    if not changes:
        return '', 400
    XWDemo(changes['event'])
    return '', 200


def XWDemo(data)
    thr = Thread(target=XWDemo, args=[data])
    thr.start()


def XWDemo_thread(data):
    jss = open_jss()
    for id in data['groupAddedDevicesIds']:
        computer = jss.Computer(id)
        attrs = tools.c_attributes(computer)
        attrs['XWDemoDate'] = tools.Now()
        c_attributes_write(attrs, computer)
    for id in data['groupRemovedDevicesIds']:
        computer = jss.Computer(id)
        attrs = tools.c_attributes(computer)
        attrs['XWDemoDate'] = ''
        c_attributes_write(attrs, computer)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)


