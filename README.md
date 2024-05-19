# Coach Teddy API

> Call him +1 (316) 669-7437

Coach Teddy is a conversational AI agent specifically designed for startup founders. The agent listens to the problems faced by founders and provides constructive solutions to help them overcome challenges and grow their businesses.

This project provides an API for handling webhook events from the Flyflow platform. It listens for `call_started` events, retrieves the 10 most recent calls for the client number associated with the call, and sets the context of the call to include the call dates, IDs, and transcripts. This context is then used by Coach Teddy to provide personalized guidance and support to the founders.

## Coach Teddy's System Prompt

Coach Teddy operates based on the following system prompt:

```
You are a coach specifically for startup founders. Your job is to listen to their problems and help come up with constructive solutions to those problems. 

Your name is Teddy.

Style Guide 
- Be concise and to the point
- For short thoughts, respond in one sentence or less
- Try to dig into problems and get to the root of the issue
- Only include one idea at a time in your response
- Keep the conversation focused on the founder and their startup  

Guide on how to be a good coach: [coaching guide content]
```

The coaching guide content provides Coach Teddy with principles and techniques for effective coaching, ensuring that the agent provides valuable support to the founders.

## Setup

1. Clone the repository:

```bash
git clone https://github.com/carlcortright/coach-teddy.git
cd coach-teddy
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your Flyflow API key:

```
FLYFLOW_API_KEY=your_api_key
```

5. Run the Flask server:

```bash
python app.py
```

The API will be available at `http://localhost:8080/webhook`.

## Deployment

The project includes a `Dockerfile` for building a Docker image and a `cloudbuild.yaml` file for deploying the API to Google Cloud Platform.

To build and deploy the API:

1. Ensure you have the Google Cloud SDK installed and configured.

2. Run the following command to initiate the Cloud Build process:

```bash
gcloud builds submit --config cloudbuild.yaml
```

The API will be built and deployed to Google Container Registry.

## Contributing

If you'd like to contribute to the Coach Teddy API project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

Please ensure that your code adheres to the project's coding conventions and includes appropriate tests and documentation.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to customize the README file further based on your specific project requirements and add any additional sections or information that you think would be helpful for users and contributors.