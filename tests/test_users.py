def test_user_profile(client):
    response = client.get('/users/testuser')
    assert response.status_code == 200
    assert b"Profile page for user: testuser" in response.data
