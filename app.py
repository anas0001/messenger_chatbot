from pymessenger import Bot
import os, sys, requests, json
from flask import Flask, request, jsonify

app = Flask('My echo bot')

VERIFICATION_TOKEN = "hello"
PAGE_ACCESS_TOKEN = 'EAAg4f5ZBJPCwBACZBIOH5xDydyb4utfDO7sFuG2hChwCewqppbHYux2KrfExxtlz7wiEeYAaWUlZAgZBgfBtCoxHixH0ZAwer7NGHQG3nLTdsrkZCQTJbO33gT61GcpVmMcFagBbBPm7we5NZCaNlqobTeh85S6LemDHiJ800EibFMUtl58IQZA4YA3VTAC5qkEZD'
token_dict = {"access_token": PAGE_ACCESS_TOKEN}
bot = Bot(PAGE_ACCESS_TOKEN)

fb_api = "https://graph.facebook.com/v4.0/me/messages"
profile_api = "https://graph.facebook.com/v4.0/me/messenger_profile"

welcome_message = "Get Started clicked. Go fun yourself. ASSALAM-U-ALAIKUM 🙂\n\n Nigga Nice to meet you. 😊\nDigiSkills Chatbot at your service 🤖"

next_message = "⚠⚠⚠\nIf you want to chat with a Human just go to Menu with text field of Messenger and click \"Live Chat\" 📱"

what_is_digiskills = "👇👇👇\n\nDigiSkills Training Program:\n\n✔ Pakistan’s 1st Online\nTraining Program🙌\n\nGoal:\n\n✔ To empower the youth\nwith skills for\nFREELANCE market.\n\nNumber of Courses:\n\n✔ Multiple courses\navailable online.📚\n\nLanguage of Courses:\n\n✔ Mix of Urdu-English\nlanguage to facilitate\nPakistani audience."

