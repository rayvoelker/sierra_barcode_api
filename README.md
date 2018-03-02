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
