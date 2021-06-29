#-*- coding:utf-8 -*-
import flask
from flask import request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__,static_folder="./files")
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:123456@127.0.0.1:3307/test'
db = SQLAlchemy(app)
api = Api(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),unique=True,nullable=False)
    email = db.Column(db.String(80),unique=True,nullable=False)

    def __repr__(self):
        return f'<user:{self.name}'

class TestCase(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nodeid = db.Column(db.String(80),unique=True,nullable=False)
    description = db.Column(db.String(120),unique=True,nullable=False)

    def as_dict(self):
        return {"id":self.id,"nodeid":self.nodeid,"description":self.description}

class TestCaseServer(Resource):
    def get(self):
        # 查询用例
        testcase = TestCase.query.all()
        # 格式化数据
        format_test_case = [i.as_dict() for i in testcase]
        #返回列表
        return format_test_case

    def post(self):
        """
        新增用例==》用例解析的方式获取
        :return:
        """
        # nodeid = request.args.get('nodeid')   #从请求中获取参数
        # description = request.json.get("description") #获取id
        # return [nodeid,description]
        #请求体中的数据，发送到数据库中
        data = TestCase(**request.json)
        db.session.add(data)
        db.session.commit()
        return {"msg":"OK"}



#flask restful将接口写入类中
api.add_resource(TestCaseServer,'/testcase')


if __name__=="__main__":
    app.run(host="0.0.0.0",port=8888,debug=True)
    # 表格创建
    # db.create_all()
    # 新增
    # data = User(id="123",name="name",email="emailtest")
    # db.session.add(data)  # add /query.filter_by/ delete  user重置数据进行修改操作
    # db.session.commit()
