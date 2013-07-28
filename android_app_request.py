import requests
import json
import sys

url = 'https://android.googleapis.com/gcm/send'
payload = {
  "registration_ids" : ["APA91bEce8m_WglQ1288TCcic6C4KoNxzosAdWaZEDkOTWF7j6oYvQqPS147C5135YnWTk_SYGO5waCrd7xTJMDShJcrTreP5JSqGFtyOH1MSdcvYI4jR4O40Z5C831DTVGavC0uX_tI1ukhCDH7M8jsAZRUF8Y4Pky9gy88-t9I6ik805Ab1gg"],
  "data": {
  	"roombaVideoChat": None
  }
}
headers = {'Content-Type': 'application/json', 'Authorization': 'key=AIzaSyAxNRgVDkx9CvnuNYJWiQhOGJRA8JRanAA'}

def start():
	payload['data']['roombaVideoChat'] = 'start'
	r = requests.post(url, data=json.dumps(payload), headers=headers)
	print "Starting app:", r.text

def stop():
	payload['data']['roombaVideoChat'] = 'stop'
	r = requests.post(url, data=json.dumps(payload), headers=headers)
	print "Stopping app:", r.text
