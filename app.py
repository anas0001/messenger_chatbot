# imports
import os, sys, requests, json
from flask import Flask, request, jsonify

app = Flask('My echo bot')

# the verification token is a string that is saved in the Facebook app. The webhook will return the same string to the app (through verify method in this code). In this way, the app will verify that the webhook is valid.
VERIFICATION_TOKEN = "hello"
# page access token is probably an index number for the app. Webhook will verify that it is connected to the right app with this page access token.
PAGE_ACCESS_TOKEN = 'EAAg4f5ZBJPCwBACZBIOH5xDydyb4utfDO7sFuG2hChwCewqppbHYux2KrfExxtlz7wiEeYAaWUlZAgZBgfBtCoxHixH0ZAwer7NGHQG3nLTdsrkZCQTJbO33gT61GcpVmMcFagBbBPm7we5NZCaNlqobTeh85S6LemDHiJ800EibFMUtl58IQZA4YA3VTAC5qkEZD'
token_dict = {"access_token": PAGE_ACCESS_TOKEN}

# different functionalities of chatbot require calling different Facebook APIs.
# to send message, quick replies and galleries etc. we call the facebook graph messages API.
fb_api = "https://graph.facebook.com/v4.0/me/messages"
# to get the user's details, such as name, profile picture, location etc. we use facebook graph messenger profile API.
profile_api = "https://graph.facebook.com/v4.0/me/messenger_profile"
# this is a generic link for facebook graph API. It is useless as it is. I have concetenated links with it to use for myself in the code.
psid_url = "https://graph.facebook.com/"

# These are just the strings of messages that are returned to the user.
welcome_message = "Get Started clicked. Go fun yourself. ASSALAM-U-ALAIKUM 🙂\n\n"

next_message = "⚠⚠⚠\nIf you want to chat with a Human just go to Menu with text field of Messenger and click \"Live Chat\" 📱"

