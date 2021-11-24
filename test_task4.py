"""
Create test to get information about albums by id
	Send the http request by using the GET method. · The URL is http://jsonplaceholder.typicode.com/ albums /{id}
	Validation: the content of the response body is the one album and it contains fields: userId, id, title.
"""

import json
import pytest
import requests


@pytest.fixture(scope='session')
def response():
	url = 'http://jsonplaceholder.typicode.com/albums/1'
	response = requests.get(url)
	response_content = json.loads(response.content)
	return response_content

def test_body_must_have_only_one_album(response):
	assert response

@pytest.mark.parametrize('field', ['userId', 'id', 'title'])
def test_album_contains_fileds(response, field):
	assert field in response.keys()