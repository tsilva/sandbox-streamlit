<div align="center">
  <img src="logo.png" alt="sandbox-streamlit" width="512"/>

  [![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
  [![Streamlit](https://img.shields.io/badge/Streamlit-latest-FF4B4B.svg)](https://streamlit.io/)
  [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

  **🎨 A playground for experimenting with Streamlit applications and interactive data visualizations 🚀**
</div>

## Overview

sandbox-streamlit is a minimal development environment for prototyping Streamlit applications. Use it to quickly test ideas, explore Streamlit's capabilities, and build interactive data apps.

## Features

- Pre-configured Conda environment with Python 3.10
- Environment variable management via python-dotenv
- Ready-to-run Streamlit setup

## Quick Start

```bash
# Create and activate the environment
conda env create -f environment.yml
conda activate sandbox-streamlit

# Run the app
streamlit run main.py
```

The app opens at `http://localhost:8501`.

## Installation

### Prerequisites

- [Conda](https://docs.conda.io/en/latest/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/tsilva/sandbox-streamlit.git
   cd sandbox-streamlit
   ```

2. Create the Conda environment:
   ```bash
   conda env create -f environment.yml
   conda activate sandbox-streamlit
   ```

3. Configure environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys if needed
   ```

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `OPENAI_API_KEY` | No | OpenAI API key for AI integrations |

## Project Structure

```
sandbox-streamlit/
├── main.py           # Main Streamlit application
├── environment.yml   # Conda environment configuration
├── .env.example      # Environment variable template
└── CLAUDE.md         # Claude Code instructions
```

## Usage

Modify `main.py` to experiment with Streamlit components:

```python
from dotenv import load_dotenv
load_dotenv()

import streamlit as st

x = st.slider("Select a value")
st.write(x, "squared is", x * x)
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## License

MIT License - see [LICENSE](LICENSE) for details.
