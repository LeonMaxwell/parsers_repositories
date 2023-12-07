import settings


class Repositories(settings.app.db.Base):
    __tablename__ = 'repositories'
    __table_args__ = {'autoload':True}