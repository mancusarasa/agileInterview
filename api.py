#!/usr/bin/env python

from flask_restful import Resource, reqparse
import requests
import json

from app_config import config
from local_images_cache import cache
from app import app, api, db
from token_manager import generate_new_token, current_token, update_current_token

class GetImages(Resource):

    def _do_get(self, token, params, request_url):
        headers = {'Authorization': 'Bearer ' + token, 'content-type': 'application/json'}
        return requests.get(request_url, headers=headers, params=params)

    def get(self):
        token = current_token
        params = {}
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int)
        args = parser.parse_args()
        if args['page'] is not None:
            params = {'page': args['page']}
        request_url = config.get_base_url() + '/images'
        response = self._do_get(token, params, request_url)
        if response.status_code != 200:
            # I'll asume that if the request fails
            # it was because of the expired token
            # and create a new one
            update_current_token()
            response = self._do_get(current_token, params, request_url)
        return response.json()


class GetImageInfo(Resource):

    def _do_get(self, token, request_url):
        # this code is repeated with getImages; extract to a common superclass
        headers = {'Authorization': 'Bearer ' + token, 'content-type': 'application/json'}
        return requests.get(request_url, headers=headers)

    def get(self, image_id):
        token = current_token
        request_url = config.get_base_url() + '/images/' + image_id
        headers = {'Authorization': 'Bearer bf12a864c251dcee47b14afa2cc648569461c83f', 'content-type': 'application/json'}
        response = self._do_get(current_token, request_url)
        if response.status_code != 200:
            # I'll asume that if the request fails
            # it was because of the expired token
            # and create a new one
            update_current_token()
            response = self._do_get(current_token, params, request_url)

        return response.json()


class SearchImages(Resource):
    def get(self, search_term):
        images = cache.find_by_term(search_term)
        return images


if __name__ == '__main__':
    api.add_resource(GetImages, '/images')
    api.add_resource(GetImageInfo, '/images/<string:image_id>')
    api.add_resource(SearchImages, '/search/<string:search_term>')
    db.create_all()
    cache.cache_random_objects()
    app.run(debug=True)
