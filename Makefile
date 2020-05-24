
COMPOSE := docker-compose -f docker-compose.yml -f compose/docker-compose.dev.yml
COMPOSE_TEST := $(COMPOSE) -f compose/docker-compose.test.yml
COMPOSE_PROD := docker-compose -f docker-compose.yml -f compose/docker-compose.prod.yml

help:
	@echo
	@echo ----------------------------------------------------------------------
	@echo "   Development commands file                                        "
	@echo ----------------------------------------------------------------------
	@echo ">  R U N N I N G"
	@echo "  - build			            Build the containers for development"
	@echo "  - up			                Run & Up development server"
	@echo "  - clean			            Remove containers"
	@echo "  - create_network			    Create docker network to allow share resources"
	@echo "  - debug			            Run on debug mode"
	@echo "  - migrate			            Run migrate command"
	@echo "  - statics			            Run Collect statics command"
	@echo "  - superuser			        Create a superuser"


build_prod:
	@echo "Server django up..."
	$(COMPOSE_PROD) build

up_prod:
	@echo "Server django up..."
	$(COMPOSE_PROD) up

up:
	@echo "Server django up..."
	$(COMPOSE) up

clean:
	@echo "Cleaning containers ..."
	docker ps -aq | xargs docker stop
	docker ps -aq | xargs docker rm

create_network:
	@echo "Create a docker network ..."
	docker network create django_network

debug:
	@echo "Launchings Server for debbugging..."
	$(COMPOSE) run --service-ports django

migrations:
	@echo "Applying migrations ..."
	$(COMPOSE) run --rm django python manage.py makemigrations $(ARG)

migrate:
	@echo "Applying migrations ..."
	$(COMPOSE) run --rm django python manage.py migrate $(ARG)

superuser:
	@echo "Creating superuser..."
	$(COMPOSE) run --rm django python manage.py createsuperuser

statics:
	@echo "Collect statics ..."
	$(COMPOSE) run --rm django python manage.py collectstatic

test:
	@echo "Running tests with pytest cleaning cache..."
	$(COMPOSE_TEST) run --rm django pytest --pyargs $(ARG)

tests:
	$(COMPOSE_TEST) run --rm django pytest -n auto --pyargs $(ARG)

shell_prod:
	@echo "Opening container bash session"
	$(COMPOSE_PROD) run --rm django bash