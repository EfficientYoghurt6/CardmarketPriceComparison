# Repository Guidelines

This repository hosts a FastAPI backend and a React + TypeScript frontend for comparing Yugioh card prices from the Cardmarket API.

## General Instructions
- Keep the architecture modular; new analytics modules will be added over time.
- Run backend checks with `pytest` in the `backend` directory.
- Run frontend checks with `npm install` and `npm test` in the `frontend` directory.
- Document architectural decisions in the README when adding features.
- Avoid committing environment-specific files or build artifacts.
