from flask import Flask, redirect, url_for, request, jsonify
import flask
from fillpdf import fillpdfs
from pprint import pprint
# from langchain.llms import Anthropic
from langchain import PromptTemplate, LLMChain
from langchain import OpenAI, ConversationChain, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
import os
from dotenv import load_dotenv
import json

load_dotenv()

app = Flask(__name__)


form_dict = {
    'topmostSubform[0].Page1[0].N12CB[0]': 'Yes',
	'topmostSubform[0].Page1[0].N12CB[1]': 'No',
	'topmostSubform[0].Page1[0].N13ACB[0]': 'Yes',
	'topmostSubform[0].Page1[0].N13ACB[1]': 'No',
	'topmostSubform[0].Page1[0].N13BFLD[0]': 'other countries social credits',
	'topmostSubform[0].Page1[0].N14ACB[0]': 'Yes',
	'topmostSubform[0].Page1[0].N14ACB[1]': 'No',
	'topmostSubform[0].Page1[0].N14BCB[0]': 'Off',
	'topmostSubform[0].Page1[0].N14BFLD1[0]': 'B MONTH',
	'topmostSubform[0].Page1[0].N14BFLD2[0]': 'B YEAR',
	'topmostSubform[0].Page1[0].N14CFLD1[0]': 'c month',
	'topmostSubform[0].Page1[0].N14CFLD2[0]': 'c YEAR',
	'topmostSubform[0].Page1[0].N1FLD[0]': 'name',
	'topmostSubform[0].Page1[0].N2FLD[0]': 'SSNss',
	'topmostSubform[0].Page1[0].N3CB[0]': 'Female',
	'topmostSubform[0].Page1[0].N3CB[1]': 'Male',
	'topmostSubform[0].Page1[0].N4SpeakFLD[0]': 'speak lang',
	'topmostSubform[0].Page1[0].N4WriteFLD[0]': 'write lang',
	'topmostSubform[0].Page1[0].N5AFLD[0]': 'dob',
	'topmostSubform[0].Page1[0].N5BFLD[0]': '5b: name of city',
	'topmostSubform[0].Page1[0].N6ACB[0]': 'Yes',
	'topmostSubform[0].Page1[0].N6ACB[1]': 'No',
	'topmostSubform[0].Page1[0].N6BCB[0]': 'Yes',
	'topmostSubform[0].Page1[0].N6BCB[1]': 'No',
	'topmostSubform[0].Page1[0].N6CFLD[0]': 'Lawful Admission',
	'topmostSubform[0].Page1[0].N7AFLD[0]': 'name if diff ',
	'topmostSubform[0].Page1[0].N7BCB[0]': 'Yes',
	'topmostSubform[0].Page1[0].N7BCB[1]': 'No',
	'topmostSubform[0].Page1[0].N7CFLD[0]': 'other names',
	'topmostSubform[0].Page1[0].N8ACB[0]': 'Yes',
	'topmostSubform[0].Page1[0].N8ACB[1]': 'No',
	'topmostSubform[0].Page1[0].N8BFLD[0]': 'more ssns',
	'topmostSubform[0].Page1[0].N9FLD[0]': 'date for severerity',

	'topmostSubform\\1330\\135\\056Page1\\1330\\135\\056N14CCB\\1330\\135': 'Off',
	'topmostSubform\\1330\\135\\056Page1\\1330\\135\\056TextField1\\1330\\135': ''
 }

