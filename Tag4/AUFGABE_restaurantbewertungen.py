restaurants = [[4, 5, 4], [3, 4, 2], [5, 5, 5]]
durchschnitte = []

for i in range(len(restaurants)):
    print(f"Restaurant{i}: {restaurants[i]}")
    einzeln_bewertung = sum(restaurants[i]) / len(restaurants[i])
    print(f"Durchschnittbewertung Restaurant{i}: {einzeln_bewertung:.2f} ")

    durchschnitte.append(einzeln_bewertung)
    print()

gesamtbewertung = sum(durchschnitte) / len(durchschnitte)

print(
    f"Durchschnittliche Gesamtbewertung aller Restaurants: {gesamtbewertung:.2f}")
