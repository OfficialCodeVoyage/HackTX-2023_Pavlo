import xml.etree.ElementTree as ET
import os

# Function to parse XML annotations and generate the positive sample list
def convert_xml_to_samples(xml_directory, output_file):
    with open(output_file, 'w') as output:
        for xml_file in os.listdir(xml_directory):
            if xml_file.endswith(".xml"):
                tree = ET.parse(os.path.join(xml_directory, xml_file))
                root = tree.getroot()

                # Extract image file path
                image_path = os.path.splitext(xml_file)[0] + ".jpg"

                for obj in root.findall(".//object"):
                    # Extract object information
                    name = obj.find("name").text
                    bndbox = obj.find("bndbox")
                    xmin = int(float(bndbox.find("xmin").text))
                    ymin = int(float(bndbox.find("ymin").text))
                    xmax = int(float(bndbox.find("xmax").text))
                    ymax = int(float(bndbox.find("ymax").text))
                    width = xmax - xmin
                    height = ymax - ymin

                    # Write to the positive sample list file
                    output.write(f"{image_path} 1 {xmin} {ymin} {width} {height}\n")

# Specify the directory containing XML annotations and the output file
xml_directory = "path/to/xml/annotations"
output_file = "positive_samples.txt"

# Convert XML annotations to the positive sample list
convert_xml_to_samples(xml_directory, output_file)
