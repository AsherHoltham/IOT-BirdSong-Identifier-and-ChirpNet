from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionary containing bird information
birds_info = {
    "Northern Cardinal": {"description": "A bright red, seed-eating bird in the cardinal family.", "habitat": "Woodlands, gardens, shrublands, and swamps."},
    "Nuttall's Woodpecker": {"description": "A small woodpecker native to California.", "habitat": "Oak woodlands and mixed deciduous forests."},
    "Rock Pigeon": {"description": "Common city pigeon with a wide range of plumage colors.", "habitat": "Urban areas, cliffs, and underpasses."},
    "Peregrine Falcon": {"description": "Fastest bird in the world, known for its speed during a hunt.", "habitat": "Wide range including mountains, coastal cliffs, and skyscrapers."},
    "Black-crowned Night Heron": {"description": "Medium-sized heron with a black crown and back.", "habitat": "Freshwater wetlands, estuaries, and marshes."},
    "Western Bluebird": {"description": "Small thrush with a blue top and a reddish breast.", "habitat": "Open woodlands and farmlands."},
    "House Sparrow": {"description": "Small bird, often found in urban environments.", "habitat": "Urban areas, parks, and gardens."},
    "Red-tailed Hawk": {"description": "One of the most common hawks in North America.", "habitat": "Open country, woodlands, prairies, and mountains."},
    "Bushtit": {"description": "Tiny, long-tailed bird of the American bushtit family.", "habitat": "Forests, thicket, and shrublands."},
    "Common Raven": {"description": "Large all-black bird, famous for its intelligence.", "habitat": "Varied, from Arctic tundra to deserts and mountains."},
}

@app.route('/bird', methods=['GET'])
def get_bird_info():
    bird_name = request.args.get('name', type=str)
    if bird_name in birds_info:
        return jsonify(birds_info[bird_name])
    else:
        return jsonify({"error": "Bird not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
