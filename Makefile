include .env

APP=docker-compose run app
MIGRATE=docker-compose run --rm app poetry run alembic

migrate-up:
		$(MIGRATE) upgrade head
migrate-down:
		$(MIGRATE) downgrade -1

create:
		@read -p  "What is the name of migration?" NAME; \
		${MIGRATE} revision --autogenerate -m $$NAME

poetry-add:
		@read -p "name? " NAME; \
		$(APP) poetry add $$NAME


poetry-install:
		$(APP) poetry install
