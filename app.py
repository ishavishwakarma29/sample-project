from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

items = [
    {"id": 1, "title": "Set up the Flask app", "done": True},
    {"id": 2, "title": "Create a sample UI", "done": False},
    {"id": 3, "title": "Deploy or extend the project", "done": False},
]

next_id = 4


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/api/items")
def get_items():
    return jsonify(items)


@app.post("/api/items")
def add_item():
    global next_id

    payload = request.get_json(silent=True) or {}
    title = (payload.get("title") or "").strip()

    if not title:
        return jsonify({"error": "Title is required"}), 400

    new_item = {"id": next_id, "title": title, "done": False}
    items.append(new_item)
    next_id += 1
    return jsonify(new_item), 201


@app.put("/api/items/<int:item_id>/toggle")
def toggle_item(item_id):
    for item in items:
        if item["id"] == item_id:
            item["done"] = not item["done"]
            return jsonify(item)

    return jsonify({"error": "Item not found"}), 404


@app.delete("/api/items/<int:item_id>")
def delete_item(item_id):
    for index, item in enumerate(items):
        if item["id"] == item_id:
            del items[index]
            return jsonify({"message": "Item deleted"})

    return jsonify({"error": "Item not found"}), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