carousel_json = {"message":{"attachment":{"type":"template","payload":{"template_type":"generic","elements":[{"title":"DigiSkills","image_url":"https://i.ibb.co/qypcyYQ/Digiskills.jpg","subtitle":"This section will tell you about DigiSkills training program\n👇👇👇","buttons":[{"type":"postback","payload":"stupid ass nigga asked what is digiskills","title":"What is DigiSkills?"},{"type":"postback","title":"Type of Program","payload":"nigga asked type of program"},{"type":"postback","title":"Benefits of Program","payload":"nigga asked benefits of program"}]},{"title":"Freelancing","image_url":"https://i.ibb.co/WgphLjx/freelance.jpg","subtitle":"This section will tell you the scope of Freelancing after any course\n👇👇👇","buttons":[{"type":"postback","title":"Scope of Courses?","payload":"freelance.scope"},{"type":"postback","title":"How can I get Work?","payload":"freelance.work"},{"type":"postback","title":"Do you Offer Jobs?","payload":"freelance.jobs"}]},{"title":"Motivation","image_url":"https://i.ibb.co/FHk5ttP/motivation.jpg","subtitle":"This section will make you understand the scope of offered courses\n👇👇👇","buttons":[{"type":"postback","title":"Certification","payload":"motivation.certification"},{"type":"postback","title":"Studying Procedure","payload":"motivation.procedure"}]},{"title":"Start Training","image_url":"https://i.ibb.co/hcB3YJc/Start-training.jpg","subtitle":"This section will tell you about course enrollment & fee structure\n👇👇👇","buttons":[{"type":"postback","title":"Enroll Courses","payload":"training.enroll"},{"type":"postback","title":"Fee Structure","payload":"training.fee"},{"type":"postback","title":"Content Availability","payload":"training.content"}]},{"title":"Courses","image_url":"https://i.ibb.co/G0rCdmS/courses.png","subtitle":"This section will help you with how you will interact with offered cources?\n👇👇👇","buttons":[{"type":"postback","title":"How to get Training?","payload":"courses.training"},{"type":"postback","title":"Can I ask Questions?","payload":"courses.questions"},{"type":"postback","title":"Course Details?","payload":"courses.details"}]},{"title":"Requirements","image_url":"https://i.ibb.co/KzG0Rjs/requirements.jpg","subtitle":"This section will help you with the requirement for having this course.\n👇👇👇","buttons":[{"type":"postback","title":"Technical","payload":"requirements.technical"},{"type":"postback","title":"Educational","payload":"requirements.educational"}]},{"title":"Batches","image_url":"https://i.ibb.co/wMhqDxc/batch.jpg","subtitle":"This section will tell you about Details of batches\n👇👇👇","buttons":[{"type":"postback","title":"Next Batch","payload":"batches.next"},{"type":"postback","title":"Course Limits","payload":"batches.limits"}]},{"title":"Error Support","image_url":"https://i.ibb.co/X2dqxmY/error-support.jpg","subtitle":"This section will help you to figure out the solution of your related error\n👇👇👇","buttons":[{"type":"postback","title":"Error Support","payload":"error support"}]},{"title":"Other Questions","image_url":"https://i.ibb.co/gF1mCjP/other-question.jpg","subtitle":"More Questions","buttons":[{"type":"postback","title":"How can I signup?","payload":"questions.signup"},{"type":"postback","title":"Upcoming Courses?","payload":"questions.courses"},{"type":"postback","title":"Course Selection?","payload":"questions.selection"}]},{"title":"Live Chat","image_url":"https://i.ibb.co/D4zDSXx/live-chat.jpg","subtitle":"If you want to interact with a human operator please click below\n👇👇👇","buttons":[{"type":"postback","title":"Live Chat","payload":"live chat"}]}]}}}}

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
	##get_started = requests.post(fb_api,params=token_dict,{"get_started":{"payload":"some bitch clicked the get started button"}})
	######
	######persis_json = {"persistent_menu":[{"locale":"default","composer_input_disabled":False,"call_to_actions":[{"type":"postback","title":"Restart","payload":"stupid ass nigga had the audacity to restart the bot"},{"type":"postback","title":"Live Chat","payload":"stupid ass nigga asking for a real human being to talk"}]}]}
	#persistent_menu_json = {"persistent_menu":[{"locale":"default","composer_input_disabled":False,"call_to_actions":[{"type":"postback","title":"Talk to an agent","payload":"CARE_HELP"},{"type":"postback","title":"Outfit suggestions","payload":"CURATION"},{"type":"web_url","title":"Shop now","url":"https://www.originalcoastclothing.com/","webview_height_ratio":"full"}]}]}
	#####
	#####persistent = requests.post(profile_api, params=token_dict, json= persis_json)
	#####print("persistent-----------------------",persistent)
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

				if messaging_event.get('postback'):
					# Handling get_started response
					if messaging_event['postback'].get('payload') == 'some bitch clicked the get started button':
						welcome_message(sender_id)
						#print("quick reply get started", response2)

					#--------------""" Handling Persistent Menu """--------------#
					# Handling Restart button
					elif messaging_event['postback'].get('payload') == 'stupid ass nigga had the audacity to restart the bot':
						welcome_message(sender_id)

					#--------------""" Handling all carousel buttons responses """--------------#
					# Handling Digiskills Gallery buttons response
					elif messaging_event['postback'].get('payload') == 'stupid ass nigga asked what is digiskills':
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": what_is_digiskills}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})
						gen_continue_button(sender_id)

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
							gen_carousel(sender_id)

						elif messaging_event['message']['quick_reply'].get('payload') == 'nigga clicked generic continue':
							gen_carousel(sender_id)

							"""response2 = requests.post(fb_api,params=token_dict, json={"recipient":{"id":sender_id},"message":{"attachment":{"type":"template","payload":{"template_type":"generic","elements":[{"title":"DigiSkills","image_url":"https://i.ibb.co/qypcyYQ/Digiskills.jpg","subtitle":"This section will tell you about DigiSkills training program\n👇👇👇","buttons":[{"type":"postback","payload":"stupid ass nigga asked what is digiskills","title":"What is DigiSkills?"},{"type":"postback","title":"Type of Program","payload":"nigga asked type of program"},{"type":"postback","title":"Benefits of Program","payload":"nigga asked benefits of program"}]},{"title":"Freelancing","image_url":"https://i.ibb.co/WgphLjx/freelance.jpg","subtitle":"This section will tell you the scope of Freelancing after any course\n👇👇👇","buttons":[{"type":"postback","title":"Scope of Courses?","payload":"freelance.scope"},{"type":"postback","title":"How can I get Work?","payload":"freelance.work"},{"type":"postback","title":"Do you Offer Jobs?","payload":"freelance.jobs"}]},{"title":"Motivation","image_url":"https://i.ibb.co/FHk5ttP/motivation.jpg","subtitle":"This section will make you understand the scope of offered courses\n👇👇👇","buttons":[{"type":"postback","title":"Certification","payload":"motivation.certification"},{"type":"postback","title":"Studying Procedure","payload":"motivation.procedure"}]},{"title":"Start Training","image_url":"https://i.ibb.co/hcB3YJc/Start-training.jpg","subtitle":"This section will tell you about course enrollment & fee structure\n👇👇👇","buttons":[{"type":"postback","title":"Enroll Courses","payload":"training.enroll"},{"type":"postback","title":"Fee Structure","payload":"training.fee"},{"type":"postback","title":"Content Availability","payload":"training.content"}]},{"title":"Courses","image_url":"https://i.ibb.co/G0rCdmS/courses.png","subtitle":"This section will help you with how you will interact with offered cources?\n👇👇👇","buttons":[{"type":"postback","title":"How to get Training?","payload":"courses.training"},{"type":"postback","title":"Can I ask Questions?","payload":"courses.questions"},{"type":"postback","title":"Course Details?","payload":"courses.details"}]},{"title":"Requirements","image_url":"https://i.ibb.co/KzG0Rjs/requirements.jpg","subtitle":"This section will help you with the requirement for having this course.\n👇👇👇","buttons":[{"type":"postback","title":"Technical","payload":"requirements.technical"},{"type":"postback","title":"Educational","payload":"requirements.educational"}]},{"title":"Batches","image_url":"https://i.ibb.co/wMhqDxc/batch.jpg","subtitle":"This section will tell you about Details of batches\n👇👇👇","buttons":[{"type":"postback","title":"Next Batch","payload":"batches.next"},{"type":"postback","title":"Course Limits","payload":"batches.limits"}]},{"title":"Error Support","image_url":"https://i.ibb.co/X2dqxmY/error-support.jpg","subtitle":"This section will help you to figure out the solution of your related error\n👇👇👇","buttons":[{"type":"postback","title":"Error Support","payload":"error support"}]},{"title":"Other Questions","image_url":"https://i.ibb.co/gF1mCjP/other-question.jpg","subtitle":"More Questions","buttons":[{"type":"postback","title":"How can I signup?","payload":"questions.signup"},{"type":"postback","title":"Upcoming Courses?","payload":"questions.courses"},{"type":"postback","title":"Course Selection?","payload":"questions.selection"}]},{"title":"Live Chat","image_url":"https://i.ibb.co/D4zDSXx/live-chat.jpg","subtitle":"If you want to interact with a human operator please click below\n👇👇👇","buttons":[{"type":"postback","title":"Live Chat","payload":"live chat"}]}]}}}})
							print("continue2 carousel", response2)"""

					# HANDLE NORMAL MESSAGES HERE
					elif messaging_event['message'].get('text'):
						# HANDLE TEXT MESSAGES
						query = messaging_event['message']['text']
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": "hello"}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})
						response2 = requests.post(fb_api,params=token_dict, json={"recipient":{"id":sender_id}, "messaging_type": "RESPONSE","message":{"text": "Pick a color:","quick_replies":[{"content_type":"text","title":"Red","payload":"red"},{"content_type":"text","title":"Green", "payload":"green"}]}})
						#print("hello",response)
						#print(response)
						#result = response.json()
						#print(result)
						#return result
						#bot.send_text_message(sender_id, query)
						#bot.send_video_url(sender_id, "https://www.youtube.com/watch?v=1I-3vJSC-Vo")
						#return jsonify({"messages":[{"text": "Welcome to the Chatfuel Rockets!"},{"text": "What are you up to?"}]})
	return "ok", 200

