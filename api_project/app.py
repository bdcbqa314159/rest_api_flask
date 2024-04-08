#pylint: disable-all

from flask import Flask, request
from flask_smorest import abort
import uuid
from db import stores, items

app = Flask(__name__)

@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}

@app.post("/store")
def create_store():
    store_data = request.get_json()
    if "name" not in store_data:
        abort(404, message="Bad request. Ensure 'name' is provided in the JSON payload.")
    
    for store in stores.values():
        if store["name"] == store_data["name"]:
            abort(400, message="Store already exists.")
            
    store_id = uuid.uuid4().hex
    store = {**store_data, "id": store_id}
    stores[store_id] = store
    return store, 201

@app.post("/item")
def create_item(name):
    item_data = request.get_json()
    if "price" not in item_data or "store_id" not in item_data or "name" not in item_data:
        abort(400, message="Bad request. Ensure 'price', 'store_id' and 'name' are provided in the JSON payload.")
    
    for item in items.values():
        if item["name"] == item_data["name"] and item["store_id"] == item_data["store_id"]:
            abort(400, message="Item already exists.")

    if item_data["store_id"] not in stores:
        abort(404, message="Store not found.")

    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item
    return item, 201

@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}

@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id], 201
    except KeyError:
        abort(404, message="Store not found.")

@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id], 201
    except KeyError:
        abort(404, message="Item not found.")