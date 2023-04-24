from currency.models import Source


def test_get_api_source_list(api_client):
    response = api_client.get('/api/currency/source/')
    assert response.status_code == 200


def test_post_source_list(api_client):
    response = api_client.post('/api/currency/source/')
    assert response.status_code == 400
    assert response.json() == {
        'name': ['This field is required.'],
        'country': ['This field is required.'],
        'source_url': ['This field is required.'],
        'code_name': ['This field is required.']
    }


# def test_post_source_create(api_client):
#     data = {
#         # 'id': 1,
#         'name': 'vadym133',
#         'country': 'ua13',
#         'source_url': 'mailmail.comm',
#         'code_name': 'ssss'
#     }
#     response = api_client.post('/api/currency/source/', data=data)
#     assert response.status_code == 201
# assert response.json() == data


# def test_post_source_update(api_client):
#     data = {
#         'id': 6,
#         'name': 'seven',
#         'country': 'seven',
#         'source_url': 'mailmail.comm',
#         'code_name': 'mono'
#     }
#     response = api_client.put('/api/currency/source/6/', data=data)
#     assert response.status_code == 200
#     assert response.json() == data


# def test_delete_source(api_client):
#     source = Source.objects.create(
#         id=10,
#         name='seven',
#         country='seven',
#         source_url='mailmail.comm',
#         code_name='adasd'
#     )
#     response = api_client.delete('/api/currency/source/10/')
#     assert response.status_code == 204
#     assert not Source.objects.filter(id=9).exists()
