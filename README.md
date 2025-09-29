This project is a FastAPI backend that generates high quality follow up questions based on candidate's responses during interviews.
It uses the OpenAI API to create follow up questions for interviewers.

To run, first install dependencies : "pip install -r requirements.txt"
Then, create a .env file in the root directory, and add your OpenAI api key in the : "OPENAI_API_KEY=your_api_key_here"
To run the application, use the command : "uvicorn app.main:app --reload" The server will start on http://127.0.0.1:

To test, open the interactive Swagger UI page at: http://127.0.0.1:8000/docs
