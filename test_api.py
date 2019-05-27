import requests


class TestServer:

    def test_get_error(self):
        res = requests.get('http://127.0.0.1:5000/planner/api/v1.0/').json()
        assert(res['error'] == "Unauthorized access")

        res = requests.get(
            'http://127.0.0.1:5000/planner/api/v1.0/notes').json()
        assert(res['error'] == "Unauthorized access")

        res = requests.get(
            'http://127.0.0.1:5000/planner/api/v1.0/notes/2012-04-23T18:25:47.511Z').json()
        assert(res['error'] == "Unauthorized access")

        res = requests.get(
            'http://127.0.0.1:5000/planner/api/v1.0/notes/2012-04-23T18:25:47.5Z',
            auth=('lazygirl', "python")).json()
        assert(res['error'] == "Not found")

    def test_get_success(self):
        res = requests.get(
            'http://127.0.0.1:5000/planner/api/v1.0/',
            auth=('lazygirl', "python")).json()
        assert(res['message'] == "Hello, world!")

        res = requests.get(
            'http://127.0.0.1:5000/planner/api/v1.0/notes',
            auth=('lazygirl', "python")).json()
        assert(res['notes'] == {'2012-04-23T18:25:47.511Z': '1',
                                '2017-04-23T18:25:43.511Z': '2', '2012-04-23T18:25:43.511Z': '3'})

        res = requests.get(
            'http://127.0.0.1:5000/planner/api/v1.0/notes/2012-04-23T18:25:47.511Z',
            auth=('lazygirl', "python")).json()
        assert(res['2012-04-23T18:25:47.511Z'] == "1")

    # put
    def test_put_error(self):
        res = requests.put("http://127.0.0.1:5000/planner/api/v1.0/notes/non-exist",
                           json={'note': "bla"}, auth=('lazygirl', "python")).json()
        assert(res['error'] == 'Updating non-existing resourse')

    def test_put_success(self):
        res = requests.put('http://127.0.0.1:5000/planner/api/v1.0/notes/2012-04-23T18:25:47.511Z',
                           auth=('lazygirl', "python"), json={'note': '1'}).json()
        assert(res['updated'] == {'2012-04-23T18:25:47.511Z': '1'})

    # post
    def test_post_error(self):
        res = requests.post(
            "http://127.0.0.1:5000/planner/api/v1.0/notes",
            json={'date': '2017-04-23T18:25:43.511Z', 'note': 'bla'},
            auth=('lazygirl', "python")).json()
        assert(res['error'] == 'Adding existing resourse')

    def test_post_success(self):
        res = requests.post(
            'http://127.0.0.1:5000/planner/api/v1.0/notes',
            json={'date': '3000-04-23T18:25:43.511Z', 'note': 'bla'},
            auth=('lazygirl', "python")).json()
        assert(res['3000-04-23T18:25:43.511Z'] == 'bla')

    # delete
    def test_delete_error(self):
        res = requests.delete(
            'http://127.0.0.1:5000/planner/api/v1.0/notes/2012-04-23T18:25:4.5Z',
            auth=('lazygirl', "python")).json()
        assert(res['error'] == "Not found")

    def test_delete_success(self):
        res = requests.delete(
            'http://127.0.0.1:5000/planner/api/v1.0/notes/3000-04-23T18:25:43.511Z',
            auth=('lazygirl', "python")).json()
        assert(res['deleted'] is True)