what_is_digiskills = "👇👇👇\n\nDigiSkills Training Program:\n\n✔ Pakistan’s 1st Online\nTraining Program🙌\n\nGoal:\n\n✔ To empower the youth\nwith skills for\nFREELANCE market.\n\nNumber of Courses:\n\n✔ Multiple courses\navailable online.📚\n\nLanguage of Courses:\n\n✔ Mix of Urdu-English\nlanguage to facilitate\nPakistani audience."
type_of_program = "👇👇👇\nDigiSkills Training Program\n\n✔Initiative by Government of Pakistan\n\n✔Spearheaded by Ministry of IT & Telecom through Ignite\n\n✔Executed by Virtual University of Pakistan."
benefits_of_program = "👇👇👇\nBenefits\n\n✔Enhance/learn skills that\nare in-demand in FREELANCE market.\n\n✔EARN without looking for a job.💵"
scope_of_courses = "👇👇👇\n\nEven freelancers can join DigiSkill Training Program to,\n\n✔ Learn new skills to make more money.💵💵\n\n✔ Enhance freelancing portfolio by learning from experienced freelancers and experts.💯\n\nThis course will definitely offer something new and helpful to existing freelancers."
freelance_work = "👇👇👇\n\nAfter this program trainees:\n\n✔ Would have new set of skills.\n\n✔ Can make online profile on any freelance marketplace.\n\n✔ Can find jobs online through freelancing platforms.\n\nCoaches will help you in creating profile and bidding for the projects in freelance markets.💲💲"
freelance_jobs = "👇👇👇\n\nThis program will NOT offer jobs to trainees, rather:\n\n✔ It is to train people for skills that are in demand.☺\n\n✔ Enable them to get projects from freelance markets.🏢"
motivation_cert = "👇👇👇\n\nCertificate:\n\nYES, you will get e-Certificate on completion of course.🏆🎓\n\nIssued by - The Virtual University of Pakistan."
motivation_proc = "👇👇👇\n\nStudy Procedure:\n\n✔ All content for each module will be available on “DigiSkills Online Learning Platform”.😊\n\n✔ You can self-pace the training.\n\n✔ You can follow announced timetable on Portal📖"
training_enroll = "👇👇👇\n\nEnrollment Procedure:\n\n1- Sign up by visiting http://DigiSkills.pk/\n\n2- Enroll in 2 courses of your CHOICE.☺\n\nNote:\n\n✔ Enrollment will open one month prior to the commencement of each upcoming batch.\n\n✔ Freelancing is MANDATORY (for first time trainees)‼"
training_content = "👇👇👇\n\nThe content and videos of each week will be made available on Respective:\n\nMonday by 10AM📅🕙"
courses_training = "👇👇👇\n\nOnline Training Program\n\nStep 1: Sign-up👍\n\nStep 2: Enroll the courses you want.👍\n\nDigiSkills Online Learning Management System\n\n✔All content you are enrolled in will be available\n✔Access it from anywhere\n✔Need a computer with internet\n\nTimetable\n\nSelf-pace or follow the announced timetable 😊"
courses_questions_continue = "✔ Interfaces are available where you can ask questions.\n\n1: Discussion boards📄:\n\nIf you are an enrolled trainee then visit discussion board of LMS to:\n\n- Post your query\n- Ask question\n- Help other trainees by commenting on their queries\n- See previous queries related to that specific topic\n\n2: Online support📶:\n\nYou can ask:\n\n- general queries related to LMS\n- Course\n- Other matters related to DigiSkills.pk\n\n3: Mobile phone number📞:\n- Call on +92 311-111-3444"
courses_details = "👇👇👇\n\nThere are 10 courses that are being offered in this program:📚\n\n1. Freelancing\n2. E-Commerce Management\n3. Creative Writing\n4. Graphics Design\n5. QuickBooks\n6.	WordPress\n7. AutoCAD\n8. Search Engine Optimization(SEO)\n9. Digital Marketing\n10. Digital Literacy"
requirements_technical = "👇👇👇\n\nAll you need is:\n\n✔ Stable internet connection📶\n\n✔ Working computer (Desktop or laptop). 💻\n\nNote:\n\nTraining on phone calls ☎ is NOT available.❌"
requirements_educational = "👇👇👇\n\nEducational requirement:\n\nAnyone who can,\n✔ Understand English.\n✔ Read.\n✔ Write.\n\nBuild your future as a FREELANCER!☺"
batches_next = "👇👇👇\n\nEnrollments will start from: November 01, 2018📅\n\nTraining will start from: December 01, 2018📅"
batches_limits = "👇👇👇\n\nCourses Offered📚:\n✔ 10 courses\n\nCourse per Batch:\n✔ Maximum 2 courses.\n✔ For all courses, training can be done in 5 batches.\n\nLimit Reason:\n✔ Trainee gets the maximum value out of the courses.\n✔ Actively participates in discussions, coaching and assignments."
questions_signup = "👇👇👇\n\nTo Signup:\n\n✔ Visit:\n\n http://DigiSkills.pk/ It’s completely FREE!🆓"
questions_courses = "👇👇👇\n\nThe upcoming courses are not being offered currently.\n\n✔ To enroll wait for the batch they are offered in.\n\n✔ Signup to get notified.🔔"
questions_selection = "👇👇👇\n\nCourse selection depends on:\n✔ Interest\n✔ Previous education (Some extent)\n\nCourses:\n✔ All courses are IMPORTANT‼\n✔ Freelancing course is MANDATORY‼\n✔ Choose a course that excited you.😄\n✔ Introduction and learning outcomes are available on web portal."
video_error1 = "👇👇👇\n\nError Reason:\n\nTab navigation is disabled, and a cross sign is being displayed if you try to click the tabs.❌\n\n"
video_error2 = "Watch Course Content STEPS:\n\n1. Login to LMS account\n2. Select your course from “My Courses”\n3.  Open the “Course Website”\n4. Click on topic to be redirected to “Topic Info” tab\n5. Click “Next”(Most right side of page)\n6. Solve any Pre-assessment if any.\n7. Click “Next” to be redirected to video tab.\n8.  Watch the video.\n\nNote : Click the NEXT button to see completion status(Tick)✔ or it will remain incomplete(cross)❌."
password_error = "👇👇👇\n\nReset Password:\n\n✔ Click “Forgot Password” link in “Sign In” page and Follow Instruction.\n\n✔ You can also contact support team using CONTACT US interface."
access_material_error = "👇👇👇\n\nProblem accessing material?\n\nStudy Material:\n\nCourse related material will be accessible after the start of the batch.📚\n\nNotification:\n\nSign up to get notified once the batch starts.🔔"
previous_material_error = "👇👇👇\n\nYES, you can access all previous material missed.\n\nLectures are offered on weekly basis.📅"
activation_error = "👇👇👇\n\nFollow these steps for account activation.\n\n✔ Sign in with your registered Email Address and Password.\n\n✔ Request activation email to activate your account."

