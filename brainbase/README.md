# BrainBase

## Description
BrainBase is a powerful software development project that integrates with the Amadeus API and OpenAI tools to build intelligent chatbot functionalities. It provides a seamless way to interact with travel data and leverage AI for enhanced user experiences.

## Features
- Integration with the Amadeus API for travel data.
- OpenAI-powered chatbot for natural language interactions.
- Modular and extensible architecture.
- Easy-to-use configuration and setup.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/brianthemessiah/brainbase.git
   ```
2. Navigate to the project directory:
   ```bash
   cd brainbase
   ```
3. Install the dependencies:
   ```bash
   poetry install
   ```

## Usage
To start the flask application, run:
```bash
python app.py
```

To start the front end app, run:
```bash
npm run dev
```

## Configuration
1. Obtain API keys for Amadeus and OpenAI.
2. Create a `.env` file in the root directory and add the following:
   ```
   AMADUES_URL = 'https://test.api.amadeus.com/v2'
   AMADEUS_CLIENT_ID=your_amadeus_api_key
   AMADEUS_CLIENT_SECRET=your_amadeus_secret_key
   OPENAI_API_KEY=your_openai_api_key
   ```

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
