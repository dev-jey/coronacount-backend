# corona-tracker
Track Corona virus cases

Front end link: https://coronacount.netlify.com

# Technologies used
- Django
- DRF
- Celery
- Selenium
- Pandas

# Endpoints

| Endpoint | route              | Method |  
|----------|--------------------|--------|
| General cases   | api/v1/cases/general-stats | GET   |
| Countries search   | api/v1/cases/countries-search?limit=1000 | GET   |
| Scrap Data   | api/v1/cases/scrap-data | GET   |
