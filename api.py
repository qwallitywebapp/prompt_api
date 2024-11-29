from flask import Flask, request, jsonify
import openai
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv('data.env')
openai_key = os.getenv('api_key')
openai.api_key = openai_key


@app.route('/ai_api/customer_support', methods=['POST'])
def customer_support_response():
    data = request.get_json(force=True)
    customer_request = data['customer_request']
    prompt = f"""Generate a professional, polite, and clear response to the following customer inquiry:
    **Customer Inquiry:** {customer_request}

    Ensure that the response is:
    1. **Clear and concise** -Avoid jargon and provide simple explanations.
    2. **Empathetic and polite** - Acknowledge the customer's concern and maintain a professional tone.
    3. **Actionable** - Offer steps the customer can take next if applicable (e.g., contact support, dispute a charge).
    4. **Aligned with company policies** - The response must be fully consistent with the company's policies on handling the specific issue.

    Example Response: 'Thank you for your inquiry regarding the recent fee charged to your account.
    According to our records, your account was charged an overdraft fee on [Date] due to a transaction that exceeded your available balance.
    Our overdraft protection policy allows for a fee to be charged when the balance falls below a certain threshold. 
    Please note that this fee is [Amount]. If you believe this fee was charged in error, please contact our support team to discuss the matter further. 
    We are here to help.'"
    """
  
    return jsonify({"task_name": "incident response example", "prompt": prompt})


@app.route('/ai_api/summarize_email', methods=['POST'])
def email_summarization():
    data = request.get_json(force=True)
    email_subject = data['email_subject']
    email_content = data['email_content']
    prompt = f"""You are an email summarization assistant. Your task is to analyze the content of the email provided below and produce a concise summary in 2-3 sentences. 
    Ensure the summary captures the email's main purpose, key details, and any action items or requests. Use a formal and professional tone.
    Email Subject: {email_subject}
    Email Content: {email_content} """  
    return jsonify({"task_name": "summarize_email", "prompt": prompt})


@app.route('/ai_api/summarize_email_ai_response', methods=['POST'])
def email_summarization_with_ai():
    data = request.get_json(force=True)
    email_subject = data['email_subject']
    email_content = data['email_content']
    prompt = f"""You are an email summarization assistant. Your task is to analyze the content of the email provided below and produce a concise summary in 2-3 sentences. 
    Ensure the summary captures the email's main purpose, key details, and any action items or requests. Use a formal and professional tone.
    Email Subject: {email_subject}
    Email Content: {email_content} """
    response = openai.ChatCompletion.create(
        model="gpt-4o",  # Or "gpt-3.5-turbo" for a cheaper alternative
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}],  # Correctly combine the lists
        max_tokens=200,  # Limit the response length
        temperature=0.5)  # Controls the randomness of the output
    return jsonify({"response": response})



@app.route('/ai_api/customer_support_ai_response', methods=['POST'])
def customer_support_response_with_ai():
    data = request.get_json(force=True)
    customer_request = data['customer_request']
    prompt = f"""Generate a professional, polite, and clear response to the following customer inquiry:
    **Customer Inquiry:** {customer_request}

    Ensure that the response is:
    1. **Clear and concise** -Avoid jargon and provide simple explanations.
    2. **Empathetic and polite** - Acknowledge the customer's concern and maintain a professional tone.
    3. **Actionable** - Offer steps the customer can take next if applicable (e.g., contact support, dispute a charge).
    4. **Aligned with company policies** - The response must be fully consistent with the company's policies on handling the specific issue.

    Example Response: 'Thank you for your inquiry regarding the recent fee charged to your account.
    According to our records, your account was charged an overdraft fee on [Date] due to a transaction that exceeded your available balance.
    Our overdraft protection policy allows for a fee to be charged when the balance falls below a certain threshold. 
    Please note that this fee is [Amount]. If you believe this fee was charged in error, please contact our support team to discuss the matter further. 
    We are here to help.'"
    """
    response = openai.ChatCompletion.create(
        model="gpt-4o",  # Or "gpt-3.5-turbo" for a cheaper alternative
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}],  # Correctly combine the lists
        max_tokens=200,  # Limit the response length
        temperature=0.5)  # Controls the randomness of the output
    return jsonify({"response": response})