# In order to show a message, quick reply or gallery, we have to send JSONs to our app. Below is the complete json to show the main gallery in the Digiskills chatbot.
carousel_json = {"message":{"attachment":{"type":"template","payload":{"template_type":"generic","elements":[{"title":"DigiSkills","image_url":"https://i.ibb.co/qypcyYQ/Digiskills.jpg","subtitle":"This section will tell you about DigiSkills training program\n👇👇👇","buttons":[{"type":"postback","payload":"stupid ass nigga asked what is digiskills","title":"What is DigiSkills?"},{"type":"postback","title":"Type of Program","payload":"nigga asked type of program"},{"type":"postback","title":"Benefits of Program","payload":"nigga asked benefits of program"}]},{"title":"Freelancing","image_url":"https://i.ibb.co/WgphLjx/freelance.jpg","subtitle":"This section will tell you the scope of Freelancing after any course\n👇👇👇","buttons":[{"type":"postback","title":"Scope of Courses?","payload":"freelance.scope"},{"type":"postback","title":"How can I get Work?","payload":"freelance.work"},{"type":"postback","title":"Do you Offer Jobs?","payload":"freelance.jobs"}]},{"title":"Motivation","image_url":"https://i.ibb.co/FHk5ttP/motivation.jpg","subtitle":"This section will make you understand the scope of offered courses\n👇👇👇","buttons":[{"type":"postback","title":"Certification","payload":"motivation.certification"},{"type":"postback","title":"Studying Procedure","payload":"motivation.procedure"}]},{"title":"Start Training","image_url":"https://i.ibb.co/hcB3YJc/Start-training.jpg","subtitle":"This section will tell you about course enrollment & fee structure\n👇👇👇","buttons":[{"type":"postback","title":"Enroll Courses","payload":"training.enroll"},{"type":"postback","title":"Fee Structure","payload":"training.fee"},{"type":"postback","title":"Content Availability","payload":"training.content"}]},{"title":"Courses","image_url":"https://i.ibb.co/G0rCdmS/courses.png","subtitle":"This section will help you with how you will interact with offered cources?\n👇👇👇","buttons":[{"type":"postback","title":"How to get Training?","payload":"courses.training"},{"type":"postback","title":"Can I ask Questions?","payload":"courses.questions"},{"type":"postback","title":"Course Details?","payload":"courses.details"}]},{"title":"Requirements","image_url":"https://i.ibb.co/KzG0Rjs/requirements.jpg","subtitle":"This section will help you with the requirement for having this course.\n👇👇👇","buttons":[{"type":"postback","title":"Technical","payload":"requirements.technical"},{"type":"postback","title":"Educational","payload":"requirements.educational"}]},{"title":"Batches","image_url":"https://i.ibb.co/wMhqDxc/batch.jpg","subtitle":"This section will tell you about Details of batches\n👇👇👇","buttons":[{"type":"postback","title":"Next Batch","payload":"batches.next"},{"type":"postback","title":"Course Limits","payload":"batches.limits"}]},{"title":"Error Support","image_url":"https://i.ibb.co/X2dqxmY/error-support.jpg","subtitle":"This section will help you to figure out the solution of your related error\n👇👇👇","buttons":[{"type":"postback","title":"Error Support","payload":"error support"}]},{"title":"Other Questions","image_url":"https://i.ibb.co/gF1mCjP/other-question.jpg","subtitle":"More Questions","buttons":[{"type":"postback","title":"How can I signup?","payload":"questions.signup"},{"type":"postback","title":"Upcoming Courses?","payload":"questions.courses"},{"type":"postback","title":"Course Selection?","payload":"questions.selection"}]},{"title":"Live Chat","image_url":"https://i.ibb.co/D4zDSXx/live-chat.jpg","subtitle":"If you want to interact with a human operator please click below\n👇👇👇","buttons":[{"type":"postback","title":"Live Chat","payload":"live chat"}]}]}}}}

