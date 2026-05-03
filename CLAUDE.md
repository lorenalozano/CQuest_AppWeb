# CQuest — Project Instructions for Claude Code

This file contains the permanent instructions for the CQuest project.
Always follow these rules when creating or modifying the repository.

This is a production-ready educational coding platform for children.
No placeholders or TODOs are allowed.

# CQuest — AI Coding Learning Platform

This is a gamified educational web application that teaches C programming to children (12 years old) through a visual, interactive and AI-assisted environment.

The experience combines:
- Duolingo-style progression (worlds and levels)
- CodeCombat-style gamification
- Visual Studio Code-like coding environment
- AI tutor assistance

----------------------------------------------------

## CORE PRINCIPLES

- The app must always be production-ready
- No placeholders or TODOs are allowed
- All features must be fully implemented
- The system must run with: docker-compose up
- The UX must be designed for children (12 years old)
- The interface must be simple, visual and encouraging

----------------------------------------------------

## TECH STACK (DO NOT CHANGE)

Frontend:
- Next.js
- React
- TailwindCSS
- Monaco Editor (VS Code-like experience)

Backend:
- Python (FastAPI)
- SQLite
- Docker-based GCC sandbox for C execution
- OpenAI API for AI tutor features

DevOps:
- docker-compose
- Docker containers for frontend and backend

----------------------------------------------------

## APPLICATION ARCHITECTURE

Frontend responsibilities:
- Visual IDE (VS Code-like)
- Lesson navigation (world map)
- User progress UI
- Code editor (Monaco)

Backend responsibilities:
- Execute C code safely in Docker sandbox
- Store users, progress and lessons
- Provide AI endpoints
- Evaluate exercises

AI system:
- Hint generation
- Error explanation
- Exercise generation

----------------------------------------------------

## AI FEATURES

The system must include:

1. HINT GENERATION
- Provide small hints only
- Never give full solutions

2. ERROR EXPLANATION
- Explain compiler errors in simple language
- Always use encouraging tone

3. EXERCISE GENERATION
- Generate new beginner-friendly C exercises dynamically

----------------------------------------------------

## GAMIFICATION RULES

- XP system is mandatory
- Worlds unlock sequentially
- Each world contains multiple lessons
- Final project unlocks next world
- Badges for completed worlds

----------------------------------------------------

## CODE EXECUTION SAFETY

- All C code must run inside Docker sandbox
- Must enforce:
  - timeout (3 seconds)
  - no filesystem access
  - memory limits
  - infinite loop protection

----------------------------------------------------

## UI/UX REQUIREMENTS

- Child-friendly design (12 years old)
- Colorful and simple interface
- Large buttons
- Friendly messages
- VS Code-like editor experience
- Clear visual feedback for success/failure

----------------------------------------------------

## DEVELOPMENT RULES

When modifying or generating code:

- Always keep full working project state
- Never leave incomplete features
- Always ensure docker-compose up works
- Keep code modular and maintainable

----------------------------------------------------

## WORLDS STRUCTURE

1. Hello World
2. Variables
3. If / Else
4. Loops
5. Functions
6. Final Project

Each world must include:
- Multiple lessons
- One final challenge project

----------------------------------------------------

## IMPORTANT

Claude must always:
- Read this file before making changes
- Follow architecture strictly
- Maintain consistency across frontend/backend/AI system