import json, falcon


class ItemDetails:
    def on_get(self,req, resp):
        content = ("You have hit this endpoint successfully")
        resp.body = json.dumps(content)



app = falcon.App()

item = ItemDetails()
app.add_route('/item', item)

# if __name__ == '__main__':
#     with make_server('', 8000, app) as httpd:
#         print("Serving port at 8000")
#         httpd.serve_forever()