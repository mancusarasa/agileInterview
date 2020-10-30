from flask_sqlalchemy import SQLAlchemy
from app import db


class Tag(db.Model):
    tag_id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(100), nullable=False)
    image_id = db.Column(db.Integer, db.ForeignKey('image.img_id'), nullable=False)
    image = db.relationship('Image', backref=db.backref('tags', lazy=True))


class Image(db.Model):
    img_id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    camera = db.Column(db.String(100), nullable=False)


class LocalImagesCache(object):
    def __init__(self):
        super(LocalImagesCache, self).__init__()

    def find_by_term(self, search_term):
        # this search is quite inefficient.
        # I just hacked this piece of code to solve this because I'm quickly running out of time.
        result = [data._asdict() for data in db.session.query(Image.id, Image.author, Image.camera, Tag.tag).join(Tag, Tag.image_id == Image.img_id).all()]
        filtered_result = [img for img in result if img['author'] == search_term or img['camera']==search_term]
        return filtered_result

    def cache_random_objects(self):
        # these dummy objects are only here to test that searching for 'camera'
        # actually works (I went past my time to actually implement the periodic caching
        # of images)
        img = Image(id='e13a844e87c749edd2fc', author='someone', camera='camera')
        tag = Tag(tag='#life', image=img)
        db.session.add(img)
        db.session.commit()

cache = LocalImagesCache()
