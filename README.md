# Vanish

Playground for experimenting with `delete` refactorinmg

## Environment

    source ./venv/Scripts/activate

## Start database
    
    (cd local && docker-compose up -d)
 
## Autogenerate migration

    alembic revision -m 'Create Appeal Table' --autogenerate

## Run migration

    alembic upgrade head
 
## Connect to database
 
    jdbc:postgresql://localhost:5433/VANISH
    dev / dev123

