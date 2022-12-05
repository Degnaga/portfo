from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import csv
import os

app = Flask(__name__)

print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        emael = data["email"]
        subject = data["subject"]
        massage = data["message"]
        file = database.write(f'\n{emael},{subject},{massage}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        emael = data["email"]
        subject = data["subject"]
        massage = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([emael, subject, massage])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again!'


'''
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
                               '''

'''
@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/works.html')
def works():
    return render_template('works.html')


@app.route('/work.html')
def work():
    return render_template('work.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/components.html')
def components():
    return render_template('components.html')
    '''
