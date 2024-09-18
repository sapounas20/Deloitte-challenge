from db import db


class ImageModel(db.Model):
    __tablename__ = "images"

    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String(200), nullable=False)
    articles = db.relationship("ArticleModel", back_populates="image", lazy="dynamic")

    def __init__(self, image_path):
        self.image_path = image_path