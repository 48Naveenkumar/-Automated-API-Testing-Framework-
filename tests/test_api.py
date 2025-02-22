import requests

def test_get_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    
    assert response.status_code == 200  # Check if the status code is 200
    assert "userId" in response.json()  # Check if response has "userId"
