from flask import Flask, jsonify

app = Flask(__name__)

# Dicionários de tradução
colors = {
    "vermelho": {"en": "red", "fr": "rouge"},
    "laranja": {"en": "orange", "fr": "orange"},
    "amarelo": {"en": "yellow", "fr": "jaune"},
    "verde": {"en": "green", "fr": "vert"},
    "azul": {"en": "blue", "fr": "bleu"},
    "anil": {"en": "indigo", "fr": "indigo"},
    "violeta": {"en": "violet", "fr": "violet"},
    "red": {"fr": "rouge"},
    "orange": {"fr": "orange"},
    "yellow": {"fr": "jaune"},
    "green": {"fr": "vert"},
    "blue": {"fr": "bleu"},
    "indigo": {"fr": "indigo"},
    "violet": {"fr": "violet"}
}

@app.route('/translate/<lang_from>/<lang_to>/<color>', methods=['GET'])
def translate(lang_from, lang_to, color):
    color = color.lower()
    lang_from = lang_from.lower()
    lang_to = lang_to.lower()

    if lang_from == "pt" and color in colors:
        if lang_to in colors[color]:
            return jsonify({color: colors[color][lang_to]})
        else:
            return jsonify({"error": "Translation not found"}), 404
    elif lang_from == "en" and color in colors:
        if "fr" in colors[color]:
            return jsonify({color: colors[color]["fr"]})
        else:
            return jsonify({"error": "Translation not found"}), 404
    else:
        return jsonify({"error": "Translation not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)