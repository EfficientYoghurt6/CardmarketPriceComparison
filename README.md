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
4. **(Optional) Create the Cardmarket API key file**
   - `echo "CARDMARKET_API_KEY=<YOUR_TOKEN>" > backend/.env`
   - Without this file the app will fall back to pricing data from the public YGOProDeck API.
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

1. **Install Docker Desktop and WSL 2**
   - Go to the [Docker Desktop download page](https://www.docker.com/products/docker-desktop) and run the installer.
   - When prompted, leave **Use WSL 2 instead of Hyper-V** checked so Windows installs the required features.
   - If WSL is missing, open **PowerShell as Administrator** and run `wsl --install`, then reboot.
   - Make sure hardware virtualization is enabled in your BIOS (often listed as **Virtualization**, **VT-x**, or **SVM**).
2. **Start Docker Desktop**
   - Launch Docker Desktop from the Start menu and wait until the whale icon in the system tray stops spinning.
   - In PowerShell run `docker --version` and `wsl -l -v` to confirm Docker and a WSL 2 distro are available. If `docker` isn't recognized, open a new PowerShell window or use the built‑in terminal in Docker Desktop.
3. **Get this project**
   - Install [Git for Windows](https://git-scm.com/download/win) or use **Code → Download ZIP** on GitHub and extract to `C:\Users\<you>`.
   - `git clone https://github.com/<your-user>/CardmarketPriceComparison.git` *(replace `<your-user>` with the GitHub user or organization name)*
   - `cd CardmarketPriceComparison`
4. **Run with Docker Desktop UI (no console)**
   - Open Docker Desktop, go to the **Containers** tab, and click **+ Create > Compose**.
   - Browse to `docker-compose.yml` in the project folder and select **Run**. Docker Desktop builds the images and starts the containers; their status should turn green.
   - Tip: click the **Docker AI** icon (beaker) and ask questions such as *"How do I build this compose file?"* if you need live guidance.
5. **Run with PowerShell instead**
   - From PowerShell in the project directory run:
     - `docker compose build`
     - `docker compose up`
6. **Access the services**
   - Frontend: <http://localhost:3000>
   - Backend API: <http://localhost:8000>

#### Troubleshooting
- *Docker fails to start*: verify virtualization and WSL 2 are enabled; run `wsl --update` if the engine refuses to start.
- *`git` or `docker` not recognized*: reopen PowerShell or use the terminal built into Docker Desktop.
- *`docker compose` errors*: ensure you are inside the project folder and that you used `docker compose` (with a space), not the legacy `docker-compose`.
- *File sharing or path errors*: keep the project inside your user directory (`C:\Users\<you>`) so Docker Desktop can mount it.
- *Port 3000 or 8000 already in use*: stop the conflicting process or edit the `ports` in `docker-compose.yml`.
- *Containers fail to build on Windows*: disable automatic line ending conversion with `git config core.autocrlf false` and clone again.


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
- Uses the public YGOProDeck API for expansion and card names. If a
  Cardmarket API key is supplied, pricing is pulled from Cardmarket;
  otherwise YGOProDeck pricing is used.
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
