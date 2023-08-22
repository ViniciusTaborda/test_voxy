.PHONY: all backend frontend

all: backend frontend

backend:
	@echo "Starting FastAPI backend..."
	cd backend && uvicorn app.main:app --reload &

frontend:
	@echo "Starting Node.js server..."
	cd frontend && node server.js &

run: 
	$(MAKE) backend
	$(MAKE) frontend
	@echo "Both servers are running..."