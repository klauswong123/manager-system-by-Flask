from setting import db
from models import Jewelrys_Photos
a = Jewelrys_Photos.query.all()

for image in a:
    print(image.image[4])