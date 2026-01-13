# MScAC Alumni Matchmaker Demo

## Overview
This Streamlit app matches current MScAC students with alumni based on past project experience. It generates suggested alumni matches and a draft email students can send.

## Setup
1. Activate your Python virtual environment:
```bash
source venv/bin/activate   # macOS/Linux
.\venv\Scripts\activate    # Windows
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Ensure the following files are present in the project root:
   - `projects_clean.csv` (or `projects.json`)
   - `projects_embeddings.pkl`
   - `projects_metadata.pkl`
   - `chroma_db/` folder

## Running the Demo
```bash
streamlit run app.py
```

## Notes
- The form requires all fields and the commitment checkbox to be filled.
- The `match_student()` function handles the matching logic internally.
- Populate the form with realistic dummy inputs for testing or screenshots (see below).

## Example Dummy Inputs
| Field | Example Input |
|-------|-----------------------------|
| Name | Alex Chen |
| Status | 1st Year MScAC Student |
| Headline | Interested in NLP and social networks |
| Background | Hi! I have prior experience in Python, some ML courses, and I’m curious about alumni career paths in data science. |
| Request | I'm looking for advice on finding an internship project in NLP and social networks, and connecting with alumni with similar interests. |
| Closing | Looking forward to learning from your experiences! |
| Commitment | Checked |

## Demo Screenshot Flow
1. Fill in the form using the dummy inputs above.
2. Submit the form.
3. Capture screenshots of:
   - The matches list under "🔎 Best Matches"
   - The generated email block under "📧 Email to Alumni"
4. Use these screenshots in the scope document appendix to illustrate the system in action.

## Notes for IT / Future Use
- The system is reproducible: ensure CSV/JSON data and embeddings are present.
- `match_student()` abstracts matching logic; no manual data handling is required.
- Adjust `chroma_db` path in `matcher.py` if running on a different machine.
