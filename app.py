from pymessenger import Bot
import os, sys, requests, json
from flask import Flask, request, jsonify

app = Flask('My echo bot')
PAGE_ACCESS_TOKEN = 'EAAg4f5ZBJPCwBACZBIOH5xDydyb4utfDO7sFuG2hChwCewqppbHYux2KrfExxtlz7wiEeYAaWUlZAgZBgfBtCoxHixH0ZAwer7NGHQG3nLTdsrkZCQTJbO33gT61GcpVmMcFagBbBPm7we5NZCaNlqobTeh85S6LemDHiJ800EibFMUtl58IQZA4YA3VTAC5qkEZD'
bot = Bot(PAGE_ACCESS_TOKEN)
fb_api = "https://graph.facebook.com/v4.0/me/messages"
profile_api = "https://graph.facebook.com/v4.0/me/messenger_profile"
VERIFICATION_TOKEN = "hello"
token_dict = {"access_token": PAGE_ACCESS_TOKEN}
welcome_message = "Get Started clicked. Go fun yourself. ASSALAM-U-ALAIKUM 🙂\n\n Nigga Nice to meet you. 😊\nDigiSkills Chatbot at your service 🤖"
next_message = "⚠⚠⚠\nIf you want to chat with a Human just go to Menu with text field of Messenger and click \"Live Chat\" 📱"

"""@app.route('/', methods=['GET'])
def verify():
	if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
		if not request.args.get("hub.verify_token") == VERIFICATION_TOKEN:
			return "Verification token mismatch", 403
		return request.args["hub.challenge"], 200
	return "Hello world", 200"""


