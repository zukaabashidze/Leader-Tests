def traveling(dist):
    n = len(dist)
    cities = list(range(n))
    min_cost = [float('inf')]

    def calculate_cost(route):
        return sum(dist(route[i]][route[i + 1]] for i in range(n - 1)))
    
    def perform(cities, start=1):
        if start == n:
            cost = calculate_cost(cities + [cities])
    return cities

#მოკლედდ რაა მართლა ვიცეკვებ აჭარულს ოღონდ ეს მაპატიიეეთ :D