# eleclerc-backend-suppliers-platform
Backend of the E.Leclerc suppliers product registration platform.

# Build & Run

```bash
# build containers and deploy
docker-compose up --build
```

# Reset Database

```bash
# drops the volumes attached to the containers
docker-compose down -v

# brings up the containers
docker-compose up
```