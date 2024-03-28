from flask import Flask, request, send_file
from PIL import Image, ImageDraw

app = Flask(__name__)

@app.route("/getTest", methods=["GET", "POST"])
def get_or_post():
    if request.method == "POST":
        return "Uso un metodo POST"
    else:
        # Create a blank image (you can replace this with your own logic to generate the thumbnail and image)
        thumbnail = Image.new("RGB", (100, 100), "white")
        image = Image.new("RGB", (400, 400), "blue")

        # Example: Drawing on the image for demonstration purposes
        draw = ImageDraw.Draw(image)
        draw.text((10, 10), "Example Text", fill="white")

        # Save the images temporarily
        thumbnail_path = "/path/to/thumbnail.jpg"  # Replace with your desired path
        image_path = "/path/to/image.jpg"  # Replace with your desired path
        thumbnail.save(thumbnail_path)
        image.save(image_path)

        # Return the images
        return send_file(thumbnail_path, mimetype='image/jpeg'), send_file(image_path, mimetype='image/jpeg')

if __name__ == "__main__":
    app.run(debug=True)
