# data.py

country_data = {
    "nigeria": {
        "name": "Nigeria",
        "description": "Nigeria is known for its vibrant flavours, iconic jollof, rich soups, and diverse food culture shaped by over 250 ethnic groups.",
        "recipes": [
            {
                "name": "Jollof Rice",
                "image": "img/nigeria/jollof.jpg",
                "ingredients": ["Rice", "Tomato paste", "Bell peppers", "Onions", "Oil", "Stock cubes"],
                "instructions": "Blend peppers, fry in oil, add tomato paste and spices, then cook rice in the sauce until fluffy."
            },
            {
                "name": "Suya",
                "image": "img/nigeria/suya.jpg",
                "ingredients": ["Beef", "Ground peanuts", "Suya spice", "Salt", "Oil"],
                "instructions": "Season sliced beef with suya spice, grill over open flames, and serve with onions."
            },
            {
                "name": "Egusi Soup",
                "image": "img/nigeria/egusi.jpg",
                "ingredients": ["Melon seeds", "Spinach", "Palm oil", "Stock", "Meat", "Pepper mix"],
                "instructions": "Fry egusi paste in palm oil, add meat and stock, then simmer with vegetables."
            }
        ]
    },

    "ghana": {
        "name": "Ghana",
        "description": "Ghanaian cuisine is known for bold flavours, hearty stews, and comforting dishes often served with fufu or rice.",
        "recipes": [
            {
                "name": "Waakye",
                "image": "img/ghana/waakye.jpg",
                "ingredients": ["Rice", "Black-eyed peas", "Waakye leaves", "Salt"],
                "instructions": "Cook rice and beans together with waakye leaves for colour and flavour."
            },
            {
                "name": "Kontomire Stew",
                "image": "img/ghana/kontomire.jpg",
                "ingredients": ["Cocoyam leaves", "Palm oil", "Onions", "Fish", "Tomatoes"],
                "instructions": "Simmer tomatoes and onions in palm oil, add fish and chopped kontomire leaves."
            },
            {
                "name": "Ghana Jollof",
                "image": "img/ghana/jollof.jpg",
                "ingredients": ["Rice", "Tomato stew", "Spices", "Stock"],
                "instructions": "Cook rice in a seasoned tomato sauce until rich and smoky."
            }
        ]
    },

    "senegal": {
        "name": "Senegal",
        "description": "Senegalese food blends coastal influences with bold spices, creating rich stews and fresh seafood dishes.",
        "recipes": [
            {
                "name": "Thieboudienne",
                "image": "img/senegal/thieboudienne.jpg",
                "ingredients": ["Fish", "Rice", "Tomato paste", "Carrots", "Cabbage"],
                "instructions": "Simmer fish in tomato broth with vegetables, then cook rice in the same broth."
            },
            {
                "name": "Yassa Chicken",
                "image": "img/senegal/yassa.jpg",
                "ingredients": ["Chicken", "Onions", "Mustard", "Lemon"],
                "instructions": "Marinate chicken in lemon and mustard, grill, then cook in caramelised onions."
            },
            {
                "name": "Sombi",
                "image": "img/senegal/sombi.jpg",
                "ingredients": ["Rice", "Coconut milk", "Sugar"],
                "instructions": "Boil rice in coconut milk and sweeten for a creamy dessert."
            }
        ]
    },

    "kenya": {
        "name": "Kenya",
        "description": "Kenyan cuisine is warm, hearty, and influenced by coastal flavours, Maasai culture, and East African staples.",
        "recipes": [
            {
                "name": "Ugali & Sukuma Wiki",
                "image": "img/kenya/ugali.jpg",
                "ingredients": ["Maize flour", "Water", "Collard greens", "Onions"],
                "instructions": "Cook maize flour in boiling water until firm; sauté greens with onions on the side."
            },
            {
                "name": "Nyama Choma",
                "image": "img/kenya/nyama_choma.jpg",
                "ingredients": ["Goat meat", "Salt", "Spices"],
                "instructions": "Grill seasoned goat meat slowly over charcoal until smoky and tender."
            },
            {
                "name": "Kenyan Pilau",
                "image": "img/kenya/pilau.jpg",
                "ingredients": ["Rice", "Pilau spice", "Beef", "Onions"],
                "instructions": "Cook rice with beef and spices for a fragrant and savoury dish."
            }
        ]
    },

    "ethiopia": {
        "name": "Ethiopia",
        "description": "Ethiopian cuisine is rich in spices, stews, and communal eating traditions centered around injera.",
        "recipes": [
            {
                "name": "Doro Wat",
                "image": "img/ethiopia/doro_wat.jpg",
                "ingredients": ["Chicken", "Berbere spice", "Onions", "Eggs"],
                "instructions": "Simmer chicken in a rich onion and berbere sauce, add boiled eggs."
            },
            {
                "name": "Injera",
                "image": "img/ethiopia/injera.jpg",
                "ingredients": ["Teff flour", "Water"],
                "instructions": "Ferment teff batter for 2–3 days, then cook like a spongy flatbread."
            },
            {
                "name": "Misir Wat",
                "image": "img/ethiopia/misir_wat.jpg",
                "ingredients": ["Lentils", "Berbere", "Tomatoes"],
                "instructions": "Simmer lentils in berbere and tomato stew until thick and spicy."
            }
        ]
    },

    "morocco": {
        "name": "Morocco",
        "description": "Moroccan cuisine blends sweet and savoury elements with aromatic spices and colourful presentations.",
        "recipes": [
            {
                "name": "Chicken Tagine",
                "image": "img/morocco/tagine.jpg",
                "ingredients": ["Chicken", "Lemon", "Olives", "Spices"],
                "instructions": "Slow-cook chicken with preserved lemon, olives, and spices in a tagine."
            },
            {
                "name": "Couscous",
                "image": "img/morocco/couscous.jpg",
                "ingredients": ["Couscous", "Vegetables", "Broth"],
                "instructions": "Steam couscous and serve with vegetables cooked in spiced broth."
            },
            {
                "name": "Harira Soup",
                "image": "img/morocco/harira.jpg",
                "ingredients": ["Tomatoes", "Lentils", "Chickpeas"],
                "instructions": "Cook tomatoes with lentils and chickpeas for a hearty soup."
            }
        ]
    },

    "egypt": {
        "name": "Egypt",
        "description": "Egyptian food is hearty and ancient, with influences from North Africa and the Mediterranean.",
        "recipes": [
            {
                "name": "Koshari",
                "image": "img/egypt/koshari.jpg",
                "ingredients": ["Rice", "Lentils", "Pasta", "Tomato sauce"],
                "instructions": "Layer rice, lentils, and pasta; top with spiced tomato sauce and crispy onions."
            },
            {
                "name": "Ful Medames",
                "image": "img/egypt/ful.jpg",
                "ingredients": ["Fava beans", "Oil", "Lemon"],
                "instructions": "Simmer beans and serve with oil, lemon, and bread."
            },
            {
                "name": "Molokhia",
                "image": "img/egypt/molokhia.jpg",
                "ingredients": ["Molokhia leaves", "Garlic", "Broth"],
                "instructions": "Cook minced molokhia leaves in broth and garlic for a silky stew."
            }
        ]
    },

    "south_africa": {
        "name": "South Africa",
        "description": "South African cuisine reflects its multicultural history, blending sweet, savoury, and spicy dishes.",
        "recipes": [
            {
                "name": "Bobotie",
                "image": "img/south_africa/bobotie.jpg",
                "ingredients": ["Minced meat", "Eggs", "Bread", "Spices"],
                "instructions": "Bake minced meat with spiced custard topping."
            },
            {
                "name": "Bunny Chow",
                "image": "img/south_africa/bunny_chow.jpg",
                "ingredients": ["Bread loaf", "Curry"],
                "instructions": "Hollow a loaf of bread and fill with spicy curry."
            },
            {
                "name": "Chakalaka",
                "image": "img/south_africa/chakalaka.jpg",
                "ingredients": ["Beans", "Peppers", "Spices"],
                "instructions": "Cook beans with vegetables and spices for a tangy relish."
            }
        ]
    },

    "cameroon": {
        "name": "Cameroon",
        "description": "Cameroonian food is diverse, rich, and influenced by the country’s rainforests and fertile agriculture.",
        "recipes": [
            {
                "name": "Ndolé",
                "image": "img/cameroon/ndole.jpg",
                "ingredients": ["Bitterleaf", "Peanuts", "Beef"],
                "instructions": "Cook bitterleaf with peanut paste and meat until rich."
            },
            {
                "name": "Poulet DG",
                "image": "img/cameroon/poulet_dg.jpg",
                "ingredients": ["Chicken", "Plantains", "Carrots"],
                "instructions": "Cook chicken and plantains together with vegetables for a sweet-savory dish."
            },
            {
                "name": "Eru Soup",
                "image": "img/cameroon/eru.jpg",
                "ingredients": ["Eru leaves", "Beef", "Palm oil"],
                "instructions": "Simmer eru leaves with meat in palm oil."
            }
        ]
    },

    "zimbabwe": {
        "name": "Zimbabwe",
        "description": "Zimbabwean cuisine features hearty dishes and flavours influenced by local produce and traditional cooking.",
        "recipes": [
            {
                "name": "Sadza",
                "image": "img/zimbabwe/sadza.jpg",
                "ingredients": ["Maize meal", "Water"],
                "instructions": "Boil water, add maize meal, and stir until thick."
            },
            {
                "name": "Beef Stew",
                "image": "img/zimbabwe/beef_stew.jpg",
                "ingredients": ["Beef", "Tomatoes", "Onions", "Garlic"],
                "instructions": "Cook beef with vegetables for a rich stew."
            },
            {
                "name": "Muriwo Unedovi",
                "image": "img/zimbabwe/muriwo.jpg",
                "ingredients": ["Leafy greens", "Peanut butter"],
                "instructions": "Simmer greens with peanut butter until creamy."
            }
        ]
    }
}