#error_json = {"recipient":{"id":sender_id},"message":{"attachment":{"type":"template","payload":{"template_type":"generic","elements":[{"title":"Video Error","image_url":"https://i.ibb.co/LRSRdj4/video-error.png","subtitle":" ","buttons":[{"type":"postback","payload":"stupid ass nigga unable to load video","title":"Unable to Load Video"}]},{"title":"Sign In Error","image_url":"https://i.ibb.co/3cYJYD6/signinerror.png","subtitle":" ","buttons":[{"type":"postback","title":"Forgot Password?","payload":"stupid ass nigga forgot his password"}]},{"title":"Enrollment","image_url":"https://i.ibb.co/FHk5ttP/motivation.jpg","subtitle":" ","buttons":[{"type":"postback","title":"Access Material?","payload":"stupid ass nigga not accessing material"},{"type":"postback","title":"Previous Material?","payload":"stupid ass nigga not accessing previous material"}]},{"title":"Activation Error","image_url":"https://i.ibb.co/BCzgsTR/activation.png","subtitle":" ","buttons":[{"type":"postback","title":"Activate Account?","payload":"nigga dont know how to activate account"}]}]}}}}

# the verify methods is used only once. it is used to verify that the webhook is valid and the facebook app
# is connected to the right webhook.

# this code is commented because it is not needed after running the webhook for the first time. It's purpose is to only verify that the webhook is valid. It can be uncommented and there still would be no change in anything because it has served it's purpose.
"""@app.route('/', methods=['GET'])
def verify():
	if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
		if not request.args.get("hub.verify_token") == VERIFICATION_TOKEN:
			return "Verification token mismatch", 403
		return request.args["hub.challenge"], 200
	return "Hello world", 200"""

