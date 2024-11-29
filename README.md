Overview
This project provides APIs for prompt-based services, offering various possibilities. The main features include:

Generating optimal prompts: Only the generated prompt is returned.
Integrating with OpenAI API: A custom API generates a response by sending the prompt to the OpenAI API.

2 .docx files: Contain examples of prompts.
api.py file: Includes 4 APIs with the following functionality

APIs
/ai_api/customer_support
Generates a prompt for customer support and returns it as the response.

/ai_api/summarize_email
Generates a prompt to summarize an email and returns it as the response.

/ai_api/summarize_email_ai_response
Generates a prompt, sends it to the OpenAI API, and returns the AI-generated response.

/ai_api/customer_support_ai_response
Generates a customer support-related prompt, sends it to the OpenAI API, and returns the AI-generated response.


app.py file to start the application using Flask.
