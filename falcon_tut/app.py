import json, falcon
from wsgiref.simple_server import make_server
class Items:
    def on_get(self,req, resp):
        resp.status = falcon.HTTP_200
        raw_data = req.stream.read()
        if raw_data:
            data = json.loads(raw_data)
        else:
            data={'name':"Unknown"}

        content = {"messge": "Hello {a}, You have hit this endpoint successfully.".format(a=data['name'])}
        resp.body = json.dumps(content)


    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200

        data = json.loads(req.stream.read())
        if data:
            ans = int(data.get('x'))+ int(data.get('y'))
            output = {'message': '{a} plus {b} equals {ans}.'.format(ans=ans, a=data["x"], b=data['y'])}
        else:
            ans = None
            output = {"message": "Invalid input: missing value for (x), (y)"}

        resp.body = json.dumps(output)

    def on_put(self, req, resp):
        resp.status = falcon.HTTP_200
        output = {"message": "Hey... Put method not supported"}
        resp.body = json.dumps(output)

    def on_delete(self, req, resp):
        resp.status = falcon.HTTP_200
        output = {"message": "Hey... Delete method not supported"}
        resp.body = json.dumps(output)

    





app = falcon.App()

item = Items()
app.add_route('/item', item)


# if __name__ == '__main__':
#     with make_server('', 8000, app) as httpd:
#         print('Serving on port 8000...')

#         # Serve until process is killed
#         httpd.serve_forever()