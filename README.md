# sierra_barcode_api

## install instructions
* install python3 and pip3 from your distribution's package manager ```sudo apt-get install python3 python3-pip3```
* install virtualenv from pip3 ```sudo pip3 install virtualenv --upgrade```
* clone this repo ```git clone https://github.com/rayvoelker/sierra_barcode_api.git```
* move to the repo dir ```cd sierra_barcode_api/```
* create the virtualenv ```virtualenv env```
* enable virtualenv ```source env/bin/activate```
* install the required python dependencies ```pip install -r requirements.txt```
* configure the variables in the ```app.ini``` file ```mv app.ini.example app.ini``` ```nano app.ini```
* run the server! ```python app.py```


## install instructions for running the Python flask web application via the apache2 web server via mod-wsgi
* install apache2, and apache mod_wsgi on your system. ```sudo apt-get install apache2 libapache2-mod-wsgi-py3```
* check the file ```app.wsgi``` and change paths were needed
* move the file ```apache2_sierra_barcode_api.conf.sample``` to ```/etc/apache2/sites-available/apache2_sierra_barcode_api.conf```
* check the file at ```/etc/apache2/sites-available/apache2_sierra_barcode_api.conf``` and verify that paths are correct
* enable the site ```sudo a2ensite apache2_sierra_barcode_api.conf```
* reload apache configurations ```sudo systemctl reload apache2```
