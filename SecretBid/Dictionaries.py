test = {"bug": "Error",
        "bug2": "1Hora",
        "bug3": "Goku", }

print(test.keys())

test["Vegeta"] = "The strongest in the universe"
print(test)


#Nesting
# travel_log = {
#         "France": ["Paris", "Lille", "Dijon"],
#         "Germany": ["Stuttgart", "Berlin"],
# }
#
# nested_list = ["A", "B", ["C","D"]]
#
# print(travel_log["France"][1])
# print(nested_list[2][0])

travel_log = {
        "France": {"cities_visited": ["Paris", "Lille", "Dijon"],
                   "total_visits": 12
                   },
        "Germany": {"cities_visited": ["Stuttgart", "Berlin"],
                    "total_visits": 5
                    },

}

print(travel_log["Germany"]["cities_visited"][0])
