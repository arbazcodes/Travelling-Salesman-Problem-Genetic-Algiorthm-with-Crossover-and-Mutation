#graph

cities = {"P": "Peshawar",
          "I": "Islamabad",
          "S": "Sialkot",
          "K": "Karachi",
          "L": "Lahore",
          "M": "Multan"}

total_cities = 6

position = {"P": 0,
            "I": 1,
            "S": 2,
            "K": 3,
            "L": 4,
            "M": 5}
                              
graph = [[0, 20, float('inf'), 250, float('inf'), 100], 
         [20, 0, 30, float('inf'), 40, float('inf')], 
         [float('inf'), 30, 0, 200, float('inf'), float('inf')], 
         [250, float('inf'), 200, 0, 180, float('inf')],
         [float('inf'), 40, float('inf'), 180, 0, 90],
         [100, float('inf'), float('inf'), float('inf'), 90, 0]]

initial_population = ["PISKLMP", "LISKPML", "ILMPKSI", "KPMLISK", "SIPMLKS"]