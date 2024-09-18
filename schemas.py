from marshmallow import Schema, fields

class PlainArticleSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)

class PlainImageSchema(Schema):
    id = fields.Int(dump_only=True)
    image_path = fields.Str(load_only=False)


class ArticleSchema(PlainArticleSchema):
    image_id = fields.Int(required=True, load_only=True)  # This field is for passing the image ID when creating/updating
    image = fields.Nested(PlainImageSchema(), dump_only=True)  # This will retrieve the image object, including its path


class ImageSchema(PlainImageSchema):
    article = fields.Nested(PlainArticleSchema(), dump_only=True)

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    #csvdycuwv