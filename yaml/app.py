#!/usr/bin/python3

from flask import Flask, request, render_template
import yaml

app = Flask(__name__)
# disabling default 12 hour caching during dev
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/', methods=['GET','POST'])
def my_form():
  if request.method == 'POST':
    text = request.form['config']
    try:
      yaml_conf = yaml.load(text)
    except:
      data = "error_text: unable to parse configuration! error_flag: ERR{qEC_11gce#!Do0}"
      return render_template('form.html', data=data)
    try:
      target = "target {}".format(yaml_conf['target'])
      secret = "secret {}".format(yaml_conf['secret'])
      action = "action {}".format(yaml_conf['action'])
      data = "Attempt to execute {} on {} with {} failed! Are target, secret and action valid?".format(action, target, secret)
      return render_template('form.html', data=data)
    except: 
      data = "error_text: unable to parse configuration: target, secret and action fields are mandatory! error_flag: ERR{br0_dsafD34!d}"
      return render_template('form.html', data=data)
  else:
    return render_template('form.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5300, debug=True)
