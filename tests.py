from App import app, url

def test_change_url():
    client = app.test_client()

    # Post a new URL
    resp = client.post('/changeurl', data={'new_url': 'example.com'})
    assert resp.status_code == 200

    # Now GET / should redirect to the updated URL
    resp = client.get('/', follow_redirects=False)
    assert resp.status_code in (301, 302)
    location = resp.headers.get('Location')
    assert location is not None
    assert location.startswith('http://example.com')

if __name__ == '__main__':
    test_change_url()
    print('Test passed')
