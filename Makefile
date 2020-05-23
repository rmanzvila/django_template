
COMPOSE := docker-compose -f docker-compose.yml -f compose/docker-compose.dev.yml

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

build:
	$(COMPOSE) build
	@echo "Building project..."

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

migrate:
	@echo "Applying migrations ..."
	$(COMPOSE) run --rm django python manage.py migrate $(ARG)

superuser:
	@echo "Creating superuser..."
	$(COMPOSE) run --rm django python manage.py createsuperuser

statics:
	@echo "Collect statics ..."
	$(COMPOSE) run --rm django python manage.py collectstatic
