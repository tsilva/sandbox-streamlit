# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Streamlit application playground. The project uses Conda for environment management and python-dotenv for environment variable configuration.

## Environment Setup

Create and activate the Conda environment:
```bash
conda env create -f environment.yml
conda activate sandbox-streamlit
```

The environment includes Python 3.10, Streamlit, and python-dotenv.

## Running the Application

**Note**: The README references `app.py`, but the actual entry point is `main.py`.

```bash
streamlit run main.py
```

The app runs at `http://localhost:8501` by default.

## Environment Variables

The project uses python-dotenv to load environment variables. Copy `.env.example` to `.env` and configure as needed:
```bash
cp .env.example .env
```

Current environment variables:
- `OPENAI_API_KEY`: OpenAI API key (if integrating with OpenAI services)

## Architecture

This is a simple single-file Streamlit application:
- `main.py`: The main application entry point that loads environment variables and defines the Streamlit UI

## Important Notes

- README.md must be kept up to date with any significant project changes, especially if the main application file name changes or new dependencies are added
