import json

FILE_HEADER = """\
/*
  Open Color CSS Classes: https://github.com/dhreck/open-color_css-classes


  Open Color: MIT License Copyright (c) 2016 heeyeun https://github.com/yeun/open-color
*/

"""

SECTION_COLOR_HEADER = """
/* #################### {color_name} #################### */

"""

CLASS_TEMPLATE = """\
.oc-{class_name}-{color_name}-{color_variant} {{
	{css_attr}: {color}
}}

"""

# [class_name]: [css_attr]
CLASSES = {
    "bg": "background",
    "cl": "color",

}

FILE_NAME_TEMPLATE = "oc-{name}.css"

if __name__ == "__main__":
    with open("open-color.json") as f:
        color_data = json.load(f)

    for class_name, attr_name in CLASSES.items():
        fn = FILE_NAME_TEMPLATE.format(
            name=class_name
        )

        file = open(fn, "w", encoding="utf8")
        file.write(FILE_HEADER)

        for color_name, variants in color_data.items():
            file.write(
                SECTION_COLOR_HEADER.format(color_name=color_name)
            )

            if not isinstance(variants, list):
                variants = [variants]

            for i, color in enumerate(variants):
                css = CLASS_TEMPLATE.format(
                    class_name=class_name,
                    color_name=color_name,
                    color_variant=i,
                    css_attr=attr_name,
                    color=color

                )

                file.write(css)

        file.close()