# this is the main method which deals with all the user inputs and chatbot responses.
@app.route('/', methods=['POST'])
def webhook():
	# this print statement checks what input has been placed by the user. It is here for debugging purposes only.
	print("start-----------------------------------------------------------------------------------------------")
	#print(request.data)
	print("end-----------------------------------------------------------------------------------------------")

	# this line of code extracts the json out of the user input.
	data = request.get_json()

	""" below lines of commented code are my attempts at enabling the 'get started' button and the 'persistent menu'. These codes are also needed to be run once, once they run, they are no longer needed. One or two lines in this code are probably wrong, and I don't remember anymore which one, so you'll have to figure it out yourself"""
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


	# below lines of code are traversing through the json which our code/webhook received from the user.
	if data['object'] == "page":
		entries = data['entry']

		for entry in entries:
			messaging = entry['messaging']

			for messaging_event in messaging:

				# getting the sender ID
				sender_id = messaging_event['sender']['id']
				print("sender_id-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
				print(sender_id)
				print("id-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
				# getting the receiver ID
				recipient_id = messaging_event['recipient']['id']

				# using a GET request to extract the user's information. In the below lines of code, we get the name of the user. Now, we can call the user by his name.
				#print("++++++++++++++++++++++++++++++sender ID:", sender_id)
				response = requests.get(psid_url+sender_id + "?fields=name&access_token=" + PAGE_ACCESS_TOKEN)
				#print("------------------------------response------------------------------")
				#print(response)
				user_json = json.loads(response.content)
				#print("------------------------------user_json------------------------------")
				#print(user_json)
				user_name = user_json["name"]

				# this is the json for another gallery
				error_json = {"recipient":{"id":sender_id},"message":{"attachment":{"type":"template","payload":{"template_type":"generic","elements":[{"title":"Video Error","image_url":"https://i.ibb.co/LRSRdj4/video-error.png","subtitle":" ","buttons":[{"type":"postback","payload":"stupid ass nigga unable to load video","title":"Unable to Load Video"}]},{"title":"Sign In Error","image_url":"https://i.ibb.co/3cYJYD6/signinerror.png","subtitle":" ","buttons":[{"type":"postback","title":"Forgot Password?","payload":"stupid ass nigga forgot his password"}]},{"title":"Enrollment","image_url":"https://i.ibb.co/KLH5THd/enrollment.png","subtitle":" ","buttons":[{"type":"postback","title":"Access Material?","payload":"stupid ass nigga not accessing material"},{"type":"postback","title":"Previous Material?","payload":"stupid ass nigga not accessing previous material"}]},{"title":"Activation Error","image_url":"https://i.ibb.co/BCzgsTR/activation.png","subtitle":" ","buttons":[{"type":"postback","title":"Activate Account?","payload":"nigga dont know how to activate account"}]}]}}}}

				if messaging_event.get('postback'):
					# Handling get_started response
					if messaging_event['postback'].get('payload') == 'some bitch clicked the get started button':
						welcome_msg(sender_id, niggas_name = user_name)
						return "ok", 200
						#print("quick reply get started", response2)

					#--------------""" Handling Persistent Menu """--------------#
					# Handling Restart button
					elif messaging_event['postback'].get('payload') == 'stupid ass nigga had the audacity to restart the bot':
						welcome_msg(sender_id, niggas_name = user_name)
						return "ok", 200

					# Handling Live Chat button
					elif messaging_event['postback'].get('payload') == 'stupid ass nigga asking for a real human being to talk':
						gen_carousel(id)
						return "ok", 200

					#--------------""" Handling all carousel buttons responses """--------------#
					# Handling Digiskills Gallery buttons response
					elif messaging_event['postback'].get('payload') == 'stupid ass nigga asked what is digiskills':
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": what_is_digiskills}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})

					elif messaging_event['postback'].get('payload') == 'nigga asked type of program':
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": type_of_program}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})

					elif messaging_event['postback'].get('payload') == 'nigga asked benefits of program':
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": benefits_of_program}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})

					# Handling Freelancing Gallery buttons response
					elif messaging_event['postback'].get('payload') == 'freelance.scope':
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": scope_of_courses}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})

					elif messaging_event['postback'].get('payload') == 'freelance.work':
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": freelance_work}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})

					elif messaging_event['postback'].get('payload') == 'freelance.jobs':
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": freelance_jobs}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})

					# Handling Motivation Gallery buttons response
					elif messaging_event['postback'].get('payload') == 'motivation.certification':
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": motivation_cert}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})

					elif messaging_event['postback'].get('payload') == 'motivation.procedure':
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": motivation_proc}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})

					# Handling Start Training Gallery buttons response
					elif messaging_event['postback'].get('payload') == 'training.enroll':
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": training_enroll}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})

					elif messaging_event['postback'].get('payload') == 'training.fee':
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": "👇👇👇\n\n💯FREE!! 😊\nJust signup and start training!"}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})

					elif messaging_event['postback'].get('payload') == 'training.content':
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": training_content}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})

					# Handling Courses Gallery buttons response
					elif messaging_event['postback'].get('payload') == 'courses.training':
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": courses_training}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})

					elif messaging_event['postback'].get('payload') == 'courses.questions':
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": "You can ask questions using:\n"}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})
						response2 = requests.post(fb_api,params=token_dict, json={"recipient":{"id": sender_id}, "messaging_type": "RESPONSE","message":{"text": "- DigiSkills Learning Management System\n- Digiskills.pk CONTACT US page.","quick_replies":[{"content_type":"text","title":"Continue Reading 🤖","payload":"nigga clicked continue reading"}]}})
						return "ok", 200

					elif messaging_event['postback'].get('payload') == 'courses.details':
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": courses_details}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})

					# Handling Requirements Gallery buttons response
					elif messaging_event['postback'].get('payload') == 'requirements.technical':
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": requirements_technical}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})

					elif messaging_event['postback'].get('payload') == 'requirements.educational':
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": requirements_educational}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})

					# Handling Requirements Gallery buttons response
					elif messaging_event['postback'].get('payload') == 'batches.next':
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": batches_next}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})

					elif messaging_event['postback'].get('payload') == 'batches.limits':
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": batches_limits}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})

					# Handling Other Courses Gallery buttons response
					elif messaging_event['postback'].get('payload') == 'questions.signup':
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": questions_signup}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})

					elif messaging_event['postback'].get('payload') == 'questions.courses':
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": questions_courses}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})

					elif messaging_event['postback'].get('payload') == 'questions.selection':
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": questions_selection}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})

					# Handling Error Support Gallery buttons response
					elif messaging_event['postback'].get('payload') == 'error support':
						response = requests.post(fb_api,params=token_dict, json=error_json)
						response2 = requests.post(fb_api,params=token_dict, json={"recipient":{"id": sender_id}, "messaging_type": "RESPONSE","message":{"text": "If you want to go to previous, click Go to Previous\n👇👇👇","quick_replies":[{"content_type":"text","title":"Go To Previous ⏮","payload":"stupid nigga now wanna go to previous carousel"}]}})
						return "ok", 200

					# Handling Error Support Carousel Gallery buttons response
					elif messaging_event['postback'].get('payload') == 'stupid ass nigga unable to load video':
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": video_error1}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})
						response2 = requests.post(fb_api,params=token_dict, json={"recipient":{"id": sender_id}, "messaging_type": "RESPONSE","message":{"text": "Solution:\n\nIn order to navigate, you are required to use NEXT and PREVIOUS buttons. If disabled please wait for few seconds so they become enabled.⏮⏭","quick_replies":[{"content_type":"text","title":"Continue Reading 🤖","payload":"illiterate nigga wanna continue reading to video_error2"}]}})
						return "ok", 200

					elif messaging_event['postback'].get('payload') == 'stupid ass nigga forgot his password':
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": password_error}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})

					elif messaging_event['postback'].get('payload') == 'stupid ass nigga not accessing material':
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": access_material_error}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})

					elif messaging_event['postback'].get('payload') == 'stupid ass nigga not accessing previous material':
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": previous_material_error}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})

					elif messaging_event['postback'].get('payload') == 'nigga dont know how to activate account':
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": activation_error}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})

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

						elif messaging_event['message']['quick_reply'].get('payload') == 'nigga clicked continue reading':
							response = requests.post(fb_api,params=token_dict, json={"message": {"text": courses_questions_continue}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})
							gen_continue_button(sender_id)

						elif messaging_event['message']['quick_reply'].get('payload') == 'nigga clicked generic continue':
							gen_carousel(sender_id)

						elif messaging_event['message']['quick_reply'].get('payload') == 'stupid nigga now wanna go to previous carousel':
							gen_carousel(sender_id)

						elif messaging_event['message']['quick_reply'].get('payload') == 'illiterate nigga wanna continue reading to video_error2':
							response = requests.post(fb_api,params=token_dict, json={"message": {"text": video_error2}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})
							gen_continue_button(sender_id)

					# HANDLE NORMAL MESSAGES HERE
					elif messaging_event['message'].get('text'):
						# HANDLE TEXT MESSAGES
						query = messaging_event['message']['text']
						response = requests.post(fb_api,params=token_dict, json={"message": {"text": "don't talk to me you stupid ass nigga. just stop sending messages. use the buttons. geez"}, "recipient": {"id": sender_id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})

	return "ok", 200

def gen_carousel(id):
	carousel_json['recipient'] = {"id": id}
	response2 = requests.post(fb_api,params=token_dict, json=carousel_json)

def gen_continue_button(id):
	response2 = requests.post(fb_api,params=token_dict, json={"recipient":{"id": id}, "messaging_type": "RESPONSE","message":{"text": "Once you're done reading, please click 'Continue' to see carousels \n👇👇👇","quick_replies":[{"content_type":"text","title":"Continue 🤖","payload":"nigga clicked generic continue"}]}})

def welcome_msg(id, niggas_name = "nigga"):
	response = requests.post(fb_api,params=token_dict, json={"message": {"text": welcome_message + niggas_name + " Nice to meet you. 😊\nDigiSkills Chatbot at your service 🤖"}, "recipient": {"id": id}, "notification_type": "REGULAR", "messaging_type": "RESPONSE"})
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
