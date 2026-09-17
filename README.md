# AI Productivity Assistant

An AI-powered workplace assistant designed to streamline daily productivity. It helps users generate polished emails, summarize meetings, plan tasks, research topics, and interact with a conversational assistant.

## Overview

This project demonstrates practical GenAI use in a workplace context. The assistant combines strong prompt engineering with clear, user-friendly workflows to support real business tasks.

## Features

- Email generation for professional messages and outreach
- Meeting summarization from raw notes or transcripts
- Task planning and prioritization
- Research assistance for quick background synthesis
- Chatbot interaction for everyday workplace questions
- Responsible AI guardrails and privacy-focused design

## Tech Stack

- Python
- Streamlit
- OpenAI-compatible API or Gemini API
- dotenv-based environment configuration

## Project Structure

- `app.py` — main Streamlit interface
- `assistant_core.py` — AI prompt logic and provider integration
- `requirements.txt` — Python dependencies
- `.env.example` — environment variable template
- `README.md` — project overview and setup guide

## Get Started

1. Clone the repository
2. Create a virtual environment
3. Install dependencies
4. Add your API key in a `.env` file
5. Run the app

### Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

### Run the app

```bash
streamlit run app.py
```

## Environment Variables

Create a `.env` file with one of the following setups:

### OpenAI

```env
AI_PROVIDER=openai
OPENAI_API_KEY=your_key_here
```

### Gemini

```env
AI_PROVIDER=gemini
GEMINI_API_KEY=your_key_here
```

## Ethical Use

This project is built with responsible AI principles in mind:

- Verify generated outputs before sending them
- Be transparent when AI is used in workflows
- Protect sensitive workplace information
- Use AI to augment, not replace, human judgment

## Future Enhancements

- Add authentication and team workspaces
- Integrate with Gmail or calendars
- Save user workflows and templates
- Add multilingual support and voice-based summarization
- Support document ingestion from PDFs and notes

## License

This project is intended for educational and demonstration purposes.
