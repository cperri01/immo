# -*- coding: utf-8 -*-
import secret

SQLALCHEMY_DATABASE_URI = u'mysql+mysqldb://%s@localhost/lebonscrap?use_unicode=1' % secret.DB_AUTH
