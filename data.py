country_data = {

    "nigeria": {
        "description": "A West African nation known for jollof rice, diverse regional stews (egusi, ogbono), and street foods such as suya.",
        "recipes": {
            "Main": [
                {
                    "name": "Jollof Rice",
                    "image": "jollof.png",
                    "ingredients": ["Rice", "Tomatoes", "Bell pepper", "Onions", "Stock cube", "Oil"],
                    "instructions": ["Heat the oil in a pan.", "Add the onions and sauté until golden.", "Add the rice and stir for 2 minutes.", "Pour in water and cook until done."]
                },
                {
                    "name": "Egusi Soup",
                    "image": "egusi.jpg",
                    "ingredients": ["Egusi", "Palm oil", "Spinach", "Meat", "Stock"],
                    "instructions": ["Fry egusi mixture, add broth, meat, and vegetables; simmer until thick."]
                }
            ],
            "Side": [
                {
                    "name": "Fried Plantain",
                    "image": "plantain.jpg",
                    "ingredients": ["Ripe plantains", "Oil", "Salt"],
                    "instructions": "Slice plantains and fry in hot oil until golden."
                }
            ],
            "Dessert": [
                {
                    "name": "Chin Chin",
                    "image": "chinchin.jpg",
                    "ingredients": ["Flour", "Sugar", "Milk", "Butter", "Oil"],
                    "instructions": "Mix dough, cut into pieces, and fry until crispy."
                }
            ]
        },
        "quiz": [
                {"type":"mcq","question":"Which spice/ingredient gives Jollof Rice much of its colour and flavour?","options":["Turmeric","Tomato","Saffron","Curry powder"],"answer":"Tomato"},
                {"type":"mcq","question":"Suya is traditionally served with which accompaniment?","options":["Grated coconut","Onions and slices of tomato","Boiled yams","Plantain chips"],"answer":"Onions and slices of tomato"},
                {"type":"mcq","question":"Egusi soup is primarily made from which ingredient?","options":["Ground melon seeds","Peanut butter","Cassava flour","Coconut milk"],"answer":"Ground melon seeds"},
                {"type":"tf","question":"Pounded yam is commonly eaten with Nigerian soups such as egusi. (True/False)","answer":True},
                {"type":"tf","question":"Nigeria’s cuisine is uniform across the country with no regional variations. (True/False)","answer":False},
                {"type":"tf","question":"Suya originated as a roadside skewered meat snack. (True/False)","answer":True}
            ]
    },

    "ghana": {
        "description": ".Ghanaian cuisine features hearty stews and staples like fufu and waakye; street snacks include kelewele (spicy fried plantain).",
        "recipes": {
            "Main": [
                {
                    "name": "Waakye",
                    "image": "waakye.jpg",
                    "ingredients": ["Rice", "Black-eyed beans", "Waakye leaves"],
                    "instructions": "Cook beans and rice together with waakye leaves for colour."
                },
                {
                    "name": "Light Soup",
                    "image": "light_soup.jpg",
                    "ingredients": ["Tomatoes", "Pepper", "Fish or meat", "Onions"],
                    "instructions": "Blend vegetables; simmer with meat and seasonings."
                }
            ],
            "Side": [
                {
                    "name": "Kelewele",
                    "image": "kelewele.jpg",
                    "ingredients": ["Plantains", "Ginger", "Chili", "Oil"],
                    "instructions": "Season diced plantain with spices and fry until crispy."
                }
            ],
            "Dessert": [
                {
                    "name": "Atadwe Milk",
                    "image": "atadwe_milk.jpg",
                    "ingredients": ["Tiger nuts", "Sugar", "Water"],
                    "instructions": "Blend soaked tiger nuts with water and sweeten lightly."
                }
            ]
        },
        "quiz": [
                {"type":"mcq","question":"Waakye is commonly cooked with which ingredient to give it colour and flavour?","options":["Banana leaves","Bay leaves","Waakye (dried sorghum) leaves/beans water","Tea leaves"],"answer":"Waakye (dried sorghum) leaves/beans water"},
                {"type":"mcq","question":"Kelewele is best described as:","options":["A spicy fried plantain snack","A fermented porridge","A coconut milk pudding","A meat stew"],"answer":"A spicy fried plantain snack"},
                {"type":"mcq","question":"Ghanaian 'Light Soup' often accompanies which starchy side?","options":["Fufu","Risotto","Chapati","Naan"],"answer":"Fufu"},
                {"type":"tf","question":"Kelewele is typically seasoned with ginger and chili. (True/False)","answer":True},
                {"type":"tf","question":"Ghanaian cuisine makes no use of palm oil. (True/False)","answer":False},
                {"type":"tf","question":"Waakye can be served with fried plantain and gari. (True/False)","answer":True}
            ]
    },

    "senegal": {
        "description": "Senegalese cuisine blends coastal seafood flavours with rich spices and tomato bases; Thieboudienne (fish and rice) is a national classic.",
        "recipes": {
            "Main": [
                {
                    "name": "Thieboudienne",
                    "image": "thieb.jpg",
                    "ingredients": ["Fish", "Rice", "Tomato paste", "Vegetables"],
                    "instructions": "Cook fish in tomato stew; add rice and steam with vegetables."
                }
            ],
            "Side": [
                {
                    "name": "Accara",
                    "image": "accara.jpg",
                    "ingredients": ["Black-eyed peas", "Onions", "Oil"],
                    "instructions": "Blend soaked beans with onions and fry into fritters."
                }
            ],
            "Dessert": [
                {
                    "name": "Sombi (Coconut Rice Pudding)",
                    "image": "sombi.jpg",
                    "ingredients": ["Rice", "Coconut milk", "Sugar"],
                    "instructions": "Cook rice in coconut milk and sweeten gently."
                }
            ]
        },
        "quiz": [
                {"type":"mcq","question":"Thieboudienne is primarily a dish of:","options":["Lamb and couscous","Fish, rice and vegetables","Fried plantain and beans","Grilled chicken and yams"],"answer":"Fish, rice and vegetables"},
                {"type":"mcq","question":"Yassa is a Senegalese dish known for heavy use of which ingredient?","options":["Lemon (citrus)","Coconut milk","Peanut butter","Sour cream"],"answer":"Lemon (citrus)"},
                {"type":"mcq","question":"Accara are similar to which of the following?","options":["Fritters made from black-eyed peas","Steamed rice cakes","Baked custards","Fresh salads"],"answer":"Fritters made from black-eyed peas"},
                {"type":"tf","question":"Senegal is a coastal country so seafood features heavily in its cuisine. (True/False)","answer":True},
                {"type":"tf","question":"Thieboudienne normally includes vegetables cooked with the fish broth. (True/False)","answer":True},
                {"type":"tf","question":"Senegalese cooking rarely uses tomatoes. (True/False)","answer":False}
            ]
    },

    "kenya": {
        "description": "Kenyan food includes staples such as ugali and sukuma wiki, grilled meats like nyama choma, and coastal pilau influenced by Arab spices.",
        "recipes": {
            "Main": [
                {
                    "name": "Ugali and Sukuma Wiki",
                    "image": "ugali.jpg",
                    "ingredients": ["Maize flour", "Water", "Collard greens"],
                    "instructions": "Cook maize flour into a stiff dough; sauté greens and serve together."
                }
            ],
            "Side": [
                {
                    "name": "Chapati",
                    "image": "chapati.jpg",
                    "ingredients": ["Flour", "Oil", "Salt", "Water"],
                    "instructions": "Knead dough, roll into circles, and fry on a hot pan."
                }
            ],
            "Dessert": [
                {
                    "name": "Mahamri",
                    "image": "mahamri.jpg",
                    "ingredients": ["Flour", "Yeast", "Coconut milk", "Sugar"],
                    "instructions": "Fry slightly sweet coconut dough until golden and puffy."
                }
            ]
        },
        "quiz": [
                {"type":"mcq","question":"Ugali is primarily made from which ingredient?","options":["Cassava","Rice","Maize (corn) flour","Wheat flour"],"answer":"Maize (corn) flour"},
                {"type":"mcq","question":"Nyama choma is best described as:","options":["A sweet dessert","Grilled/roasted meat","A fish stew","A coconut rice"],"answer":"Grilled/roasted meat"},
                {"type":"mcq","question":"Pilau in Kenya often uses which spice blend?","options":["Berbere","Garam masala","Pilau spice (cardamom, cumin, cloves)","Ras el hanout"],"answer":"Pilau spice (cardamom, cumin, cloves)"},
                {"type":"tf","question":"Chapati is a flatbread commonly eaten in Kenya. (True/False)","answer":True},
                {"type":"tf","question":"Nyama choma is usually served alone without any side dishes. (True/False)","answer":False},
                {"type":"tf","question":"Ugali has a stiff, dough-like texture when cooked correctly. (True/False)","answer":True}
            ]
    },

    "ethiopia": {
        "description": "Ethiopian cuisine is notable for injera (fermented flatbread) and spicy stews (wats) such as doro wat, often eaten communally.",
        "recipes": {
            "Main": [
                {
                    "name": "Doro Wat",
                    "image": "doro_wat.jpg",
                    "ingredients": ["Chicken", "Berbere spice", "Onions", "Eggs"],
                    "instructions": "Slow-cook onions and spices; add chicken and simmer until tender."
                }
            ],
            "Side": [
                {
                    "name": "Injera",
                    "image": "injera.jpg",
                    "ingredients": ["Teff flour", "Water"],
                    "instructions": "Ferment batter; cook on a flat pan to form spongy bread."
                }
            ],
            "Dessert": [
                {
                    "name": "Himbasha",
                    "image": "himbasha.jpg",
                    "ingredients": ["Flour", "Sugar", "Cardamom", "Yeast"],
                    "instructions": "Bake a soft, lightly sweetened flatbread flavoured with cardamom."
                }
            ]
        },
        "quiz": [
                {"type":"mcq","question":"Injera is typically made from which flour?","options":["Wheat","Teff","Rice","Maize"],"answer":"Teff"},
                {"type":"mcq","question":"Doro wat is primarily a:","options":["Vegetable salad","Chicken stew","Pasta dish","Seafood rice"],"answer":"Chicken stew"},
                {"type":"mcq","question":"Berbere is:","options":["A type of flatbread","A spice mix","A cooking pot","A fermented drink"],"answer":"A spice mix"},
                {"type":"tf","question":"Ethiopian meals are often served on a single communal platter. (True/False)","answer":True},
                {"type":"tf","question":"Injera is eaten with the hands and used as a utensil. (True/False)","answer":True},
                {"type":"tf","question":"Ethiopian cuisine uses minimal spices. (True/False)","answer":False}
            ]
    },

    "morocco": {
        "description": "Moroccan food blends sweet and savoury flavours—tagines, couscous, and pastries—using spices like cinnamon, cumin and preserved lemon.",
        "recipes": {
            "Main": [
                {
                    "name": "Chicken Tagine",
                    "image": "tagine.jpg",
                    "ingredients": ["Chicken", "Preserved lemon", "Olives", "Spices"],
                    "instructions": "Slow-cook chicken with spices in a tagine pot."
                }
            ],
            "Side": [
                {
                    "name": "Couscous",
                    "image": "couscous.jpg",
                    "ingredients": ["Couscous", "Stock", "Vegetables"],
                    "instructions": "Steam couscous over broth and fluff before serving."
                }
            ],
            "Dessert": [
                {
                    "name": "Msemen with Honey",
                    "image": "msemen.jpg",
                    "ingredients": ["Flour", "Semolina", "Butter", "Honey"],
                    "instructions": "Pan-fry layered flatbread and drizzle with honey."
                }
            ]
        },
        "quiz": [
                {"type":"mcq","question":"A tagine is:","options":["A cooking vessel and the stew cooked in it","A type of flatbread","A sweet pastry","A spice mix"],"answer":"A cooking vessel and the stew cooked in it"},
                {"type":"mcq","question":"Which ingredient is commonly paired with meat in Moroccan sweet-savory dishes?","options":["Chocolate","Preserved lemon","Soy sauce","Maple syrup"],"answer":"Preserved lemon"},
                {"type":"mcq","question":"Couscous is traditionally made from:","options":["Wheat semolina","Rice flour","Cornmeal","Lentil flour"],"answer":"Wheat semolina"},
                {"type":"tf","question":"Moroccan cuisine often blends fruits or dried fruit with meat. (True/False)","answer":True},
                {"type":"tf","question":"Tagine dishes are always very spicy hot. (True/False)","answer":False},
                {"type":"tf","question":"Couscous is usually steamed rather than boiled. (True/False)","answer":True}
            ]
    },

    "egypt": {
        "description": "Egyptian cuisine features dishes such as koshari, ful medames and molokhia, reflecting Nile-based agriculture and Levantine influences.",
        "recipes": {
            "Main": [
                {
                    "name": "Koshari",
                    "image": "koshari.jpg",
                    "ingredients": ["Lentils", "Rice", "Pasta", "Tomato sauce"],
                    "instructions": "Layer rice, lentils, pasta, and top with spicy tomato sauce."
                }
            ],
            "Side": [
                {
                    "name": "Ful Medames",
                    "image": "ful.jpg",
                    "ingredients": ["Fava beans", "Oil", "Lemon"],
                    "instructions": "Simmer fava beans and serve with olive oil and lemon."
                }
            ],
            "Dessert": [
                {
                    "name": "Basbousa",
                    "image": "basbousa.jpg",
                    "ingredients": ["Semolina", "Sugar", "Butter", "Syrup"],
                    "instructions": "Bake semolina cake and soak in sweet syrup."
                }
            ]
        },
        "quiz": [
                {"type":"mcq","question":"Koshari is a layered dish that commonly includes which of the following?","options":["Rice, lentils and pasta","Fish and couscous","Steamed vegetables","Grilled meat only"],"answer":"Rice, lentils and pasta"},
                {"type":"mcq","question":"Ful medames is made primarily from:","options":["Fava beans","Chickpeas","Cowpeas","Lentils"],"answer":"Fava beans"},
                {"type":"mcq","question":"Molokhia is best described as:","options":["A sweet pastry","A leafy green stew/soup","A type of bread","A rice pudding"],"answer":"A leafy green stew/soup"},
                {"type":"tf","question":"Koshari originated as a street food and comfort dish. (True/False)","answer":True},
                {"type":"tf","question":"Ful medames is typically eaten for breakfast in Egypt. (True/False)","answer":True},
                {"type":"tf","question":"Egyptian cuisine has no Mediterranean influences. (True/False)","answer":False}
            ]
    },

    "south_africa": {
        "description": "South African cuisine is multicultural (e.g., braai/BBQ, bobotie, bunny chow), reflecting African, Dutch, Indian and Malay influences.",
        "recipes": {
            "Main": [
                {
                    "name": "Bobotie",
                    "image": "bobotie.jpg",
                    "ingredients": ["Minced meat", "Spices", "Egg custard"],
                    "instructions": "Bake seasoned minced meat topped with custard."
                }
            ],
            "Side": [
                {
                    "name": "Chakalaka",
                    "image": "chakalaka.jpg",
                    "ingredients": ["Peppers", "Beans", "Carrots"],
                    "instructions": "Cook vegetables with spices into a chunky relish."
                }
            ],
            "Dessert": [
                {
                    "name": "Melktert",
                    "image": "melktert.jpg",
                    "ingredients": ["Milk", "Sugar", "Cinnamon", "Pastry"],
                    "instructions": "Bake creamy milk tart with cinnamon topping."
                }
            ]
        },
        "quiz": [
                {"type":"mcq","question":"What does 'braai' refer to in South Africa?","options":["A type of dessert","A barbecue/grill","A spicy stew","A breakfast porridge"],"answer":"A barbecue/grill"},
                {"type":"mcq","question":"Bunny chow originally comes from which community?","options":["Indian community in Durban","Dutch settlers","Zulu tradition","Portuguese traders"],"answer":"Indian community in Durban"},
                {"type":"mcq","question":"Bobotie is a dish that typically includes:","options":["Minced meat with spiced custard topping","Raw fish","Stuffed vegetables only","A rice pudding"],"answer":"Minced meat with spiced custard topping"},
                {"type":"tf","question":"Chakalaka is a vegetable relish often served at braais. (True/False)","answer":True},
                {"type":"tf","question":"Bunny chow is a bread loaf filled with curry. (True/False)","answer":True},
                {"type":"tf","question":"South African cuisine is homogeneous across the country. (True/False)","answer":False}
            ]
    },

    "cameroon": {
        "description": "Cameroonian cuisine combines rainforest and coastal ingredients—ndolé, poulet DG and spicy stews are regional favourites.",
        "recipes": {
            "Main": [
                {
                    "name": "Ndolé",
                    "image": "ndole.jpg",
                    "ingredients": ["Bitterleaf", "Peanuts", "Meat"],
                    "instructions": "Cook bitterleaf with peanut paste and meat into a rich stew."
                }
            ],
            "Side": [
                {
                    "name": "Puff Puff",
                    "image": "puff_puff.jpg",
                    "ingredients": ["Flour", "Sugar", "Yeast"],
                    "instructions": "Fry sweet yeasted dough until golden."
                }
            ],
            "Dessert": [
                {
                    "name": "Corn Fritters",
                    "image": "corn_fritters.jpg",
                    "ingredients": ["Corn", "Flour", "Oil"],
                    "instructions": "Mix corn batter and fry until crispy."
                }
            ]
        },
        "quiz": [
                {"type":"mcq","question":"Ndolé is primarily made from which leafy ingredient?","options":["Bitterleaf or ndolé leaves","Spinach only","Kale","Lettuce"],"answer":"Bitterleaf or ndolé leaves"},
                {"type":"mcq","question":"Poulet DG commonly pairs chicken with which side?","options":["Plantains and vegetables","Sushi rice","Pasta","Pancakes"],"answer":"Plantains and vegetables"},
                {"type":"mcq","question":"Cameroon includes cuisines influenced by which of these?","options":["Rainforest, coastal and savanna regions","Only Mediterranean cuisine","Only French dessert traditions","Only Japanese influences"],"answer":"Rainforest, coastal and savanna regions"},
                {"type":"tf","question":"Ndolé often includes peanuts or peanut paste. (True/False)","answer":True},
                {"type":"tf","question":"Cameroon is landlocked with no coastal culinary influences. (True/False)","answer":False},
                {"type":"tf","question":"Poulet DG is a celebratory dish often served at gatherings. (True/False)","answer":True}
            ]
    },

    "zimbabwe": {
        "description": "Zimbabwean cuisine is maize-based (sadza), with stews, leafy greens and snacks; meals are often simple and hearty.",
        "recipes": {
            "Main": [
                {
                    "name": "Sadza",
                    "image": "sadza.jpg",
                    "ingredients": ["Maize meal", "Water"],
                    "instructions": "Cook maize meal into a firm porridge."
                }
            ],
            "Side": [
                {
                    "name": "Muriwo Unedovi",
                    "image": "muriwo.jpg",
                    "ingredients": ["Greens", "Peanut butter"],
                    "instructions": "Cook greens and mix with peanut butter sauce."
                }
            ],
            "Dessert": [
                {
                    "name": "Mapopo Candy (Papaya Strips)",
                    "image": "mapopo.jpg",
                    "ingredients": ["Papaya", "Sugar"],
                    "instructions": "Cook papaya strips in sugar syrup until chewy."
                }
            ]
        },
        "quiz": [
                {"type":"mcq","question":"Sadza is most similar to which of these?","options":["Porridge made from maize meal","Rice pilaf","Baked bread loaf","Noodles"],"answer":"Porridge made from maize meal"},
                {"type":"mcq","question":"Muriwo unedovi is a dish combining greens with which ingredient?","options":["Peanut butter","Yogurt","Tomato jam","Coconut milk"],"answer":"Peanut butter"},
                {"type":"mcq","question":"Mapopo candy uses which fruit as its base?","options":["Papaya","Mango","Banana","Guava"],"answer":"Papaya"},
                {"type":"tf","question":"Sadza is traditionally eaten with the hands or a serving utensil, not forks. (True/False)","answer":True},
                {"type":"tf","question":"Zimbabwean cuisine heavily features maize as a staple. (True/False)","answer":True},
                {"type":"tf","question":"Mapopo candy is a savoury fermented dish. (True/False)","answer":False}
            ]
    }

}
