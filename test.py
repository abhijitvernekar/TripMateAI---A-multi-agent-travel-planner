from  tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent


# res = tavily_search("Best hotel in India")
# print(res)

# print(search_flights("plan a 7 days Japan trip from Pune"))

response = run_travel_agent("search flight to kashmir")

print(response["answer"])

