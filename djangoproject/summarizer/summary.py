# import library
import openai

# configure openai to your account 
openai.api_key = "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"

def summarize(text):
	
	# create prompt
	prompt = "Write a concise summary of the following content: \n"
	prompt += text
	
	# ping model and generate a response
	response = openai.Completion.create(
			engine = "text-davinci-003",
			prompt = prompt
	)
	
	# clean up response to just the actual String value and return 
	answer = response["choices"][0]["text"].strip()
	return answer 

########################################################
# you can tinker even further with model settings.     #
# read about your options here                         #
########################################################