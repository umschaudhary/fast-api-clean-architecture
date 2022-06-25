# fast-api-clean-architecture
Fast API Clean Architecture template with docker, nginx, postgres, pgadmin4
<br/>



## Instructions

```bash
COPY .env.example .env #copy sample env to .env
```

```bash
docker-compose up --build #build and spin docker containers
```
OPEN API : http://localhost/docs


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
