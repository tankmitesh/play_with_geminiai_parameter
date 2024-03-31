# Play with parameters : Gemini AI 

## Introduction
This project is a cool tool powered by advanced AI called the Gemini AI API. It helps you do three main things: summarize text, answer questions using different settings, and learn about those settings through experiments. It's like having a smart helper that makes understanding and working with text easier.


## Getting Started

### Prerequisites

- Python 3.9
- [Create an account on Gemini AI](https://aistudio.google.com/app/apikey) to obtain your API token.

### Installation

To install the required packages, run the following command:

```bash
pip install -r requirements.txt
```

### API Token

Before running the project, make sure to generate your API token from the Gemini AI website: [Gemini API Token](https://aistudio.google.com/app/apikey). Once obtained, create a file named `.env` in the root directory and add your token like this:

```env
GOOGLE_API_KEY = your_api_token_here
```

### Running the Application

Execute the following command to run the main file:

```bash
streamlit run run.py
```

This will start the generative AI application using the Gemini AI API.

## Project Structure

- **`requirements.txt`**: Contains the list of Python packages required for the project.
- **`.env`**: Configuration file to store sensitive information, like the Gemini API token.
- **`run.py`**: The main file to execute the generative AI application.
- **`data_generation`**: This file contains LLM text generation function and streamlit based frontend generation code.
- **`prompt_template`**: Contains summary, question and code analysis based prompt for text generation.  


## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Gemini AI](https://gemini.google.com/app) for providing the powerful generative AI API.

---