#@app.route('/', methods=['POST'])
def gen_carousel(id):
	carousel_json['recipient'] = {"id": id}
	response2 = requests.post(fb_api,params=token_dict, json=carousel_json)

def gen_continue_button(id):
	response2 = requests.post(fb_api,params=token_dict, json={"recipient":{"id": id}, "messaging_type": "RESPONSE","message":{"text": "Once you're done reading, please click continue to see carousels.","quick_replies":[{"content_type":"text","title":"Continue 🤖","payload":"nigga clicked generic continue"}]}})

def welcome_message(id):
	response = requests.post(fb_api,params=token_dict, json={"message": {"text": welcome_message}, "recipient": {"id": id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})
	response2 = requests.post(fb_api,params=token_dict, json={"recipient":{"id": id}, "messaging_type": "RESPONSE","message":{"text": "You can ask me about DigiSkills Training program.","quick_replies":[{"content_type":"text","title":"Next","payload":"nigga clicked next"}]}})

	#print("continue2 carousel", response2)
#	get_started_json= {"get_started":{"payload":"some bitch clicked the get started button"}}
#	get_started = requests.post(profile_api,params=token_dict,data = json.dumps(get_started_json), headers={'Content-Type': 'application/json'})
#	print("get_started", get_started)

#@app.route('/', methods=['POST'])
#def persistent_menu():
#	persistent_menu_json = {"persistent_menu":[{"locale":"default","composer_input_disabled":false,"call_to_actions":[{"type":"postback","title":"Talk to an agent","payload":"CARE_HELP"},{"type":"postback","title":"Outfit suggestions","payload":"CURATION"},{"type":"web_url","title":"Shop now","url":"https://www.originalcoastclothing.com/","webview_height_ratio":"full"}]}]}
#	persistent = requests.post(profile_api, params=token_dict, json= persistent_menu_json)

if __name__ == "__main__":
	app.run(port=5000, use_reloader = True)
