# Email Generator
A simple, privacy-friendly AI tool that turns bullet points into complete, natural-sounding emails — powered entirely by a **local LLM (Mistral)** using **Ollama**.
Built with **Python** and **Streamlit**, no OpenAI API or internet connection is required.

## Features
- Converts bullet points into full emails with proper structure and flow
- Choose tone: Professional, Friendly, Persuasive, Apologetic
- Powered by **Mistral (via Ollama)** — runs locally, no API needed
- Clean and responsive UI using Streamlit
- Fully offline & private — no data is sent to third parties

## How to run the app
### Install requirements
Make sure you have Python 3.10+ and Ollama installed.  
```bash
pip install -r requirements.txt
```
### Install Ollama
Visit https://ollama.com and install Ollama for your OS
Then, open a terminal and pull the Mistral model:
```bash
ollama pull mistral
```
### Run the app
In the project directory, run:
```bash
streamlit run main.py
```
Your browser will open automatically with the app UI.

## Why use this?
This tool is great for:
  - Freelancers & VAs writing frequent emails
	- Support agents drafting replies quickly
	-	Anyone who wants to save time and avoid blank page syndrome

## Example input
```bash
- Apologize for delay in delivery
- Mention new estimated delivery date (Friday)
- Offer 10% discount for inconvenience
```

## Contact/support
If you need help setting it up or want a custom version with branding, export options, or email integration — feel free to reach out via LinkedIn or Fiverr.

### Built by
Gabriel Indrei  
[LinkedIn](www.linkedin.com/in/gabriel-indrei-9288909a) 
[Fiverr](https://www.fiverr.com/gabriel_indrei)
