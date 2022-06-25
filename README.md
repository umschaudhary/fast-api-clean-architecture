# fast-api-clean-architecture
Fast API Clean Architecture template with docker, nginx, postgres, pgadmin4
<br/>



## Instructions
Run below commands to your terminal

```bash
COPY .env.example .env #copy sample env to .env
```

```bash
docker-compose up --build #build and spin docker containers
```

```bash
make migrate-up # to migrate migrations
```

- API DOCS : http://localhost/docs 
- PGADMIN4: http://localhost:5050

Check `Makefile` for available commands


## Features
- [X] Docker
- [x] postgres
- [x] nginx
- [x] pgadmin4
- [x] Dependency injection
- [x] SqlAlchemy as ORM
- [x] Poetry to manage python packages
- [x] Alembic for migrations
- [x] pydantic data validation
- [x] User model
- [ ] User authentication 
- [ ] Exception handling
- [ ] Error handling
- [ ] Singleton instance
