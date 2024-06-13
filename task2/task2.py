data = {"alis": 15, "john":20, "anna":30, "tom":40,"annie":50}

for key,value in data.items():
    with open(f"mod3/task2/{key}.txt", "a") as file:
        file.write(f"{key}: {value}")
