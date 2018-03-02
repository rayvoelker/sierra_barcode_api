import sys, psycopg2, datetime, configparser
from flask import Flask
from flask import json
from flask_restful import Resource, Api


def clear_connection():
	if 'conn' in globals():
		global conn
		if hasattr(conn, 'close'):
			conn.close()
		conn = None

	if 'cur' in globals():
		global cur
		if hasattr(cur, 'close'):
			cur.close()
		cur = None

# import configuration file containing our connection string
# app.ini looks like the following
#[db]
#	connection_string = dbname='iii' user='PUT_USERNAME_HERE' host='sierra-db.library-name.org' password='PUT_PASSWORD_HERE' port=1032
config = configparser.ConfigParser()
config.read('app.ini')

app = Flask(__name__)
api = Api(app)

# not sure if we should connect to the db for each request .. or connect to the db, and stay connected... doing the latter for now
try:
	# variable connection string should be defined in the imported config file
	conn = psycopg2.connect( config['db']['connection_string'] )
except:
	print("unable to connect to the database")
	clear_connection()
	sys.exit(1)

# here's our base query ...
sql = """\
---
SELECT
upper(p.call_number_norm) AS call_number_norm,
v.field_content AS volume,
i.location_code,
i.item_status_code,
b.best_title,
c.due_gmt,
i.inventory_gmt

FROM
sierra_view.phrase_entry AS e
JOIN
sierra_view.item_record_property AS p
ON
  e.record_id = p.item_record_id
  JOIN sierra_view.item_record AS i
ON
  i.id = p.item_record_id
LEFT OUTER JOIN sierra_view.checkout AS c
ON
  i.id = c.item_record_id
-- This JOIN will get the Title and Author from the bib
JOIN
sierra_view.bib_record_item_record_link	AS l
ON
  l.item_record_id = e.record_id
JOIN
sierra_view.bib_record_property AS b
ON
  l.bib_record_id = b.bib_record_id

LEFT OUTER JOIN
sierra_view.varfield AS v
ON
  (i.id = v.record_id) AND (v.varfield_type_code = 'v')
WHERE
e.index_tag || e.index_entry = 'b' || LOWER('0989053860015')
---
"""

try:
	cur = conn.cursor()
	cur.execute(sql)

except:
	print("error connecting or running query sql")
	clear_connection()
	sys.exit(1)

output = ( list( cur.fetchone() ) )
# print the output to standard out ...
print(output)

class HelloWorld(Resource):
	def get(self):
		#return {'hello': 'world'}
		return json.dumps(output)

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
	app.run(debug=True)