q_to_item = {
	'': 'topmostSubform\\1330\\135\\056Page1\\1330\\135\\056TextField1\\1330\\135',
	'5.b: name of city': 'topmostSubform[0].Page1[0].N5BFLD[0]',
	'12b. MONTH': 'topmostSubform[0].Page1[0].N14BFLD1[0]',
	'12b. YEAR': 'topmostSubform[0].Page1[0].N14BFLD2[0]',
	'3. Female': 'topmostSubform[0].Page1[0].N3CB[0]',
	'6.c. Lawful Admission': 'topmostSubform[0].Page1[0].N6CFLD[0]',
	'3. Male': 'topmostSubform[0].Page1[0].N3CB[1]',
	'No': 'topmostSubform[0].Page1[0].N8ACB[1]',
	'Off': 'topmostSubform\\1330\\135\\056Page1\\1330\\135\\056N14CCB\\1330\\135',
	'2. SSN': 'topmostSubform[0].Page1[0].N2FLD[0]',
	'Yes': 'topmostSubform[0].Page1[0].N8ACB[0]',
	'12c. YEAR': 'topmostSubform[0].Page1[0].N14CFLD2[0]',
	'12c. month': 'topmostSubform[0].Page1[0].N14CFLD1[0]',
	'9 date for severerity': 'topmostSubform[0].Page1[0].N9FLD[0]',
	'5.a. dob': 'topmostSubform[0].Page1[0].N5AFLD[0]',
	'8b. more ssns': 'topmostSubform[0].Page1[0].N8BFLD[0]',
	'1. Full Name': 'topmostSubform[0].Page1[0].N1FLD[0]',
	'7a. name if diff ': 'topmostSubform[0].Page1[0].N7AFLD[0]',
	'11.b. other countries social credits': 'topmostSubform[0].Page1[0].N13BFLD[0]',
	'other names': 'topmostSubform[0].Page1[0].N7CFLD[0]',
	'4. speak lang': 'topmostSubform[0].Page1[0].N4SpeakFLD[0]',
	'4. write lang': 'topmostSubform[0].Page1[0].N4WriteFLD[0]'
}
template = """Assistant is a large language model trained by OpenAI.

Assistant is designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, Assistant is able to generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.

Assistant is constantly learning and improving, and its capabilities are constantly evolving. It is able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally, Assistant is able to generate its own text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on a wide range of topics.

Overall, Assistant is a powerful tool that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether you need help with a specific question or just want to have a conversation about a particular topic, Assistant is here to assist.

Human: {question}

Use the information above, fill out the form that you memorized section by section 1-12. Leave out the fields that you do not have answers to or should not fill. Choose No for appropriate fields that you have answers for. Do not include part of the prompt in your answer.

A sample output would look like:

    1.    John Q. Doe

    2.    123-45-6789

    3.    Male

    4.    blank

    5.    (a) January 1, 1970 (b) New York, NY

    6.    (a) Yes

    7.    (a)

(b) Yes (c) John Quincy Doe

    8.    (a) No

    9.    January 1, 2020

    10.    No

    11.    (a) No

    12.    (a) No
	
Assistant:
"""

# prompt = PromptTemplate(template=template, input_variables=["question"])
# llm_chain = LLMChain(prompt=prompt, llm=Anthropic(anthropic_api_key=ANTHROPIC_API_KEY))

@app.route('/',methods = ['POST', 'GET'])
def return_pdf():
	print(request.form.to_dict())
	prompt = PromptTemplate(template=template, input_variables=["question"])

	chatgpt_chain = LLMChain(
		llm=OpenAI(temperature=0), 
		prompt=prompt, 
		verbose=True, 
		memory=ConversationBufferWindowMemory(k=2),
	)
	
	output = chatgpt_chain.predict(question=request.form.to_dict()['prompt'])
	print(output)
	newd = parse_output(output)
	fillpdfs.write_fillable_pdf('newfile.pdf', 'output.pdf', newd)
	res = {
		'ack': 'true'
	}
	return flask.Response(
				str(res), status=500, mimetype='application/json'
			)
    
def parse_output(ins):
	values = ins.split('\n')
	# print(values)
	newd = dict()
	for val in values:
		num = val.split(' ')
		# print(num)
		if num[0] == '1.':
			newd['topmostSubform[0].Page1[0].N1FLD[0]'] = ' '.join(num[1:])
		elif num[0] == '2.':
			newd['topmostSubform[0].Page1[0].N2FLD[0]'] = ' '.join(num[1:])
		elif num[0] == '3.':
			ans = ' '.join(num[1:])
			if 'Female' in ans:
				newd['topmostSubform[0].Page1[0].N3CB[1]'] = 'Female'
		elif num[0] == '4.':
			newd['topmostSubform[0].Page1[0].N4SpeakFLD[0]'] = ' '.join(num[1:])
			newd['topmostSubform[0].Page1[0].N4WriteFLD[0]'] = ' '.join(num[1:])
		elif num[0] == '5.':
			if num[1] == '(a)':
				newd['topmostSubform[0].Page1[0].N5AFLD[0]'] = ' '.join(num[2:5])
			if num[5] == '(b)':
				newd['topmostSubform[0].Page1[0].N5BFLD[0]'] = ' '.join(num[6:])
		elif num[0] == '9.':
			newd['topmostSubform[0].Page1[0].N9FLD[0]'] = ' '.join(num[1:])

	return newd

if __name__ == "__main__":
	app.run()