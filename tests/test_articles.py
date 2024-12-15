def test_list_articles(client):
    response = client.get('/articles/')
    assert response.status_code == 200
