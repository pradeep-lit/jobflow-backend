# JobFlow Backend
The Backend service to aggregate and track job opportunities.
## Problem
Nowadays, there are floods of job platforms they all have their own job opportunity base, so in this situation an employee dont want themself to spare their time in signing up for those floods while getting all relevant job opportunities. So I came up with a job aggregator and tracker system for them.
## Intended Users
Productive Job seeker and Employers maybe
## Planned Features
Job ingestion
Job deduplication
Search and filtering
Application tracking
User authentication
Telegram notifications
Background synchronization
PostgreSQL persistence
Redis caching
Automated tests
Docker deployment
## Technology Stack
Python (FastAPI) for backend
PostgreSQL for database
Redis for caching
Pytest for testing
etc...
## Current API Endpoints
/health - returns `{'status':'ok'}` when everything is ok in backend side
## Local Setup
I have added `pyproject.toml` for dependencies and etc. I have used `uv` so you can too.
## Testing
Using `pytest` for api testing of now
## Development Roadmap
First scripts to scrape the jobs and then backend then frontend then hosting and scaling