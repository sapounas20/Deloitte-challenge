from db import db 

class ArticleModel(db.Model):
    __tablename__ = "articles"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.String, unique=True, nullable=False)
    image_id = db.Column(db.Integer, db.ForeignKey("images.id"), nullable=True)
    image = db.relationship("ImageModel", back_populates="articles")
    
    