# Cardmarket Price Comparison

An extensible web application that compares prices of Yugioh singles and sealed products using the [Cardmarket API](https://api.cardmarket.com/). The app also estimates expected value (EV) per pack and will support more analytics features over time.

## Setup Guide

The project runs the backend and frontend in Docker containers, so the host only needs Docker and `docker-compose`.

### Linux / TrueNAS SCALE

1. **Install Docker and Compose**
   - Ubuntu/Debian: `sudo apt update && sudo apt install docker.io docker-compose`
   - TrueNAS SCALE: open the web UI, go to **Apps → Settings**, enable **Docker Compose**, and apply.
2. **Allow your user to run Docker**
   - `sudo usermod -aG docker $USER`
   - log out and back in to apply the group change.
3. **Clone this repository**
   - `git clone https://github.com/<your-user>/CardmarketPriceComparison.git` *(replace `<your-user>` with the GitHub user or organization name)*
   - `cd CardmarketPriceComparison`
4. **Create the Cardmarket API key file**
   - `echo "CARDMARKET_API_KEY=<YOUR_TOKEN>" > backend/.env`
5. **Build and start the containers**
   - `docker-compose build`
   - `docker-compose up`
6. **Visit the app**
   - Frontend: `http://localhost:3000`
   - Backend API: `http://localhost:8000`

#### Troubleshooting
- *Docker command not found*: ensure Docker is installed and the service is running (`sudo systemctl status docker`).
- *Permission denied while connecting to Docker daemon*: run step 2 and re-login.
- *Ports 3000 or 8000 already in use*: stop the conflicting service or edit `docker-compose.yml` to change the ports.

### Windows (Docker Desktop)

1. **Install prerequisites**
   - [Download Docker Desktop](https://www.docker.com/products/docker-desktop) and run the installer.
   - Enable the **WSL 2** option if prompted and reboot when requested.
2. **Verify Docker is running**
   - Start Docker Desktop and wait for the whale icon to become stable.
   - Open PowerShell and run `docker --version` and `docker compose version` to confirm.
3. **Clone this repository**
   - Install [Git for Windows](https://git-scm.com/download/win) if needed.
   - `git clone https://github.com/<your-user>/CardmarketPriceComparison.git` *(replace `<your-user>` with the GitHub user or organization name)*
   - `cd CardmarketPriceComparison`
4. **Add the API key**
   - `echo CARDMARKET_API_KEY=<YOUR_TOKEN> > backend/.env`
5. **Build and start the stack**
   - `docker compose build`
   - `docker compose up`
6. **Access the services**
   - Frontend: <http://localhost:3000>
   - Backend API: <http://localhost:8000>

#### Troubleshooting
- *Docker fails to start*: ensure hardware virtualization is enabled in the BIOS and that Hyper-V/WSL features are turned on.
- *`git` or `docker` not recognized*: reopen PowerShell after installation or check that the tools were added to your PATH.
- *File sharing errors*: keep the project in your user directory so Docker Desktop can mount it.


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
- Uses the public YGOProDeck API for expansion and card names and the
  authenticated Cardmarket API for live pricing.
- Stores the Cardmarket API key in a local `.env` file which is excluded from
  version control. The key can be supplied via the console with
  `python -m app.cli --key <TOKEN>` or through the web UI form.
- Includes an expected value utility that validates probability distributions.
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
