
import frappe

def calculate_average_rating(doc, method):
    trainer_ratings = frappe.get_all("Gym Trainer Rating",
        filters={"trainer": doc.name},
        fields=["rating"]
    )

    total_ratings = len(trainer_ratings)
    total_rating_points = sum([rating.get("rating") for rating in trainer_ratings])

    if total_ratings > 0:
        average_rating = total_rating_points / total_ratings
        doc.db_set("average_rating", average_rating)
    else:
        doc.db_set("average_rating", 0)