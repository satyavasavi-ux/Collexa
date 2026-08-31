.PHONY: help install build run test clean docker-build docker-up

help:
	@echo "Collexa Enterprise Campus Management System"
	@echo "Available commands:"
	@echo "  make install      - Install backend and frontend dependencies"
	@echo "  make build        - Build frontend production assets"
	@echo "  make run          - Launch backend and frontend servers"
	@echo "  make test         - Run test suite"
	@echo "  make docker-build - Build Docker container image"
	@echo "  make docker-up    - Run application via Docker Compose"

install:
	cd backend && pip install -r requirements.txt
	cd frontend && npm install

build:
	cd frontend && npm run build

run:
	python run.py

test:
	pytest backend/tests

clean:
	rm -rf frontend/dist backend/__pycache__ .pytest_cache

docker-build:
	docker build -t collexa-erp:latest .

docker-up:
	docker compose up -d
