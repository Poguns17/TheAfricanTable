from app import app
from models import db, Country, Recipe, QuizQuestion
from data import country_data
import json

with app.app_context():
    db.drop_all()
    db.create_all()

    for country_name, info in country_data.items():
        country = Country(
            name=country_name.lower(),   # normalize
            description=info.get("description", "")
        )
        db.session.add(country)
        db.session.flush()

        # ---- Recipes ----
        for category, recipes in info.get("recipes", {}).items():
            for r in recipes:
                recipe = Recipe(
                    name=r["name"],
                    country_id=country.id,
                    category=category,
                    image=r.get("image", ""),

                    # Store lists as JSON
                    ingredients=json.dumps(r.get("ingredients", [])),
                    instructions=json.dumps(r.get("instructions", [])),
                )
                db.session.add(recipe)

        # ---- Quiz Questions ----
        for q in info.get("quiz", []):
            question = QuizQuestion(
                country_id=country.id,
                question=q["question"],
                type=q.get("type", "mcq"),

                # Options as JSON list (if MCQ, otherwise empty)
                options=json.dumps(q.get("options", [])) if "options" in q else "[]",

                # Answer may be string or boolean → clean storage
                answer=json.dumps(q.get("answer", "")),
            )
            db.session.add(question)

    db.session.commit()

print("Database seeded successfully!")
