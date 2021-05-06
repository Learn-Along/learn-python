"""
@TODO:
- Look at HTTP methods, HTTP status codes
"""

import unittest
import os
import json
from app import create_app, db


class BucketlistTestCase(unittest.TestCase):
    """This class represents the bucketlist test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.bucketlist = {'name': 'Go to Borabora for vacation'}

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_bucketlist_creation(self):
        """Test API can create a bucketlist (POST request)"""
        # visit http://localhost:5000/bucketlists/; HTTP method: POST
        res = self.client().post('/bucketlists/', data=self.bucketlist)
        # Expect that HTTP status_code == 201
        self.assertEqual(res.status_code, 201)
        # Expect 'Go to Borabora' is in str(res.data)
        self.assertIn('Go to Borabora', str(res.data))

    def test_api_can_get_all_bucketlists(self):
        """Test API can get a bucketlist (GET request)."""
        # visit http://localhost:5000/bucketlists/; HTTP method: POST
        res = self.client().post('/bucketlists/', data=self.bucketlist)
        # Expect that the HTTP status code is 201
        self.assertEqual(res.status_code, 201)
        # http://localhost:5000/bucketlists/; HTTP method: GET
        res = self.client().get('/bucketlists/')
        # Expect that the HTTP status code will be 200
        self.assertEqual(res.status_code, 200)
        # Expect that the body (data) will have the words 'Go to Borabora'
        # which are part of the bucketlist item we created (self.bucketlist)
        self.assertIn('Go to Borabora', str(res.data))

    def test_api_can_get_bucketlist_by_id(self):
        """Test API can get a single bucketlist by using it's id."""
        # visit http://localhost:5000/bucketlists/; HTTP method: POST
        rv = self.client().post('/bucketlists/', data=self.bucketlist)
        # Expect that the HTTP status code is 201
        self.assertEqual(rv.status_code, 201)
        # we decode the data that is returned to get the id of the created bucketlist
        result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        # http://localhost:5000/bucketlists/1; if id = 1; HTTP method: GET
        result = self.client().get(
            '/bucketlists/{}'.format(result_in_json['id']))
        # Expect that status code is 200
        self.assertEqual(result.status_code, 200)
        # Expect that self.bucketlist is returned
        self.assertIn('Go to Borabora', str(result.data))

    def test_bucketlist_can_be_edited(self):
        """Test API can edit an existing bucketlist. (PUT request)"""
        # visit http://localhost:5000/bucketlists/; HTTP method: POST
        rv = self.client().post(
            '/bucketlists/',
            data={'name': 'Eat, pray and love'})
        # Expect the HTTP status code is 201
        self.assertEqual(rv.status_code, 201)
        # visit http://localhost:5000/bucketlists/1; HTTP method: PUT
        rv = self.client().put(
            '/bucketlists/1',
            data={
                "name": "Dont just eat, but also pray and love :-)"
            })
        # Expect that the status code is 200
        self.assertEqual(rv.status_code, 200)
        # visit http://localhost:5000/bucketlists/1; HTTP method: GET
        results = self.client().get('/bucketlists/1')
        # Exect the name to have been updated
        self.assertIn('Dont just eat', str(results.data))

    def test_bucketlist_deletion(self):
        """Test API can delete an existing bucketlist. (DELETE request)."""
        # visit http://localhost:5000/bucketlists/; HTTP method: POST
        rv = self.client().post(
            '/bucketlists/',
            data={'name': 'Eat, pray and love'})
        # Expect the statu code to be 201
        self.assertEqual(rv.status_code, 201)
        # visit http://localhost:5000/bucketlists/1; HTTP method: DELETE
        res = self.client().delete('/bucketlists/1')
        # Expect that the status code wil be 200
        self.assertEqual(res.status_code, 200)
        # Test to see if it exists, should return a status code: NOT FOUND: 404
        result = self.client().get('/bucketlists/1')
        self.assertEqual(result.status_code, 404)

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
