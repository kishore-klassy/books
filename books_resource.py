import json
from re import X

import falcon

from books_data import Books


class BooksResource:

    def on_get(self, req, resp):
        doc =  Books.library
        resp.text = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200
        return resp
    
    def on_post(self, req : falcon.Request, resp):
        new_book =json.loads(req.bounded_stream.read())
        new_book['id'] = 10000 + len(Books.library)
        Books.library.append(new_book)
        resp.text = json.dumps({'msg': 'Added', 'body': new_book}, ensure_ascii=False)
        resp.status = falcon.HTTP_200
    
    def on_delete(self, req : falcon.Request, resp):
        # print(req.query_string.split(sep='=')[1])
        for x in Books.library:
            if int(x['id']) == int(req.query_string.split(sep='=')[1]):
                deleted_book = x
                break
            else:
                deleted_book = None
        if(deleted_book != None):
            # print(deleted_book['id'])
            Books.library.remove(deleted_book)
            resp.text = json.dumps({'msg': 'Deleted', 'body': deleted_book}, ensure_ascii=False)
            resp.status = falcon.HTTP_200
        else:
            resp.text = json.dumps({'msg': 'Id not found'}, ensure_ascii=False)
            resp.status = falcon.HTTP_201
    
    def on_put(self, req : falcon.Request, resp):
        update =json.loads(req.bounded_stream.read())
        for x in Books.library:
            if str(x['id']) == req.query_string.split(sep='=')[1]:
                updated_book = x
                break
            else:
                updated_book = None
        if(updated_book != None):
            Books.library[Books.library.index(updated_book)] = update
            resp.text = json.dumps({'msg': 'Updated', 'body': updated_book}, ensure_ascii=False)
            resp.status = falcon.HTTP_200
        else:
            resp.text = json.dumps({'msg': 'Id not found'}, ensure_ascii=False)
            resp.status = falcon.HTTP_201