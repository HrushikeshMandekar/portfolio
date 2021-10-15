from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)  


@app.route('/') # This is the root directory
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>') # This is for the dynamic page routes, and the input must be string after /
def html_page(page_name):
    return render_template(page_name)

# To store the data in database
def write_file(data):
    with open('database.txt', mode='a') as databases:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file =databases.write(f'\n{email}, {subject}, {message}')

# To store the data in csv file
def write_csv(data):
    with open('database2.csv', mode='a', newline='') as db2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer =csv.writer(db2, delimiter=',', quotechar='|',  quoting=csv.QUOTE_MINIMAL)      
        # first we give file name in which we want to write
        # delimiter is for by what you want to separate the columns, default is comma ','
        # quotechar is to want quotes around the character
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict() # collected the data and stored it into the dictionary
            write_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did dont save to database'
    else:
        return "Something went wrong. Try again!"