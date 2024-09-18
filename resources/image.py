from flask import request, jsonify, send_from_directory
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from db import db 
import os 
from models import ImageModel
from schemas import ImageSchema
from flask_jwt_extended import jwt_required, get_jwt
from werkzeug.utils import secure_filename

blp = Blueprint("Images", "images", description="Operations on images")

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@blp.route("/uploads")
class ImageList(MethodView):
    @jwt_required(fresh=True)
    @blp.arguments(ImageSchema)
    @blp.response(201, ImageSchema)
    def post(self, image_data):
        if 'image' not in request.files:
            return jsonify({'message': 'No image part'}), 400

        file = request.files['image']
        if file.filename == '':
            return jsonify({'message': 'No selected file'}), 400

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            new_image = ImageModel(image_path=os.path.join(UPLOAD_FOLDER, filename))
            db.session.add(new_image)
            db.session.commit()

            return jsonify({'message': 'Image uploaded successfully', 'image_id': new_image.id}), 201

        return jsonify({'message': 'Invalid file type'}), 400
    
@blp.route("/uploads/<string:image_id>")
class Image(MethodView):
    @blp.response(200, ImageSchema)
    def get(self, image_id):
        image = ImageModel.query.get_or_404(image_id)
        image_path = image.image_path
        filename = os.path.basename(image_path)
        return send_from_directory(directory=UPLOAD_FOLDER, path=filename)
