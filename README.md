# InterviewCoach — AI Mock Interview Agent

Practice job interviews with 5 AI-generated questions tailored to your role and level. Get scored feedback on every answer plus a final performance report.

## Features
- Role + level + focus area configuration
- 5 adaptive questions per session
- Per-question scoring: Clarity, Depth, Examples, Relevance
- Model answer reveal
- Final session summary with verdict (Excellent / Good / Needs Improvement / Not Ready)

## Stack
- **Frontend**: React 18, Vite, Tailwind CSS v4, Framer Motion
- **Backend**: FastAPI, Groq SDK (stateful session store)

## Local Development

### Backend
```bash
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn main:app --reload --port 8000
```

### Frontend
```bash
cd frontend
npm install
echo "VITE_API_BASE_URL=http://localhost:8000" > .env
npm run dev
```
