import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEV_DATA = {
        'categories': ["Men's Shoes","Coats","Women's Pants","Accessories", "Cell Phones"],
        'companies': ["Macy's","Ross","Saks 5th Avenue","Best Buy"],
        'segments': ["Department","Hardgoods","Discount","Dollar","Electronics","Home Improvement","Apparel","Jewelry","Other"],
        'user_roles': ["Category Manager", "Exec", "Store Lead","Store Manager"], 
    }



    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 't0p s3cr3t'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'postgresql+psycopg2://blakeadams:@localhost/devturnstile'
  

class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'dbs/test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}