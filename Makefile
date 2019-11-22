MAIN_DOCKER := docker-compose.yml
PROJECT_NAME := daily
PARALLEL	:= --parallel
BUILD_MODE	:= build  ## Pass `pull` in order to pull images instead of building them

GIT_HASH=$(shell git rev-parse --short HEAD)

.PHONY:all
all:
	@echo 'Available make targets:'
	@grep '^[^#[:space:]^\.PHONY.*].*:' Makefile

## Run Commands
.PHONY: run
run:
	docker-compose -f $(MAIN_DOCKER) -p $(PROJECT_NAME) up -d

## Build Commands
.PHONY: build
build:
	docker-compose -f $(MAIN_DOCKER) -p $(PROJECT_NAME) $(BUILD_MODE) $(PARALLEL) base
	docker-compose -f $(MAIN_DOCKER) -p $(PROJECT_NAME) $(BUILD_MODE) $(PARALLEL)

## Stop Commands
.PHONY: stop stop-tests stop-testbed stop-integration
stop:
	-docker-compose -f $(MAIN_DOCKER) -p $(PROJECT_NAME) stop

## Clean Commands
.PHONY: clean clean-testbed clean-integration
clean:
	-docker-compose -f $(MAIN_DOCKER) -p $(PROJECT_NAME) down -v --remove-orphans