@app.route('/', methods=['POST'])
def webhook():
	print(request.data)
	data = request.get_json()
	#get_started = requests.post(fb_api,params=token_dict,{"get_started":{"payload":"some bitch clicked the get started button"}})
	#persistent_menu_json = {"persistent_menu":[{"locale":"default","composer_input_disabled":False,"call_to_actions":[{"type":"postback","title":"Talk to an agent","payload":"CARE_HELP"},{"type":"postback","title":"Outfit suggestions","payload":"CURATION"},{"type":"web_url","title":"Shop now","url":"https://www.originalcoastclothing.com/","webview_height_ratio":"full"}]}]}
	#persistent = requests.post(profile_api, params=token_dict, json= persistent_menu_json)
	#print("persistent",persistent)
	#get_started_json= {"get_started":{"payload":"some bitch clicked the get started button"}}
	#get_started = requests.post(profile_api,params=token_dict,data = json.dumps(get_started_json), headers={'Content-Type': 'application/json'})
	#print("get_started", get_started)

	if data['object'] == "page":
		entries = data['entry']

		for entry in entries:
			messaging = entry['messaging']

			for messaging_event in messaging:

				sender_id = messaging_event['sender']['id']
				recipient_id = messaging_event['recipient']['id']

				# Handling get_started response
				if messaging_event.get('postback'):
					if messaging_event['postback'].get('title') == 'Get Started':
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": welcome_message}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})
						response2 = requests.post(fb_api,params=token_dict, json={"recipient":{"id":sender_id}, "messaging_type": "RESPONSE","message":{"text": "You can ask me about DigiSkills Training program.","quick_replies":[{"content_type":"text","title":"Next","payload":"nigga clicked next"}]}})
						#print("quick reply get started", response2)

				elif messaging_event.get('message'):
					if messaging_event['message'].get('quick_reply'):
						# Handling 'next' quick_reply
						if messaging_event['message']['quick_reply'].get('payload') == 'nigga clicked next':
							response = requests.post(fb_api,params=token_dict, json={"message": {"text": next_message}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})
							response2 = requests.post(fb_api,params=token_dict, json={"recipient":{"id": sender_id}, "messaging_type": "RESPONSE","message":{"text": "You can also search your query through given cards & buttons below. \n👇👇👇.","quick_replies":[{"content_type":"text","title":"Continue 🤖","payload":"nigga clicked continue1"}]}})

						# Handling first 'continue' quick_reply
						elif messaging_event['message']['quick_reply'].get('payload') == 'nigga clicked continue1':
							response = requests.post(fb_api,params=token_dict, json={"recipient":{"id": sender_id},"messaging_type": "RESPONSE","message":{"attachment":{"type":"image","payload":{"url":"https://i.ibb.co/NY5rf39/first-image.png","is_reusable":True}}}})
							response2 = requests.post(fb_api,params=token_dict, json={"recipient":{"id": sender_id}, "messaging_type": "RESPONSE","message":{"text": "👇👇👇","quick_replies":[{"content_type":"text","title":"Continue 🤖","payload":"nigga clicked continue2"}]}})

						# Handling second 'continue' quick_reply
						elif messaging_event['message']['quick_reply'].get('payload') == 'nigga clicked continue2':
							response = requests.post(fb_api,params=token_dict, json={"message": {"text": "You can find your queries here 🤗 \nPlease swipe left and right \n👈👉"}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})
							print("continue2 text", response)
							response2 = requests.post(fb_api,params=token_dict, json={"recipient":{"id":sender_id},"message":{"attachment":{"type":"template","payload":{"template_type":"generic","elements":[{"title":"DigiSkills","image_url":"https://i.ibb.co/qypcyYQ/Digiskills.jpg","subtitle":"This section will tell you about DigiSkills training program\n👇👇👇","buttons":[{"type":"postback","payload":"stupid ass nigga asked what is digiskills","title":"What is DigiSkills?"},{"type":"postback","title":"Type of Program","payload":"nigga asked type of program"},{"type":"postback","title":"Benefits of Program","payload":"nigga asked benefits of program"}]},{"title":"Freelancing","image_url":"https://i.ibb.co/WgphLjx/freelance.jpg","subtitle":"This section will tell you the scope of Freelancing after any course\n👇👇👇","buttons":[{"type":"postback","title":"Scope of Courses?","payload":"freelance.scope"},{"type":"postback","title":"How can I get Work?","payload":"freelance.work"},{"type":"postback","title":"Do you Offer Jobs?","payload":"freelance.jobs"}]},{"title":"Motivation","image_url":"https://i.ibb.co/FHk5ttP/motivation.jpg","subtitle":"This section will make you understand the scope of offered courses\n👇👇👇","buttons":[{"type":"postback","title":"Certification","payload":"motivation.certification"},{"type":"postback","title":"Studying Procedure","payload":"motivation.procedure"}]},{"title":"Freelancing","image_url":"https://i.ibb.co/WgphLjx/freelance.jpg","subtitle":"This section will tell you the scope of Freelancing after any course\n👇👇👇","buttons":[{"type":"postback","title":"Scope of Courses?","payload":"freelance.scope"},{"type":"postback","title":"How can I get Work?","payload":"freelance.work"},{"type":"postback","title":"Do you Offer Jobs?","payload":"freelance.jobs"}]}]}}}})
							print("continue2 carousel", response2)

					# HANDLE NORMAL MESSAGES HERE
					elif messaging_event['message'].get('text'):
						# HANDLE TEXT MESSAGES
						query = messaging_event['message']['text']
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": "hello"}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})
						#response2 = requests.post(fb_api,params=token_dict, json={"recipient":{"id":sender_id}, "messaging_type": "RESPONSE","message":{"text": "Pick a color:","quick_replies":[{"content_type":"text","title":"Red","payload":"red"},{"content_type":"text","title":"Green", "payload":"green"}]}})
						#print("hello",response)
						#print(response)
						#result = response.json()
						#print(result)
						#return result
						#	bot.send_text_message(sender_id, query)
						#bot.send_video_url(sender_id, "https://www.youtube.com/watch?v=1I-3vJSC-Vo")
						#return jsonify({"messages":[{"text": "Welcome to the Chatfuel Rockets!"},{"text": "What are you up to?"}]})
	return "ok", 200

#@app.route('/', methods=['POST'])
#def send_get_started():
#	get_started_json= {"get_started":{"payload":"some bitch clicked the get started button"}}
#	get_started = requests.post(profile_api,params=token_dict,data = json.dumps(get_started_json), headers={'Content-Type': 'application/json'})
#	print("get_started", get_started)

#@app.route('/', methods=['POST'])
#def persistent_menu():
#	persistent_menu_json = {"persistent_menu":[{"locale":"default","composer_input_disabled":false,"call_to_actions":[{"type":"postback","title":"Talk to an agent","payload":"CARE_HELP"},{"type":"postback","title":"Outfit suggestions","payload":"CURATION"},{"type":"web_url","title":"Shop now","url":"https://www.originalcoastclothing.com/","webview_height_ratio":"full"}]}]}
#	persistent = requests.post(profile_api, params=token_dict, json= persistent_menu_json)

if __name__ == "__main__":
	app.run(port=5000, use_reloader = True)
