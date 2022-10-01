import pytest
import requests

def test_rq():
    q = requests.get("http://localhost:5500/data.json")
    data = q.json()
    assert data["b"] == "bbcc"
    print(data)