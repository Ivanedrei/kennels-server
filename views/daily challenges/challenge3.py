# We're pretending that "world_supply_string" is an
# example data-set representing all the doors and wheels of the world.
# write code that will give you an answer to the question,
# QUESTION 1: "are there more doors or wheels in the world?"
# As groups, break down step by step what you'll need to do to discover the answer
# (hint: think about what Alex demonstrated to parse the url string in our request_handler.py file)
# QUESTION 2: "By how much are there more doors or wheels in the world?"

world_supply_string = "wheel|wheel|wheel|door|wheel|wheel|door|door|door|wheel|door|door|wheel|wheel|wheel|wheel|door|door|door|wheel|door|door|door|door|door|door|door|door|door|wheel|wheel|door|wheel|wheel|door|door|door|wheel|wheel|wheel|door|door|door|door|door|wheel|door|door|door|door|door|door|door|wheel|door|wheel|wheel|wheel|wheel|door|door|wheel|wheel|door|wheel|door|door|door|wheel|door|wheel|door|wheel|wheel|wheel|wheel|wheel|door|wheel|wheel|wheel|door|wheel|wheel|wheel|wheel|door|door|wheel|door|door|door|wheel|wheel|door|wheel|door|door|wheel|wheel"

new_array = world_supply_string.split("|")
Wheel_count = world_supply_string.count("wheel")
Door_count = world_supply_string.count("door")
print(Wheel_count, Door_count)


    # for x,string in enumerate(world_supply_string):
    #     if string === "wheel"
    
# def main():
#     “”"
#     “”"
#     name_of_your_function()
# if __name__ == “__main__“:
#     main()    


# WORLD_SUPPLY_STRING = "wheel|wheel|wheel|door|wheel|wheel|door|door|door|wheel|door|door|wheel|wheel|wheel|wheel|door|door|door|wheel|door|door|door|door|door|door|door|door|door|wheel|wheel|door|wheel|wheel|door|door|door|wheel|wheel|wheel|door|door|door|door|door|wheel|door|door|door|door|door|door|door|wheel|door|wheel|wheel|wheel|wheel|door|door|wheel|wheel|door|wheel|door|door|door|wheel|door|wheel|door|wheel|wheel|wheel|wheel|wheel|door|wheel|wheel|wheel|door|wheel|wheel|wheel|wheel|door|door|wheel|door|door|door|wheel|wheel|door|wheel|door|door|wheel|wheel"


# def ice_breaker_challenge():
#     """The parent function that houses two portions of this Ice Breaker Challenge
#     """
#     # find most occurring string value after parsing world_supply_string
#     list_values, most_common_str, least_common_str = _find_most_occurring(
#         WORLD_SUPPLY_STRING)

#     question_one_answer = f"There are more {most_common_str}s than {least_common_str}s in the world"

#     calculated_amount_difference = _by_how_much(
#         list_values, most_common_str, least_common_str)

#     question_two_answer = f"by {calculated_amount_difference} {most_common_str}s"

#     print(question_one_answer)
#     print(f"{question_one_answer} {question_two_answer}")


# def _find_most_occurring(world_supply_string: str):
#     """ Finds the most and least occurring string value after parcing a string by its pipe "|" delimiter

#     Args:
#         world_supply_string (str): a string of all the doors and wheels of the world

#     Returns:
#         list_values (List): a List of the parced string values
#         most_common_str (str): the most common string value of the List
#         least_common_str (str): the least common string value of the List
#     """
#     list_values = world_supply_string.split("|")
#     most_common_str = max(list_values, key=list_values.count)
#     least_common_str = min(list_values, key=list_values.count)

#     return list_values, most_common_str, least_common_str


# def _by_how_much(list_x: List, str_x: str, str_y: str):
#     """ Finds the value of how much more occurrences there are of then max occurring  string

#     Args:
#         list_x (List): a List of the parced string values
#         str_x (str): the most common string value of the List
#         str_y (str): the least common string value of the List

#     Returns:
#         calculated_amount_difference (int): calculated difference of max and min amounts
#     """
#     most_common_amount = list_x.count(str_x)
#     least_common_amount = list_x.count(str_y)
#     calculated_amount_difference = most_common_amount - least_common_amount
#     return calculated_amount_difference


# def main():
#     """
#     """
#     ice_breaker_challenge()


# if __name__ == "__main__":
#     main()