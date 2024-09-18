from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from db import db 
from models import ArticleModel
from schemas import ArticleSchema
from flask_jwt_extended import jwt_required, get_jwt

blp = Blueprint("Articles", "articles", description="Operations on articles")


@blp.route("/articles/<int:article_id>")
class Article(MethodView):
    @blp.response(200, ArticleSchema)
    def get(self, article_id):
       article = ArticleModel.query.get_or_404(article_id)
       return  article
    
    @jwt_required()
    def delete(self, article_id):
        article = ArticleModel.query.get_or_404(article_id)
        db.session.delete(article)
        db.session.commit()
        return {"message": "Article deleted"}
    
    
    @jwt_required()
    @blp.arguments(ArticleSchema(partial=True))
    @blp.response(200, ArticleSchema)
    def put(self, article_data, article_id):
        """Update article title, content, and image."""
        article = ArticleModel.query.get_or_404(article_id)

        for key, value in article_data.items():
            setattr(article, key, value) 
        
        try:
            db.session.commit()
        except IntegrityError:
            abort(400, message="An article with that name already exists.")
        except SQLAlchemyError:
            abort(500, message="An error occurred while updating the article.")
        
        return article

@blp.route("/articles")
class StoreList(MethodView):
    @blp.response(201, ArticleSchema(many= True))
    def get(self):
        return ArticleModel.query.all()
    
    @jwt_required()
    @blp.arguments(ArticleSchema)
    @blp.response(201,ArticleSchema)
    def post(self, article_data):
        article = ArticleModel(**article_data)

        try:
            db.session.add(article)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="An article with that name already exists.",
            )
        
        except SQLAlchemyError:
            abort(500, message="An error occurred while uploading the article.")

        return article
