## Command to Startup the Prediction Server

``` bash
cd prediction
uvicorn server:app --reload --host 0.0.0.0 --port 8000
```