class ImageEditor:
    def __init__(self, canvas, crop_size_label):
        self.canvas = canvas
        self.crop_size_label = crop_size_label
        self.original_img = Image.open(os.path.join(os.path.dirname(__file__), "logo.png"))
        self.img = self.original_img.resize((600, 700))
        self.outputImage = self.img