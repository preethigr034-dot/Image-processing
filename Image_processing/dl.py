from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
import os
import uuid

# ============================================================
# FLASK CONFIGURATION
# ============================================================

app = Flask(__name__)

RESULT_FOLDER = "static/results"

os.makedirs(RESULT_FOLDER, exist_ok=True)


# ============================================================
# IMAGE PROCESSING CLASS
# ============================================================

class ImageProcessor:

    def __init__(self, image):
        self.image = image

    # --------------------------------------------------------
    # DISPLAY IMAGE
    # --------------------------------------------------------

    def display(self):
        return self.image.copy()

    # --------------------------------------------------------
    # GRAYSCALE
    # --------------------------------------------------------

    def grayscale(self):
        return cv2.cvtColor(
            self.image,
            cv2.COLOR_BGR2GRAY
        )

    # --------------------------------------------------------
    # BINARY / THRESHOLD
    # --------------------------------------------------------

    def binary(self):

        gray = cv2.cvtColor(
            self.image,
            cv2.COLOR_BGR2GRAY
        )

        _, binary_image = cv2.threshold(
            gray,
            127,
            255,
            cv2.THRESH_BINARY
        )

        return binary_image

    # --------------------------------------------------------
    # JPG
    # --------------------------------------------------------

    def jpg(self):
        return self.image.copy()

    # --------------------------------------------------------
    # PNG
    # --------------------------------------------------------

    def png(self):
        return self.image.copy()

    # --------------------------------------------------------
    # BMP
    # --------------------------------------------------------

    def bmp(self):
        return self.image.copy()

    # --------------------------------------------------------
    # RGB TO GRAYSCALE
    # --------------------------------------------------------

    def rgb_gray(self):

        return cv2.cvtColor(
            self.image,
            cv2.COLOR_BGR2GRAY
        )

    # --------------------------------------------------------
    # RGB TO HSV
    # --------------------------------------------------------

    def hsv(self):

        hsv_image = cv2.cvtColor(
            self.image,
            cv2.COLOR_BGR2HSV
        )

        # Convert back to BGR for browser display
        return cv2.cvtColor(
            hsv_image,
            cv2.COLOR_HSV2BGR
        )

    # --------------------------------------------------------
    # HISTOGRAM EQUALIZATION
    # --------------------------------------------------------

    def histogram(self):

        gray = cv2.cvtColor(
            self.image,
            cv2.COLOR_BGR2GRAY
        )

        equalized = cv2.equalizeHist(gray)

        return equalized

    # --------------------------------------------------------
    # BRIGHTNESS AND CONTRAST
    # --------------------------------------------------------

    def brightness_contrast(
        self,
        alpha=1.5,
        beta=40
    ):

        return cv2.convertScaleAbs(
            self.image,
            alpha=alpha,
            beta=beta
        )

    # --------------------------------------------------------
    # AVERAGE FILTER
    # --------------------------------------------------------

    def average(self):

        return cv2.blur(
            self.image,
            (5, 5)
        )

    # --------------------------------------------------------
    # GAUSSIAN FILTER
    # --------------------------------------------------------

    def gaussian(self):

        return cv2.GaussianBlur(
            self.image,
            (5, 5),
            0
        )

    # --------------------------------------------------------
    # LAPLACIAN FILTER
    # --------------------------------------------------------

    def laplacian(self):

        gray = cv2.cvtColor(
            self.image,
            cv2.COLOR_BGR2GRAY
        )

        lap = cv2.Laplacian(
            gray,
            cv2.CV_64F
        )

        return cv2.convertScaleAbs(lap)

    # ========================================================
    # MORPHOLOGICAL OPERATIONS
    # ========================================================

    def get_binary_image(self):

        gray = cv2.cvtColor(
            self.image,
            cv2.COLOR_BGR2GRAY
        )

        _, binary_image = cv2.threshold(
            gray,
            127,
            255,
            cv2.THRESH_BINARY
        )

        return binary_image

    # --------------------------------------------------------
    # EROSION
    # --------------------------------------------------------

    def erosion(self):

        binary_image = self.get_binary_image()

        kernel = np.ones(
            (5, 5),
            np.uint8
        )

        eroded = cv2.erode(
            binary_image,
            kernel,
            iterations=1
        )

        return eroded

    # --------------------------------------------------------
    # DILATION
    # --------------------------------------------------------

    def dilation(self):

        binary_image = self.get_binary_image()

        kernel = np.ones(
            (5, 5),
            np.uint8
        )

        dilated = cv2.dilate(
            binary_image,
            kernel,
            iterations=1
        )

        return dilated

    # --------------------------------------------------------
    # OPENING
    # --------------------------------------------------------

    def opening(self):

        binary_image = self.get_binary_image()

        kernel = np.ones(
            (5, 5),
            np.uint8
        )

        opened = cv2.morphologyEx(
            binary_image,
            cv2.MORPH_OPEN,
            kernel
        )

        return opened

    # --------------------------------------------------------
    # CLOSING
    # --------------------------------------------------------

    def closing(self):

        binary_image = self.get_binary_image()

        kernel = np.ones(
            (5, 5),
            np.uint8
        )

        closed = cv2.morphologyEx(
            binary_image,
            cv2.MORPH_CLOSE,
            kernel
        )

        return closed


