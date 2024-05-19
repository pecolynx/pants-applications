
.PHONY: test-docker-up
test-docker-up:
	@docker compose -f docker/test/docker-compose.yml up -d
