"""
Learning Roadmap Generator
"""

def generate_roadmap(role):

    roadmap = {

        "Python Developer":[
            "Python",
            "OOP",
            "SQL",
            "Django"
        ],

        "AI/ML Engineer":[
            "Python",
            "NumPy",
            "Pandas",
            "TensorFlow"
        ]

    }

    return roadmap.get(role, [])