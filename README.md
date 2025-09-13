# Cardmarket Price Comparison

An extensible web application that compares prices of Yugioh singles and sealed products using the [Cardmarket API](https://api.cardmarket.com/). The app also estimates expected value (EV) per pack and will support more analytics features over time.

## Architecture

The project is split into a **FastAPI backend** and a **React + TypeScript frontend**. Each part runs in its own container and they are orchestrated with `docker-compose`.

```
.
├── backend                # FastAPI service
├── frontend               # React web client
├── Dockerfile.backend     # Backend container definition
├── Dockerfile.frontend    # Frontend container definition
└── docker-compose.yml     # Development orchestration
```

### Backend
- Exposes REST endpoints for expansions, card data and EV calculation.
- Provides service layer stubs for Cardmarket API communication and EV computation.
- Written in Python 3.11 with FastAPI.
- Tests are executed with `pytest`.

### Frontend
- Vite-powered React application using TypeScript.
- Modern UI skeleton with components for selecting expansions, listing cards and configuring EV calculations.
- Future analytics views can be added under `src/components`.

### Docker
- `Dockerfile.backend` builds the FastAPI service and runs it with Uvicorn on port `8000`.
- `Dockerfile.frontend` builds the React application and serves the static bundle through Nginx on port `3000`.
- `docker-compose.yml` wires both services together for local development.

## Development

### Backend
```bash
cd backend
pip install -r requirements.txt
pytest
```

### Frontend
```bash
cd frontend
npm install
npm test
```

### Running with Docker
```bash
docker-compose build
docker-compose up
```

The frontend will be available at `http://localhost:3000` and the backend API at `http://localhost:8000`.

## License

MIT