# ============================================================
# HOME PAGE
# ============================================================

@app.route("/")
def index():

    return render_template("index.html")


# ============================================================
# IMAGE PROCESSING
# ============================================================

@app.route("/process", methods=["POST"])
def process_image():

    try:

        # ----------------------------------------------------
        # CHECK IMAGE
        # ----------------------------------------------------

        if "image" not in request.files:

            return jsonify({
                "error": "No image uploaded"
            }), 400

        file = request.files["image"]

        if file.filename == "":

            return jsonify({
                "error": "No image selected"
            }), 400

        # ----------------------------------------------------
        # GET OPERATION
        # ----------------------------------------------------

        operation = request.form.get("operation")

        if not operation:

            return jsonify({
                "error": "No operation selected"
            }), 400

        # ----------------------------------------------------
        # READ IMAGE
        # ----------------------------------------------------

        file_bytes = np.frombuffer(
            file.read(),
            np.uint8
        )

        image = cv2.imdecode(
            file_bytes,
            cv2.IMREAD_COLOR
        )

        # IMPORTANT
        # Check the decoded image, NOT the file path

        if image is None:

            return jsonify({
                "error": "Unable to read image"
            }), 400

        # ----------------------------------------------------
        # CREATE PROCESSOR
        # ----------------------------------------------------

        processor = ImageProcessor(image)

        # ----------------------------------------------------
        # SELECT OPERATION
        # ----------------------------------------------------

        if operation == "display":

            result = processor.display()
            extension = ".jpg"

        elif operation == "grayscale":

            result = processor.grayscale()
            extension = ".png"

        elif operation == "binary":

            result = processor.binary()
            extension = ".png"

        elif operation == "jpg":

            result = processor.jpg()
            extension = ".jpg"

        elif operation == "png":

            result = processor.png()
            extension = ".png"

        elif operation == "bmp":

            result = processor.bmp()
            extension = ".bmp"

        elif operation == "rgb_gray":

            result = processor.rgb_gray()
            extension = ".png"

        elif operation == "hsv":

            result = processor.hsv()
            extension = ".jpg"

        elif operation == "histogram":

            result = processor.histogram()
            extension = ".png"

        elif operation == "brightness":

            result = processor.brightness_contrast()
            extension = ".jpg"

        elif operation == "average":

            result = processor.average()
            extension = ".jpg"

        elif operation == "gaussian":

            result = processor.gaussian()
            extension = ".jpg"

        elif operation == "laplacian":

            result = processor.laplacian()
            extension = ".png"

        # ----------------------------------------------------
        # MORPHOLOGY
        # ----------------------------------------------------

        elif operation == "erosion":

            result = processor.erosion()
            extension = ".png"

        elif operation == "dilation":

            result = processor.dilation()
            extension = ".png"

        elif operation == "opening":

            result = processor.opening()
            extension = ".png"

        elif operation == "closing":

            result = processor.closing()
            extension = ".png"

        else:

            return jsonify({
                "error": "Invalid operation"
            }), 400

        # ----------------------------------------------------
        # CREATE UNIQUE FILE NAME
        # ----------------------------------------------------

        filename = (
            str(uuid.uuid4())
            + extension
        )

        result_path = os.path.join(
            RESULT_FOLDER,
            filename
        )

        # ----------------------------------------------------
        # SAVE RESULT
        # ----------------------------------------------------

        success = cv2.imwrite(
            result_path,
            result
        )

        if not success:

            return jsonify({
                "error": "Could not save processed image"
            }), 500

        # ----------------------------------------------------
        # RESULT URL
        # ----------------------------------------------------

        result_url = (
            "/static/results/"
            + filename
        )

        return jsonify({

            "success": True,

            "result": result_url,

            "operation": operation

        })

    except Exception as e:

        print("ERROR:", e)

        return jsonify({

            "error": str(e)

        }), 500


# ============================================================
# START SERVER
# ============================================================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )